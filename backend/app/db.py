from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app import config


class Base(DeclarativeBase):
    """Clase base de los modelos de SQLAlchemy."""
    pass


def crear_motor(url: str = config.DATABASE_URL, **kwargs):
    """Crea el motor de la base de datos; en SQLite permite usar la conexión desde varios hilos."""
    if url.startswith("sqlite"):
        kwargs.setdefault("connect_args", {"check_same_thread": False})
    return create_engine(url, **kwargs)


engine = crear_motor()
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db():
    """Entrega una sesión de base de datos por petición y la cierra al terminar."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
