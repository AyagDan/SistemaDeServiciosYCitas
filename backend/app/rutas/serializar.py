"""Convierte entidades en respuestas de la API."""
from app import reloj, schemas
from app.models import Cotizacion, OrdenServicio
from app.servicios import cobro


def resumen_orden(o: OrdenServicio) -> schemas.OrdenResumen:
    """Convierte una orden en su versión resumida para listados."""
    v = o.vehiculo
    return schemas.OrdenResumen(
        folio=o.folio, estado=o.estado, placas=v.placas, vehiculo=f"{v.marca} {v.modelo} {v.anio}",
        cliente=v.cliente.nombre, numero_bahia=o.numero_bahia,
        responsable=o.responsable.nombre if o.responsable else None, fecha_apertura=o.fecha_apertura,
        dias_estancia=(reloj.ahora() - reloj.utc(o.fecha_apertura)).days)


def detalle_orden(o: OrdenServicio) -> schemas.OrdenDetalle:
    """Convierte una orden en su versión completa: recepción, diagnósticos, historial y saldo."""
    r = o.recepcion
    return schemas.OrdenDetalle(
        **resumen_orden(o).model_dump(),
        kilometraje=r.kilometraje, nivel_combustible=r.nivel_combustible,
        checklist=schemas.Checklist.model_validate(r.checklist, from_attributes=True),
        fotografias=[schemas.FotoSalida.model_validate(f) for f in r.fotografias],
        recepcion_completa=r.esta_completa(),
        diagnosticos=[schemas.DiagnosticoSalida.model_validate(d) for d in o.diagnosticos],
        historial=[schemas.HistorialSalida.model_validate(h) for h in o.historial],
        total_autorizado=cobro.total_autorizado(o), saldo_pendiente=cobro.saldo_pendiente(o),
        entrega_a_credito=o.entrega_a_credito)


def cotizacion(c: Cotizacion) -> schemas.CotizacionSalida:
    """Convierte una cotización en su respuesta, con total y fecha de vencimiento."""
    return schemas.CotizacionSalida.model_validate(c)
