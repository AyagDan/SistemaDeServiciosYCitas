"""Portal del cliente: acceso con el enlace seguro, sin contraseña (RF-02.1, CU-10, CU-11).

El token identifica una sola orden, así que el cliente no puede abrir la orden
de otro cambiando un número en la URL (OWASP A01).
"""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app import schemas
from app.db import get_db
from app.errores import NoEncontradoError
from app.models import MedioAutorizacion, TokenAcceso
from app.rutas.serializar import cotizacion
from app.servicios import cobro, cotizaciones

router = APIRouter(prefix="/portal/{token}", tags=["Portal del cliente"])


def acceso(token: str, db: Session = Depends(get_db)) -> TokenAcceso:
    """Valida el token del enlace seguro del cliente (RN-01)."""
    return cotizaciones.token_valido(db, token)


def _ultima(orden):
    """La pendiente, si hay; si no, la última emitida (aunque esté vencida o autorizada)."""
    return cotizaciones.pendiente(orden) or (orden.cotizaciones[-1] if orden.cotizaciones else None)


def _cotizacion_actual(acc: TokenAcceso):
    """Devuelve la cotización más reciente de la orden del enlace o avisa que aún no existe."""
    cot = _ultima(acc.orden)
    if not cot:
        raise NoEncontradoError("Tu vehículo todavía no tiene cotización")
    return cot


def _ip(request: Request) -> str:
    """Dirección IP desde la que el cliente hace la petición, para dejarla en la autorización."""
    return request.client.host if request.client else "0.0.0.0"


@router.get("", response_model=schemas.PortalEstado)
def estado(acc: TokenAcceso = Depends(acceso)):
    """Estado del vehículo y cotización vigente que ve el cliente (HU-02, HU-28)."""
    o = acc.orden
    cot = _ultima(o)
    return schemas.PortalEstado(
        folio=o.folio, vehiculo=f"{o.vehiculo.marca} {o.vehiculo.modelo}", placas=o.vehiculo.placas,
        estado=o.estado, historial=[schemas.HistorialSalida.model_validate(h) for h in o.historial],
        cotizacion=cotizacion(cot) if cot else None, saldo_pendiente=cobro.saldo_pendiente(o))


@router.put("/seleccion", response_model=schemas.CotizacionSalida)
def seleccionar(datos: schemas.Seleccion, acc: TokenAcceso = Depends(acceso), db: Session = Depends(get_db)):
    """El cliente elige los conceptos opcionales de su cotización (HU-13, RN-03)."""
    cot = cotizaciones.seleccionar_opcionales(_cotizacion_actual(acc), datos.seleccion)
    db.commit()
    return cotizacion(cot)


@router.post("/codigo", status_code=202)
def pedir_codigo(request: Request, acc: TokenAcceso = Depends(acceso), db: Session = Depends(get_db)):
    """Envía al correo del cliente el código de 6 dígitos para autorizar (RN-02)."""
    cotizaciones.solicitar_codigo(db, _cotizacion_actual(acc), MedioAutorizacion.Remoto,
                                  token_hash=acc.token_hash, ip=_ip(request))
    db.commit()
    return {"detail": "Te enviamos un código de 6 dígitos a tu correo"}


@router.post("/autorizacion", response_model=schemas.AutorizacionSalida)
def autorizar(datos: schemas.CodigoPresencial, request: Request, acc: TokenAcceso = Depends(acceso),
              db: Session = Depends(get_db)):
    """Confirma el código y autoriza la cotización desde el enlace del cliente (HU-14)."""
    aut = cotizaciones.confirmar_codigo(db, _cotizacion_actual(acc), datos.codigo, ip=_ip(request),
                                        token_hash=acc.token_hash)
    db.commit()
    return aut


@router.post("/rechazo", response_model=schemas.CotizacionSalida)
def rechazar(acc: TokenAcceso = Depends(acceso), db: Session = Depends(get_db)):
    """El cliente rechaza la cotización (HU-15)."""
    cot = _cotizacion_actual(acc)
    cotizaciones.rechazar(db, cot)
    db.commit()
    return cotizacion(cot)
