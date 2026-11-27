# -*- coding: utf-8 -*-
"""Genera la presentación del proyecto: docs/presentacion/IS1-Fase1-EquipoB-presentacion.pptx.

Uso (desde la raíz del repositorio): pip install python-pptx Pillow && python docs/presentacion/generar_presentacion.py

Usa los diagramas, wireframes y capturas del repositorio, así que se regenera cuando estos cambian.
"""
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

RAIZ = Path.cwd()
SALIDA = RAIZ / "docs/presentacion/IS1-Fase1-EquipoB-presentacion.pptx"

GRAFITO = RGBColor(0x26, 0x32, 0x38)
NARANJA = RGBColor(0xE8, 0x63, 0x0A)
GRIS = RGBColor(0x5F, 0x6B, 0x73)
CLARO = RGBColor(0xF1, 0xF3, 0xF4)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
TIT, CUERPO = "Cambria", "Calibri"

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
VACIA = prs.slide_layouts[6]
W, H = 13.333, 7.5


def fondo(s, color):
    f = s.background.fill
    f.solid()
    f.fore_color.rgb = color


def texto(s, x, y, w, h, contenido, size=16, color=GRAFITO, bold=False, font=CUERPO, align=PP_ALIGN.LEFT,
          anchor=MSO_ANCHOR.TOP, italic=False):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, 0)
    lineas = contenido if isinstance(contenido, list) else [contenido]
    for i, l in enumerate(lineas):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run()
        r.text = l
        r.font.size, r.font.bold, r.font.italic = Pt(size), bold, italic
        r.font.color.rgb, r.font.name = color, font
        p.space_after = Pt(6)
    return tb


def vinetas(s, x, y, w, h, items, size=16, color=GRAFITO):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, 0)
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(10)
        if isinstance(it, tuple):
            r = p.add_run()
            r.text = it[0] + " "
            r.font.bold, r.font.size, r.font.color.rgb, r.font.name = True, Pt(size), color, CUERPO
            it = it[1]
        r = p.add_run()
        r.text = it
        r.font.size, r.font.color.rgb, r.font.name = Pt(size), color, CUERPO
    return tb


def titulo(s, t, color=GRAFITO):
    texto(s, 0.6, 0.45, W - 1.2, 0.9, t, size=36, bold=True, font=TIT, color=color)


def circulo(s, x, y, d, etiqueta, relleno=NARANJA, size=18):
    c = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(d), Inches(d))
    c.fill.solid()
    c.fill.fore_color.rgb = relleno
    c.line.fill.background()
    tf = c.text_frame
    tf.margin_left = tf.margin_right = 0
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = etiqueta
    r.font.size, r.font.bold, r.font.color.rgb, r.font.name = Pt(size), True, BLANCO, CUERPO
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return c


def tarjeta(s, x, y, w, h, color=CLARO):
    r = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    r.adjustments[0] = 0.08
    r.fill.solid()
    r.fill.fore_color.rgb = color
    r.line.fill.background()
    r.shadow.inherit = False
    return r


def imagen(s, ruta, x, y, w_max, h_max):
    """Inserta la imagen ajustada a la caja, centrada."""
    ancho, alto = Image.open(RAIZ / ruta).size
    esc = min(w_max / ancho, h_max / alto)
    w, h = ancho * esc, alto * esc
    s.shapes.add_picture(str(RAIZ / ruta), Inches(x + (w_max - w) / 2), Inches(y + (h_max - h) / 2), Inches(w), Inches(h))


def pie(s, n, oscuro=False):
    texto(s, 0.6, H - 0.45, 8, 0.3, "Equipo B · Sistema de Órdenes de Servicio y Citas", size=10,
          color=(CLARO if oscuro else GRIS))
    texto(s, W - 1.6, H - 0.45, 1.0, 0.3, str(n), size=10, color=(CLARO if oscuro else GRIS), align=PP_ALIGN.RIGHT)


def notas(s, t):
    s.notes_slide.notes_text_frame.text = t


