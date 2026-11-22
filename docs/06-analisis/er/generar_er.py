"""Genera el diagrama entidad-relación de la base de datos a partir de los modelos (backend/app/models.py).

Uso (desde la raíz del repositorio, con las dependencias del backend instaladas):
    python docs/06-analisis/er/generar_er.py

Escribe dos fuentes PlantUML en esta carpeta (er-1-operacion.puml y er-2-cotizacion-cobro.puml).
Para obtener las imágenes:
    java -jar plantuml.jar -charset UTF-8 -tpng docs/06-analisis/er/*.puml

Las tablas, columnas, llaves y relaciones salen de los modelos de SQLAlchemy, que son iguales a db/schema.sql,
así que el diagrama siempre coincide con la base de datos que usa el sistema.
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "backend"))

from sqlalchemy import Enum  # noqa: E402

from app import models  # noqa: E402,F401  (registra las tablas en Base.metadata)
from app.db import Base  # noqa: E402

CARPETA = Path(__file__).resolve().parent

# Mismas láminas que el diagrama de clases (docs/06-analisis/clases/).
DIAGRAMAS = {
    "er-1-operacion": (
        "Clientes, citas, recepción y orden de servicio",
        ["usuario", "cliente", "cliente_particular", "flotilla", "vehiculo", "bahia", "cita", "orden_servicio",
         "asignacion_colaborador", "historial_estado", "diagnostico", "recepcion_vehicular",
         "checklist_inspeccion", "fotografia", "token_acceso"],
    ),
    "er-2-cotizacion-cobro": (
        "Cotización, autorización, cobro y garantía",
        ["orden_servicio", "cotizacion", "detalle_cotizacion", "autorizacion", "pago", "garantia"],
    ),
}
# En la segunda lámina la orden solo aparece como referencia (sus columnas están en la primera).
SOLO_NOMBRE = {"er-2-cotizacion-cobro": {"orden_servicio"}}


def tipo_sql(col) -> str:
    """Nombre corto del tipo de la columna, como aparece en db/schema.sql."""
    if isinstance(col.type, Enum):
        return col.type.name
    try:
        return str(col.type.compile()).lower()
    except Exception:  # tipos propios de un dialecto
        return type(col.type).__name__.lower()


def entidad(tabla, solo_nombre: bool) -> list[str]:
    """Bloque PlantUML de una tabla: llave primaria arriba, luego el resto de columnas."""
    lineas = [f"entity {tabla.name} {{"]
    if not solo_nombre:
        pk = [c for c in tabla.columns if c.primary_key]
        resto = [c for c in tabla.columns if not c.primary_key]
        for c in pk:
            marca = " <<FK>>" if c.foreign_keys else ""
            lineas.append(f"  * {c.name} : {tipo_sql(c)} <<PK>>{marca}")
        lineas.append("  --")
        for c in resto:
            obligatoria = "* " if not c.nullable else ""
            marcas = []
            if c.foreign_keys:
                marcas.append("<<FK>>")
            if c.unique:
                marcas.append("<<UQ>>")
            lineas.append(f"  {obligatoria}{c.name} : {tipo_sql(c)} {' '.join(marcas)}".rstrip())
    lineas.append("}")
    return lineas


def relaciones(tablas: set[str]) -> list[str]:
    """Una línea por llave foránea entre tablas de la lámina, con su cardinalidad."""
    salida = []
    for nombre in sorted(tablas):
        tabla = Base.metadata.tables[nombre]
        for fk in sorted(tabla.foreign_keys, key=lambda f: f.parent.name):
            destino = fk.column.table.name
            if destino not in tablas:
                continue
            col = fk.parent
            # Lado de la tabla hija: 0..1 si la llave es única o primaria; si no, 0..*.
            unica = col.unique or (col.primary_key and len(tabla.primary_key.columns) == 1)
            hijo = "o|" if unica else "o{"
            # Lado de la tabla padre: 0..1 si la llave foránea admite nulos; si no, exactamente 1.
            padre = "|o" if col.nullable else "||"
            salida.append(f"{destino} {padre}--{hijo} {nombre} : {col.name}")
    return salida


def generar() -> None:
    """Escribe las fuentes .puml de las dos láminas."""
    for archivo, (titulo, tablas) in DIAGRAMAS.items():
        faltan = [t for t in tablas if t not in Base.metadata.tables]
        if faltan:
            raise SystemExit(f"Tablas que no existen en los modelos: {faltan}")
        p = ["@startuml " + archivo,
             "' Generado por docs/06-analisis/er/generar_er.py a partir de backend/app/models.py.",
             f"title Diagrama entidad-relación · {titulo}",
             "!pragma layout smetana",
             "skinparam shadowing false",
             "skinparam linetype ortho",
             "hide circle",
             ""]
        for t in tablas:
            p += entidad(Base.metadata.tables[t], t in SOLO_NOMBRE.get(archivo, set()))
            p.append("")
        p += relaciones(set(tablas))
        p += ["", "legend right", "  * columna obligatoria (NOT NULL)", "  PK llave primaria · FK llave foránea · UQ única",
              "endlegend", "@enduml", ""]
        (CARPETA / f"{archivo}.puml").write_text("\n".join(p), encoding="utf-8", newline="\n")
        print(f"Escrito {archivo}.puml")


if __name__ == "__main__":
    generar()
