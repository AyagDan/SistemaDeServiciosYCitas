"""Genera el diagrama de tecnologías del proyecto (SVG) con los íconos oficiales incrustados.

Uso (desde la raíz del repositorio):
    python docs/07-arquitectura/tecnologias/generar_diagrama.py docs/07-arquitectura/tecnologias/iconos docs/07-arquitectura/tecnologias/diagrama-tecnologias.svg

El PNG se obtiene exportando el SVG desde un navegador (por ejemplo, la captura sin interfaz de Edge o
Chrome a escala 2).
"""
import base64
import sys
from pathlib import Path

ICONOS = Path(sys.argv[1])
SALIDA = Path(sys.argv[2])
W, H = 1830, 1140

COLOR_SI = {"pydantic": "#E92063", "swagger": "#85EA2D"}


def icono(nombre):
    if nombre.startswith("si-"):
        svg = (ICONOS / f"{nombre}.svg").read_text(encoding="utf-8")
        svg = svg.replace("<svg ", f'<svg fill="{COLOR_SI[nombre[3:]]}" ', 1)
        return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
    ruta = ICONOS / nombre
    mime = "image/png" if ruta.suffix == ".png" else "image/svg+xml"
    return f"data:{mime};base64," + base64.b64encode(ruta.read_bytes()).decode()


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


partes = []
add = partes.append

PERSONA = ('<g transform="translate({x},{y})" fill="{c}"><circle cx="24" cy="13" r="11"/>'
           '<path d="M2 48c0-13 10-21 22-21s22 8 22 21z"/></g>')


def zona(x, y, w, h, titulo, color, fondo, ico=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fondo}" stroke="{color}" stroke-width="1.5"/>')
    tx = x + 18
    if ico:
        add(f'<image href="{icono(ico)}" x="{x + 14}" y="{y + 10}" width="24" height="24"/>')
        tx = x + 46
    add(f'<text x="{tx}" y="{y + 28}" class="zona" fill="{color}">{esc(titulo)}</text>')


def nodo(cx, cy, titulo, sub="", ico=None, persona=None, texto_ico=None, w=158, punteado=False):
    h = 124
    borde = 'stroke="#9aa4ae" stroke-dasharray="6 5"' if punteado else 'stroke="#c9d1d9"'
    add(f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="14" fill="#fff" {borde} '
        f'stroke-width="1.4" filter="url(#sombra)"/>')
    if ico:
        add(f'<image href="{icono(ico)}" x="{cx - 26}" y="{cy - 54}" width="52" height="52" '
            f'preserveAspectRatio="xMidYMid meet"/>')
    elif persona:
        add(PERSONA.format(x=cx - 24, y=cy - 54, c=persona))
    elif texto_ico:
        t, c = texto_ico
        add(f'<rect x="{cx - 44}" y="{cy - 50}" width="88" height="42" rx="8" fill="{c}"/>')
        add(f'<text x="{cx}" y="{cy - 22}" class="badge">{esc(t)}</text>')
    add(f'<text x="{cx}" y="{cy + 18}" class="titulo-nodo">{esc(titulo)}</text>')
    for i, linea in enumerate(sub.split("\n") if sub else []):
        add(f'<text x="{cx}" y="{cy + 35 + i * 13}" class="sub">{esc(linea)}</text>')


def ficha(cx, cy, texto, color):
    add(f'<rect x="{cx - 34}" y="{cy - 17}" width="68" height="34" rx="8" fill="#fff" stroke="{color}" stroke-width="1.6"/>')
    add(f'<text x="{cx}" y="{cy + 5}" class="ficha" fill="{color}">{esc(texto)}</text>')


ESTILOS = {
    "run": ('#3b4a5a', '', 'flecha'),
    "ci": ('#2f81f7', 'stroke-dasharray="9 6"', 'flecha-ci'),
    "doc": ('#8957e5', 'stroke-dasharray="9 6"', 'flecha-doc'),
    "pend": ('#9aa4ae', 'stroke-dasharray="3 5"', 'flecha-pend'),
}


