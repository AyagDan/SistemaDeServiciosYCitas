"""Fuente única de la hora. Las pruebas la sustituyen para verificar vigencias."""
from datetime import date, datetime, timezone


def ahora() -> datetime:
    """Fecha y hora actuales en UTC."""
    return datetime.now(timezone.utc)


def hoy() -> date:
    """Fecha de hoy en UTC."""
    return ahora().date()


def utc(dt: datetime) -> datetime:
    """SQLite devuelve fechas sin zona horaria; se interpretan como UTC."""
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
