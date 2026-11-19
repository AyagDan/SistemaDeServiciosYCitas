"""Máquina de estados de la Orden (6.5): reparación, espera de refacción y autorización adicional (RN-04, RN-06)."""
from app.models import EstadoOrden
from app.models import RolUsuario as R
from app.servicios.ordenes import TRANSICIONES
from tests.conftest import codigo_cliente, enlace_cliente

BASE = [{"concepto": "Cambio de balatas", "tipo": "ManoDeObra", "cantidad": 1, "precio_unitario": "600.00"},
        {"concepto": "Juego de balatas", "tipo": "Refaccion", "cantidad": 1, "precio_unitario": "900.00"},
        {"concepto": "Lavado de motor", "tipo": "ManoDeObra", "cantidad": 1, "precio_unitario": "250.00"}]
ADICIONAL = {"concepto": "Disco de freno", "tipo": "Refaccion", "cantidad": 1, "precio_unitario": "176.00"}  # +10.06 %


def _autorizar(c):
    token = enlace_cliente()
    assert c.post(f"/portal/{token}/codigo").status_code == 202
    return c.post(f"/portal/{token}/autorizacion", json={"codigo": codigo_cliente()})


def _en_reparacion(flujo, c, h):
    folio = flujo.hasta_diagnostico()
    flujo.cotizar(folio)
    assert _autorizar(c).status_code == 200
    r = c.post(f"/ordenes/{folio}/reparacion", headers=h[R.JefeMecanicos])
    assert r.status_code == 200 and r.json()["estado"] == "EnReparacion"
    return folio


def _orden(c, h, folio):
    return c.get(f"/ordenes/{folio}", headers=h[R.JefeMecanicos]).json()


def test_tabla_de_transiciones_cubre_todos_los_estados():
    assert set(TRANSICIONES) == set(EstadoOrden)
    assert TRANSICIONES[EstadoOrden.Autorizada] == {EstadoOrden.EnReparacion}
    assert EstadoOrden.ListaParaEntrega in TRANSICIONES[EstadoOrden.EnReparacion]


def test_no_se_termina_sin_iniciar_la_reparacion(flujo, cliente_http, h):
    folio = flujo.hasta_diagnostico()
    flujo.cotizar(folio)
    assert _autorizar(cliente_http).status_code == 200
    r = cliente_http.post(f"/ordenes/{folio}/terminar", headers=h[R.JefeMecanicos])
    assert r.status_code == 409
    assert _orden(cliente_http, h, folio)["estado"] == "Autorizada"


def test_rn06_espera_de_refaccion_libera_la_bahia_y_reanuda(flujo, cliente_http, h):
    folio = _en_reparacion(flujo, cliente_http, h)
    r = cliente_http.post(f"/ordenes/{folio}/espera-refaccion", headers=h[R.JefeMecanicos])
    assert r.status_code == 200 and r.json()["estado"] == "EsperandoRefaccion"
    assert r.json()["numero_bahia"] is None
    bahias = cliente_http.get("/bahias", headers=h[R.Recepcionista]).json()
    assert all(b["estado"] == "Libre" for b in bahias)
    # Mientras espera no se puede terminar.
    assert cliente_http.post(f"/ordenes/{folio}/terminar", headers=h[R.JefeMecanicos]).status_code == 409
    r = cliente_http.post(f"/ordenes/{folio}/reanudacion", headers=h[R.JefeMecanicos], json={"numero_bahia": 2})
    assert r.status_code == 200 and r.json()["estado"] == "EnReparacion" and r.json()["numero_bahia"] == 2
    r = cliente_http.post(f"/ordenes/{folio}/terminar", headers=h[R.JefeMecanicos])
    assert r.status_code == 200 and r.json()["estado"] == "ListaParaEntrega"


def test_rn06_no_se_reanuda_en_bahia_ocupada(flujo, cliente_http, h, datos):
    folio = _en_reparacion(flujo, cliente_http, h)
    cliente_http.post(f"/ordenes/{folio}/espera-refaccion", headers=h[R.JefeMecanicos])
    otra = flujo.abrir(datos["vehiculo_flotilla"])
    flujo.asignar(otra, bahia=1)
    r = cliente_http.post(f"/ordenes/{folio}/reanudacion", headers=h[R.JefeMecanicos], json={"numero_bahia": 1})
    assert r.status_code == 409 and r.json()["regla"] == "RN-05"
    assert _orden(cliente_http, h, folio)["estado"] == "EsperandoRefaccion"


def test_rn04_recotizacion_mayor_al_10_detiene_y_al_autorizar_reanuda(flujo, cliente_http, h):
    folio = _en_reparacion(flujo, cliente_http, h)
    cot = flujo.cotizar(folio, BASE + [ADICIONAL])
    assert cot["estado"] == "Pendiente"
    assert _orden(cliente_http, h, folio)["estado"] == "EsperandoAutorizacionAdicional"
    assert _autorizar(cliente_http).status_code == 200
    assert _orden(cliente_http, h, folio)["estado"] == "EnReparacion"


def test_rn04_rechazar_el_incremento_continua_con_lo_autorizado(flujo, cliente_http, h):
    folio = _en_reparacion(flujo, cliente_http, h)
    flujo.cotizar(folio, BASE + [ADICIONAL])
    token = enlace_cliente()
    assert cliente_http.post(f"/portal/{token}/rechazo").status_code in (200, 204)
    orden = _orden(cliente_http, h, folio)
    assert orden["estado"] == "EnReparacion"
    assert orden["total_autorizado"] == "1750.00"


def test_historial_registra_cada_transicion(flujo, cliente_http, h):
    folio = _en_reparacion(flujo, cliente_http, h)
    cliente_http.post(f"/ordenes/{folio}/espera-refaccion", headers=h[R.JefeMecanicos])
    cliente_http.post(f"/ordenes/{folio}/reanudacion", headers=h[R.JefeMecanicos], json={"numero_bahia": 1})
    estados = [e["estado_nuevo"] for e in _orden(cliente_http, h, folio)["historial"]]
    assert estados[-3:] == ["EnReparacion", "EsperandoRefaccion", "EnReparacion"]