def arista(puntos, etiqueta="", en=None, estilo="run", doble=False):
    color, guion, marca = ESTILOS[estilo]
    d = "M" + " L".join(f"{x},{y}" for x, y in puntos)
    ini = f'marker-start="url(#{marca}-ini)"' if doble else ""
    add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2" {guion} '
        f'marker-end="url(#{marca})" {ini} stroke-linejoin="round"/>')
    if etiqueta:
        if en is None:
            (x1, y1), (x2, y2) = puntos[0], puntos[-1]
            en = ((x1 + x2) / 2, (y1 + y2) / 2)
        lineas = etiqueta.split("\n")
        ancho = max(len(l) for l in lineas) * 6.3 + 12
        alto = 16 * len(lineas) + 4
        x, y = en
        add(f'<rect x="{x - ancho / 2}" y="{y - alto / 2}" width="{ancho}" height="{alto}" rx="5" '
            f'fill="#fff" fill-opacity="0.95" stroke="{color}" stroke-opacity="0.35"/>')
        for i, l in enumerate(lineas):
            add(f'<text x="{x}" y="{y - alto / 2 + 14 + i * 16}" class="etq" fill="{color}">{esc(l)}</text>')


# ---------- Encabezado ----------
add('<text x="40" y="52" class="h1">Mapa de tecnologías · Sistema de Órdenes de Servicio y Citas</text>')
add('<text x="40" y="78" class="h2">Servicio Automotriz Hermanos Ruiz · Equipo B · IDSSI-27 · Release v0.1.0 (en desarrollo) · '
    'actualizado 18/11/2026</text>')