# 1. Portada ---------------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, GRAFITO)
circulo(s, 0.8, 1.2, 0.9, "B", size=28)
texto(s, 0.8, 2.4, 11.5, 1.6, "Sistema de Órdenes de Servicio y Citas", size=44, bold=True, font=TIT, color=BLANCO)
texto(s, 0.8, 3.75, 11.5, 0.6, "Servicio Automotriz Hermanos Ruiz, S.A. de C.V.", size=22, color=NARANJA)
texto(s, 0.8, 4.8, 11.5, 1.5, ["Ingeniería de Software I (IDSSI-27) · Universidad del Istmo, Campus Ixtepec",
                                "Equipo B · grupo 517 · Profesor: Florentino Ruiz Aquino",
                                "Documento de Ingeniería – Fase 1 · noviembre de 2026"], size=16, color=CLARO)
notas(s, "Presentamos el sistema que el Equipo B construye para el taller Servicio Automotriz Hermanos Ruiz.")

# 2. Problema ----------------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, BLANCO)
titulo(s, "Cinco problemas le cuestan dinero y clientes al taller")
problemas = [("Cobros en disputa", "Autorizaciones verbales: «dijo que sí, pero cobra otra cosa»."),
             ("Reclamos por daños", "Sin checklist ni fotografías del estado en que llega el vehículo."),
             ("Exceso de llamadas", "Los clientes llaman para saber el avance e interrumpen a recepción."),
             ("Bahías de palabra", "Vehículos detenidos sin justificación y carga de trabajo sin control."),
             ("Historial en carpetas", "Reparaciones y garantías difíciles de consultar.")]
for i, (t, d) in enumerate(problemas):
    col, fila = i % 3, i // 3
    x, y = 0.6 + col * 4.1, 1.7 + fila * 2.6
    tarjeta(s, x, y, 3.8, 2.3)
    circulo(s, x + 0.3, y + 0.3, 0.6, str(i + 1))
    texto(s, x + 1.1, y + 0.38, 2.5, 0.5, t, size=18, bold=True)
    texto(s, x + 0.3, y + 1.1, 3.2, 1.1, d, size=14, color=GRIS)
texto(s, 8.8, 4.55, 3.9, 2.0, "Fuente: anteproyecto y entrevista con el cliente del 19/10/2026 (Anexo A.2).",
      size=12, color=GRIS, italic=True, anchor=MSO_ANCHOR.MIDDLE)
pie(s, 2)
notas(s, "Estos problemas salen del anteproyecto y se confirmaron en la entrevista con el cliente.")

# 3. Solución: flujo núcleo -------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, BLANCO)
titulo(s, "El flujo núcleo de la Fase 1")
pasos = [("Recepción", "Cliente, vehículo, kilometraje, combustible, checklist y 4 fotografías."),
         ("Diagnóstico y asignación", "Una de las 4 bahías, un mecánico responsable y el diagnóstico en tableta."),
         ("Cotización y autorización", "Presupuesto desglosado; el cliente autoriza con un código de 6 dígitos."),
         ("Monitoreo gerencial", "Órdenes abiertas, su estado y la carga del taller.")]
for i, (t, d) in enumerate(pasos):
    x = 0.6 + i * 3.1
    circulo(s, x + 1.05, 1.9, 0.8, str(i + 1), size=22)
    if i < 3:
        f = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x + 2.2), Inches(2.15), Inches(0.7), Inches(0.3))
        f.fill.solid()
        f.fill.fore_color.rgb = GRIS
        f.line.fill.background()
    texto(s, x, 3.0, 2.9, 0.8, t, size=18, bold=True, align=PP_ALIGN.CENTER)
    texto(s, x + 0.1, 3.85, 2.7, 1.6, d, size=14, color=GRIS, align=PP_ALIGN.CENTER)
tarjeta(s, 0.6, 5.6, W - 1.2, 1.0)
texto(s, 0.9, 5.6, W - 1.8, 1.0, "Todo con herramientas de código abierto y planes educativos; el cliente consulta y "
      "autoriza desde su celular, sin instalar aplicaciones.", size=15, anchor=MSO_ANCHOR.MIDDLE)
pie(s, 3)
notas(s, "El flujo núcleo es lo que el anteproyecto pide funcionando en la Fase 1.")

