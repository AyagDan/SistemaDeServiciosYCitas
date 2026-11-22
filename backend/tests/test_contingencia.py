"""Procedimientos de contingencia aceptados por el cliente el 09/11/2026 (4.7.1, RN-14 y RN-15)."""
from decimal import Decimal

import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Autorizacion, Cotizacion, MedioAutorizacion, OrdenServicio
from app.models import RolUsuario as R


def _recepcion(cliente_http, h, datos, **combustible):
    """Abre una orden con los datos de combustible indicados."""
    cuerpo = {"id_vehiculo": datos["vehiculo"], "kilometraje": 45210,
              "checklist": {"carroceria": "Sin daños", "interiores": "Sin daños", "completo": True}}
    cuerpo.update(combustible)
    return cliente_http.post("/ordenes", headers=h[R.Recepcionista], json=cuerpo)


def test_cpa36_no_verificable_con_metodo_se_registra(cliente_http, h, datos):
    r = _recepcion(cliente_http, h, datos, nivel_combustible="NoVerificable", metodo_combustible="OBDII")
    assert r.status_code == 201, r.text
    orden = r.json()["orden"]
    assert orden["nivel_combustible"] == "NoVerificable"
    assert orden["metodo_combustible"] == "OBDII" and orden["litros_medidos"] is None


def test_cpa37_no_verificable_sin_metodo_se_rechaza(cliente_http, h, datos):
    r = _recepcion(cliente_http, h, datos, nivel_combustible="NoVerificable")
    assert r.status_code == 409 and r.json()["regla"] == "RN-14"
    r = _recepcion(cliente_http, h, datos, nivel_combustible="Mitad", metodo_combustible="OBDII")
    assert r.status_code == 409 and r.json()["regla"] == "RN-14"


def test_cpa38_medicion_en_litros_exige_los_litros(cliente_http, h, datos):
    r = _recepcion(cliente_http, h, datos, nivel_combustible="NoVerificable", metodo_combustible="MedicionLitros")
    assert r.status_code == 409 and r.json()["regla"] == "RN-14"
    r = _recepcion(cliente_http, h, datos, nivel_combustible="NoVerificable", metodo_combustible="MedicionLitros",
                   litros_medidos="18.5")
    assert r.status_code == 201, r.text
    assert Decimal(str(r.json()["orden"]["litros_medidos"])) == Decimal("18.5")


def test_cpa39_firma_en_papel_y_folio_provisional(flujo, sesion_db):
    folio = flujo.abrir()
    with sesion_db() as db:
        orden = db.get(OrdenServicio, folio)
        orden.folio_provisional = "C-20261109-01"
        cot = Cotizacion(folio=folio, version=1)
        db.add(cot)
        db.flush()
        # RN-15: en contingencia la autorización es la firma autógrafa, sin código 2FA.
        db.add(Autorizacion(id_cotizacion=cot.id_cotizacion, medio=MedioAutorizacion.FirmaEnPapel,
                            monto_aceptado=Decimal("0"), codigo_verificacion_hash=None))
        db.commit()
        assert db.get(OrdenServicio, folio).folio_provisional == "C-20261109-01"
    with sesion_db() as db:
        otra = db.get(OrdenServicio, flujo.abrir(vehiculo=flujo.datos["vehiculo_flotilla"]))
        otra.folio_provisional = "C-20261109-01"
        with pytest.raises(IntegrityError):
            db.commit()