# Leyenda
lx, ly = 1250, 40
for i, (est, txt) in enumerate([("run", "Comunicación en ejecución"), ("doc", "Generación de documentación"),
                                ("pend", "Pendiente (todavía no existe)")]):
    color, guion, marca = ESTILOS[est]
    y = ly + (i % 2) * 24
    x = lx + (i // 2) * 290
    add(f'<path d="M{x},{y} L{x + 40},{y}" stroke="{color}" stroke-width="2" {guion} marker-end="url(#{marca})"/>')
    add(f'<text x="{x + 52}" y="{y + 4}" class="leyenda">{txt}</text>')

# ---------- Zonas ----------
zona(40, 120, 300, 540, "Usuarios", "#57606a", "#f6f8fa")
zona(380, 120, 820, 540, "Backend · API REST · Python 3.12+ (probado con 3.13)", "#3572A5", "#f1f6fc", "dev-python.svg")
zona(1235, 120, 210, 540, "Datos", "#336791", "#eef4f9")
zona(400, 700, 380, 330, "Pruebas automatizadas", "#0a9edc", "#eef9fd", "dev-python.svg")
zona(820, 700, 625, 330, "Documentación del proyecto", "#8957e5", "#f6f2fd")
zona(1490, 120, 290, 910, "Versionado e integración continua", "#24292f", "#f6f8fa")

# ---------- Nodos ----------
nodo(190, 230, "Personal del taller", "recepción, mecánicos, jefe de\nmecánicos, gerente, almacén", persona="#57606a", w=190)
nodo(190, 400, "Cliente", "portal con enlace seguro\n+ código 2FA", persona="#0969da")
nodo(190, 570, "Swagger UI", "documentación interactiva\n/docs (OpenAPI)", ico="si-swagger")

nodo(490, 280, "Uvicorn", "servidor ASGI", ico="uvicorn.png")
nodo(690, 280, "FastAPI", "rutas: personal, taller,\nportal · reglas de negocio", ico="dev-fastapi.svg", w=170)
nodo(900, 280, "SQLAlchemy 2", "ORM · models.py", ico="dev-sqlalchemy.svg")
nodo(1095, 280, "psycopg 3", "driver de PostgreSQL", texto_ico=("psycopg", "#336791"))
nodo(570, 520, "Pydantic 2", "validación de datos\nschemas.py", ico="si-pydantic")
nodo(810, 520, "Notificaciones", "correo / SMS al cliente\n(hoy: bitácora simulada)", texto_ico=("✉ SMS", "#9aa4ae"),
     punteado=True, w=170)

nodo(1340, 280, "PostgreSQL 14+", "objetivo de producción\nesquema: db/schema.sql", ico="dev-postgresql.svg", w=170)
nodo(1340, 470, "SQLite", "desarrollo local\ny pruebas", ico="dev-sqlite.svg")

nodo(500, 860, "pytest", "42 pruebas del\nflujo núcleo", ico="dev-pytest.svg")
nodo(690, 860, "HTTPX", "TestClient de FastAPI", texto_ico=("HTTPX", "#3b4a5a"))

nodo(960, 860, "PlantUML", "casos de uso, clases,\nestados y proceso", ico="plantuml.png")
nodo(1160, 860, "LaTeX", "Documento de\nIngeniería", ico="dev-latex.svg", w=170)
ficha(1365, 860, "PDF", "#c62828")
add('<text x="1365" y="900" class="sub">docs/entregas/</text>')

nodo(1635, 240, "Git", "main y una rama\npor historia o tarea", ico="dev-git.svg")
nodo(1635, 430, "GitHub", "repositorio, issues\ny Pull Requests", ico="dev-github.svg", w=170)
nodo(1635, 620, "GitHub Actions", "pendiente: aún no hay\nintegración continua", ico="dev-githubactions.svg", w=170, punteado=True)
nodo(1635, 830, "Docker", "pendiente: servicio\nde PostgreSQL", ico="dev-docker.svg", punteado=True)

# ---------- Aristas: ejecución ----------
arista([(285, 230), (330, 230), (360, 262), (410, 262)], "HTTP · JSON / multipart\nsesión firmada", en=(258, 147))
arista([(270, 400), (360, 400), (360, 298), (410, 298)], "HTTP · JSON\ntoken + 2FA", en=(318, 355))
arista([(270, 570), (372, 570), (372, 318), (410, 318)], "consulta\nOpenAPI", en=(318, 528))
arista([(570, 280), (605, 280)], "ASGI", en=(588, 248))
arista([(775, 280), (821, 280)], "Session", en=(798, 248))
arista([(979, 280), (1016, 280)], "SQL", en=(997, 248))
arista([(1174, 280), (1255, 280)], "protocolo PG\nTCP 5432", en=(1214, 238))
arista([(650, 336), (600, 464)], "valida entrada\ny salida", en=(592, 400), doble=True)
arista([(735, 336), (790, 464)], "", estilo="pend")
add('<text x="832" y="408" class="etq" fill="#9aa4ae" text-anchor="start">enlaces y códigos 2FA</text>')
arista([(940, 336), (940, 470), (1261, 470)], "sqlite3 (biblioteca estándar)", en=(1100, 470))

# ---------- Aristas: pruebas ----------
arista([(579, 860), (611, 860)], "usa", en=(595, 828))
arista([(690, 804), (690, 690), (690, 336)], "llamadas a la API\nen memoria (sin red)", en=(690, 680))

# ---------- Aristas: documentación ----------
arista([(1039, 860), (1075, 860)], "", estilo="doc")
add('<text x="1057" y="845" class="etq" fill="#8957e5">PNG</text>')
arista([(1245, 860), (1331, 860)], "pdflatex", en=(1288, 828), estilo="doc")

# ---------- Aristas: versionado / CI ----------
arista([(1635, 296), (1635, 374)], "push", en=(1690, 335))
arista([(1635, 486), (1635, 564)], "", estilo="pend")
arista([(1635, 676), (1635, 774)], "", estilo="pend")
arista([(1556, 830), (1470, 830), (1470, 310), (1425, 310)], "", estilo="pend")
arista([(1720, 620), (1805, 620), (1805, 1095), (500, 1095), (500, 922)], "", estilo="pend")
arista([(1160, 1095), (1160, 922)], "", estilo="pend")

# ---------- Ensamblado ----------
def marcador(id_, color):
    return (f'<marker id="{id_}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>'
            f'<marker id="{id_}-ini" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M10,0 L0,5 L10,10 z" fill="{color}"/></marker>')


defs = "".join(marcador(m, c) for c, _, m in ESTILOS.values())
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>{defs}
<filter id="sombra" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#1f2328" flood-opacity="0.10"/></filter>
<style>
text {{ font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif; }}
.h1 {{ font-size: 28px; font-weight: 700; fill: #1f2328; }}
.h2 {{ font-size: 15px; fill: #57606a; }}
.zona {{ font-size: 16px; font-weight: 700; }}
.titulo-nodo {{ font-size: 15px; font-weight: 700; fill: #1f2328; text-anchor: middle; }}
.sub {{ font-size: 11.5px; fill: #57606a; text-anchor: middle; }}
.etq {{ font-size: 11.5px; font-weight: 600; text-anchor: middle; }}
.badge {{ font-size: 15px; font-weight: 700; fill: #fff; text-anchor: middle; }}
.ficha {{ font-size: 14px; font-weight: 700; text-anchor: middle; }}
.leyenda {{ font-size: 13px; fill: #3b4a5a; }}
</style></defs>
<rect width="100%" height="100%" fill="#ffffff"/>
{chr(10).join(partes)}
</svg>'''
SALIDA.write_text(svg, encoding="utf-8", newline="\n")
print("escrito", SALIDA, len(svg) // 1024, "KB")