# 4. Alcance -----------------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, BLANCO)
titulo(s, "Un Release v0.1.0 centrado en el flujo núcleo")
for i, (num, lab, color) in enumerate([("11", "historias en el Release v0.1.0", NARANJA),
                                        ("40", "puntos en el Release v0.1.0", NARANJA),
                                        ("19", "historias pasan a la Fase 2", GRAFITO)]):
    x = 0.6 + i * 4.1
    tarjeta(s, x, 1.8, 3.8, 2.4)
    texto(s, x + 0.3, 1.95, 3.2, 1.3, num, size=66, bold=True, color=color, font=TIT)
    texto(s, x + 0.3, 3.3, 3.2, 0.7, lab, size=16, color=GRIS)
vinetas(s, 0.6, 4.6, W - 1.2, 2.0, [
    ("Antes:", "25 historias y 92 puntos en v0.1.0 (observación B2 de la Review 1)."),
    ("Fase 2:", "operación sin conexión, cobro y entrega, citas en línea, refacciones; especificadas y diseñadas."),
    ("Estado:", "propuesta pendiente de negociar con el cliente.")], size=16)
pie(s, 4)
notas(s, "Las cifras salen de docs/04-requisitos/propuesta-release-v0.1.0.md. La decisión es del cliente.")

# 5. Reglas de negocio -------------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, BLANCO)
titulo(s, "Las reglas del taller viven en el sistema")
reglas = [("RN-02", "Doble verificación: código de 6 dígitos, de un solo uso, vigente 5 minutos."),
          ("RN-04", "Si los trabajos adicionales suben el costo más del 10 %, el cliente vuelve a autorizar."),
          ("RN-05", "4 bahías (un vehículo por bahía) y 5 lugares de espera."),
          ("RN-10", "No se entrega un vehículo con saldo, salvo crédito a flotillas autorizado por el gerente."),
          ("RN-14", "Medidor de combustible descompuesto: nivel «No verificable» y método de estimación."),
          ("RN-15", "Cortes largos de luz o internet: Bitácora de Contingencia en papel y captura en 24 h.")]
for i, (rn, d) in enumerate(reglas):
    col, fila = i % 2, i // 2
    x, y = 0.6 + col * 6.15, 1.65 + fila * 1.7
    tarjeta(s, x, y, 5.9, 1.45)
    circulo(s, x + 0.25, y + 0.3, 0.85, rn, size=12, relleno=(NARANJA if i < 4 else GRAFITO))
    texto(s, x + 1.35, y + 0.2, 4.35, 1.1, d, size=15, anchor=MSO_ANCHOR.MIDDLE)
pie(s, 5)
notas(s, "RN-14 y RN-15 son los procedimientos de contingencia que el cliente aceptó el 09/11/2026.")

# 6. Arquitectura -------------------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, BLANCO)
titulo(s, "Arquitectura de código abierto")
imagen(s, "docs/07-arquitectura/tecnologias/diagrama-tecnologias.png", 0.6, 1.5, 7.6, 5.2)
vinetas(s, 8.6, 1.7, 4.2, 5.0, [
    ("Backend:", "Python con FastAPI; documentación interactiva en /docs."),
    ("Datos:", "PostgreSQL; SQLite en desarrollo y pruebas."),
    ("Interfaz:", "PWA responsiva para la tableta del taller y el celular del cliente (wireframes W-01 a W-06)."),
    ("Calidad:", "pruebas automatizadas con pytest y solo datos ficticios.")], size=15)
pie(s, 6)
notas(s, "Mapa de tecnologías de docs/07-arquitectura/tecnologias/.")

# 7. Prototipos -----------------------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, BLANCO)
titulo(s, "Prototipos para la tableta y el celular")
imagen(s, "docs/documento/figuras/wireframe-w01.png", 0.6, 1.5, 5.9, 4.6)
imagen(s, "docs/documento/figuras/wireframe-w03.png", 6.85, 1.5, 5.9, 4.6)
texto(s, 0.6, 6.2, 5.9, 0.5, "W-01 · Recepción del vehículo", size=13, color=GRIS, align=PP_ALIGN.CENTER)
texto(s, 6.85, 6.2, 5.9, 0.5, "W-03 · Generación de cotización", size=13, color=GRIS, align=PP_ALIGN.CENTER)
pie(s, 7)
notas(s, "Seis wireframes en la sección 4.10 del Documento de Ingeniería.")

