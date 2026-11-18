"""Genera el diagrama de clases del dominio a partir de los modelos del backend (backend/app/models.py).

Uso (desde la raíz del repositorio, con las dependencias del backend instaladas):
    python docs/06-analisis/clases/generar_clases.py

Escribe dos fuentes PlantUML en esta carpeta (clases-1-operacion.puml y clases-2-cotizacion-cobro.puml).
Para obtener las imágenes:
    java -jar plantuml.jar -charset UTF-8 -tpng docs/06-analisis/clases/*.puml

Como el diagrama sale del código, siempre coincide con las tablas, los atributos, las relaciones y los estados
que el sistema usa de verdad.
"""
import enum
import inspect
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(RAIZ / "backend"))

from sqlalchemy import Date, DateTime, Enum, Numeric  # noqa: E402
from sqlalchemy.orm import ONETOMANY  # noqa: E402

from app import models  # noqa: E402
from app.db import Base  # noqa: E402

DIAGRAMAS = {
    "clases-1-operacion": (
        "Clientes, citas, recepción y orden de servicio",
        ["Usuario", "Cliente", "ClienteParticular", "Flotilla", "Vehiculo", "Bahia", "Cita", "OrdenServicio",
         "AsignacionColaborador", "HistorialEstado", "Diagnostico", "RecepcionVehicular", "ChecklistInspeccion",
         "Fotografia", "TokenAcceso"],
        ["RolUsuario", "TipoVehiculo", "EstadoCita", "EstadoBahia", "EstadoOrden", "NivelCombustible",
         "PosicionFoto", "Canal"],
    ),
    "clases-2-cotizacion-cobro": (
        "Cotización, autorización, cobro y garantía",
        ["OrdenServicio", "Cotizacion", "DetalleCotizacion", "Autorizacion", "Pago", "Garantia"],
        ["EstadoCotizacion", "TipoConcepto", "MedioAutorizacion", "TipoAutorizacion", "EstadoAutorizacion"],
    ),
}
# En el segundo diagrama la orden solo se muestra como referencia (sus atributos están en el primero).
SOLO_NOMBRE = {"clases-2-cotizacion-cobro": {"OrdenServicio"}}


def tipo(col):
    t = col.type
    if isinstance(t, Enum) and t.enum_class is not None:
        return t.enum_class.__name__
    if isinstance(t, DateTime):
        return "DateTime"
    if isinstance(t, Date):
        return "Date"
    if isinstance(t, Numeric):
        return "Decimal"
    try:
        nombres = {int: "int", str: "String", bool: "Boolean", float: "float"}
        n = t.python_type.__name__
        return nombres.get(t.python_type, n if n[0].isupper() else n.capitalize())
    except NotImplementedError:
        return type(t).__name__


def clases_del_modelo():
    return {m.class_.__name__: m for m in Base.registry.mappers}


def metodos(cls):
    """Métodos y propiedades definidos en la clase del modelo (no los heredados de SQLAlchemy)."""
    salida = []
    for nombre, valor in cls.__dict__.items():
        if nombre.startswith("_"):
            continue
        if isinstance(valor, property):
            salida.append(f"+ {nombre}() : {_retorno(valor.fget)}")
        elif inspect.isfunction(valor):
            salida.append(f"+ {nombre}() : {_retorno(valor)}")
    return salida


def _retorno(f):
    r = inspect.signature(f).return_annotation
    if r is inspect.Signature.empty:
        return "void"
    nombre = getattr(r, "__name__", str(r))
    return {"bool": "Boolean", "str": "String", "date": "Date", "datetime": "DateTime"}.get(nombre, nombre)


def clase_puml(mapper, solo_nombre=False):
    nombre = mapper.class_.__name__
    if solo_nombre:
        return [f'class {nombre} <<ver diagrama 1>>']
    lineas = [f"class {nombre} {{"]
    for col in mapper.columns:
        marcas = [m for m, si in (("PK", col.primary_key), ("FK", bool(col.foreign_keys))) if si]
        lineas.append(f"  - {col.key} : {tipo(col)}" + (f" {{{', '.join(marcas)}}}" if marcas else ""))
    ms = metodos(mapper.class_)
    if ms:
        lineas.append("  --")
        lineas += [f"  {m}" for m in ms]
    lineas.append("}")
    return lineas


def relaciones(mappers, nombres):
    """Una línea por relación del ORM, sin duplicar las dos direcciones de un back_populates, y una línea
    por cada llave foránea que no tiene relación en el ORM (por ejemplo, quién abrió la orden)."""
    vistas, cubiertas, lineas = set(), set(), []
    por_tabla = {mappers[n].local_table.name: n for n in nombres}
    for n in sorted(nombres):
        for rel in mappers[n].relationships:
            destino = rel.mapper.class_.__name__
            if destino not in nombres:
                continue
            for col in rel.local_columns | rel.remote_side:
                if col.foreign_keys:
                    cubiertas.add((col.table.name, col.name))
            par = tuple(sorted([n, destino])) + tuple(sorted(c.name for c in rel.local_columns | rel.remote_side))
            if par in vistas:
                continue
            vistas.add(par)
            fks = [c for c in rel.local_columns | rel.remote_side if c.foreign_keys]
            uno = "0..1" if any(c.nullable for c in fks) else "1"
            if rel.direction is ONETOMANY:
                muchos = "0..*" if rel.uselist else "0..1"
                flecha = "*--" if "delete-orphan" in str(rel.cascade) else "--"
                lineas.append(f'{n} "{uno}" {flecha} "{muchos}" {destino} : {rel.key}')
            elif rel.direction.name == "MANYTOONE":
                lineas.append(f'{destino} "{uno}" -- "0..*" {n} : {rel.key}')
            else:
                lineas.append(f"{n} -- {destino} : {rel.key}")
    for n in sorted(nombres):
        for col in mappers[n].local_table.columns:
            for fk in col.foreign_keys:
                destino = por_tabla.get(fk.column.table.name)
                if not destino or (col.table.name, col.name) in cubiertas:
                    continue
                uno = "0..1" if col.nullable else "1"
                pk_simple = col.primary_key and len(col.table.primary_key.columns) == 1
                muchos = "0..1" if pk_simple else "0..*"
                lineas.append(f'{destino} "{uno}" -- "{muchos}" {n} : {col.name}')
    return lineas


def enum_puml(nombre):
    cls = getattr(models, nombre)
    assert issubclass(cls, enum.Enum)
    return [f"enum {nombre} {{"] + [f"  {m.value}" for m in cls] + ["}"]


def generar():
    mappers = clases_del_modelo()
    for archivo, (titulo, clases, enums) in DIAGRAMAS.items():
        faltan = [c for c in clases if c not in mappers]
        assert not faltan, faltan
        p = ["@startuml " + archivo,
             f"' Generado por docs/06-analisis/clases/generar_clases.py a partir de backend/app/models.py.",
             f"title Diagrama de clases del dominio · {titulo}",
             "skinparam classAttributeIconSize 0",
             "skinparam shadowing false",
             "skinparam linetype polyline",
             "skinparam nodesep 60",
             "skinparam ranksep 70",
             "hide empty members",
             ""]
        for c in clases:
            p += clase_puml(mappers[c], c in SOLO_NOMBRE.get(archivo, set()))
        p.append("")
        for e in enums:
            p += enum_puml(e)
        p.append("")
        p += relaciones(mappers, set(clases))
        p.append("@enduml")
        (AQUI / f"{archivo}.puml").write_text("\n".join(p) + "\n", encoding="utf-8", newline="\n")
        print("escrito", archivo + ".puml")


if __name__ == "__main__":
    generar()