# 8. Estado actual ---------------------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, BLANCO)
titulo(s, "Hoy el backend ya aplica las reglas del flujo núcleo")
imagen(s, "assets/capturas/docs-orden.png", 0.6, 1.5, 6.6, 5.1)
vinetas(s, 7.6, 1.7, 5.2, 5.0, [
    ("API:", "recepción, asignación, diagnóstico, cotización, autorización 2FA, cobro, citas y panel."),
    ("Pruebas:", "pruebas automatizadas que pasan en un clon limpio, con evidencia en docs/pruebas/."),
    ("Modelos:", "máquina de estados de la orden, diagrama de clases y esquema de PostgreSQL."),
    ("Pendiente:", "la interfaz gráfica; mientras tanto se usa desde /docs (manual de usuario).")], size=15)
pie(s, 8)
notas(s, "Captura de /docs con datos ficticios de la demostración.")

# 9. Proceso Scrum ------------------------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, BLANCO)
titulo(s, "Proceso Scrum y correcciones de la Review 1")
hitos = [("14/10", "Inicio del Sprint 0"), ("19/10", "Entrevista con el cliente"),
         ("29/10", "Review 0 · v0.1"), ("10/11", "Review 1 · 7.4/10"), ("27/11", "Entrega de correcciones")]
linea = s.shapes.add_connector(1, Inches(1.0), Inches(2.6), Inches(W - 1.0), Inches(2.6))
linea.line.color.rgb = GRIS
for i, (f, d) in enumerate(hitos):
    x = 0.8 + i * 2.45
    circulo(s, x + 0.65, 2.25, 0.7, str(i + 1), size=16, relleno=(NARANJA if i != 4 else GRAFITO))
    texto(s, x, 3.1, 2.0, 0.4, f, size=18, bold=True, align=PP_ALIGN.CENTER)
    texto(s, x, 3.55, 2.0, 0.8, d, size=14, color=GRIS, align=PP_ALIGN.CENTER)
tarjeta(s, 0.6, 4.7, W - 1.2, 1.4)
vinetas(s, 0.9, 4.9, W - 1.8, 1.6, [
    ("Correcciones:", "cada observación B1 a B11 tiene su issue, su rama y su Pull Request, y sube un dígito la versión."),
    ("Trabajo en equipo:", "GitHub Flow, commits con la cuenta de cada rol y sesión interna de transferencia (18/11).")],
    size=15)
pie(s, 9)
notas(s, "Sprints de dos semanas; el detalle está en la sección 2.3 y en docs/minutas/.")

# 10. Siguientes pasos (cierre oscuro) -------------------------------------------------------
s = prs.slides.add_slide(VACIA)
fondo(s, GRAFITO)
titulo(s, "Siguientes pasos", color=BLANCO)
pasos = [("Negociar con el cliente", "el alcance del Release v0.1.0 (B2)."),
         ("Construir la interfaz", "PWA de la tableta y del portal del cliente."),
         ("Integración continua", "pruebas en SQLite y PostgreSQL en cada Pull Request."),
         ("Demo final", "el flujo núcleo funcionando de extremo a extremo.")]
for i, (t, d) in enumerate(pasos):
    y = 1.75 + i * 1.2
    circulo(s, 0.8, y, 0.75, str(i + 1), size=18)
    texto(s, 1.85, y + 0.02, 10.5, 0.4, t, size=20, bold=True, color=BLANCO)
    texto(s, 1.85, y + 0.45, 10.5, 0.4, d, size=15, color=CLARO)
pie(s, 10, oscuro=True)
notas(s, "Gracias. Preguntas.")

SALIDA.parent.mkdir(parents=True, exist_ok=True)
prs.core_properties.title = "Sistema de Órdenes de Servicio y Citas"
prs.core_properties.author = "Equipo B"
prs.save(SALIDA)
print("Escrito", SALIDA)
