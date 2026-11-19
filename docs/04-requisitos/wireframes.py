"""Genera los wireframes de baja fidelidad W-01 a W-06 (Figuras 4.5 a 4.10).

Uso (desde la raíz del repositorio):
    python docs/04-requisitos/wireframes.py

Escribe docs/documento/figuras/wireframe-w01.png ... wireframe-w06.png. Requiere matplotlib.
Solo cajas, etiquetas y botones en gris: muestran la distribución de cada pantalla, no su diseño visual.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

SALIDA = Path(__file__).resolve().parents[1] / "documento" / "figuras"
GRIS, GRIS_CLARO, BORDE, TEXTO = "#cfcfcf", "#f2f2f2", "#555555", "#222222"


class Pantalla:
    """Lienzo en unidades de 0 a ancho y de 0 a alto, con el origen arriba a la izquierda."""

    def __init__(self, titulo, ancho=100, alto=70, pulgadas=(10, 7)):
        self.ancho, self.alto = ancho, alto
        self.fig, self.ax = plt.subplots(figsize=pulgadas)
        self.ax.set_xlim(0, ancho)
        self.ax.set_ylim(alto, 0)
        self.ax.axis("off")
        self.ax.add_patch(Rectangle((0, 0), ancho, alto, fill=False, ec=BORDE, lw=2))
        self.ax.add_patch(Rectangle((0, 0), ancho, 6, fc=GRIS, ec=BORDE, lw=1))
        self.texto(2, 3, titulo, tam=12, negrita=True, va="center")

    def texto(self, x, y, t, tam=9, negrita=False, ha="left", va="top", color=TEXTO):
        self.ax.text(x, y, t, fontsize=tam, ha=ha, va=va, color=color, fontweight="bold" if negrita else "normal")

    def caja(self, x, y, w, h, etiqueta="", relleno=GRIS_CLARO, tam=8, centrado=False):
        self.ax.add_patch(Rectangle((x, y), w, h, fc=relleno, ec=BORDE, lw=1))
        if etiqueta:
            if centrado:
                self.texto(x + w / 2, y + h / 2, etiqueta, tam=tam, ha="center", va="center")
            else:
                self.texto(x + 1, y + 0.8, etiqueta, tam=tam)

    def campo(self, x, y, w, etiqueta, valor=""):
        self.texto(x, y, etiqueta, tam=8)
        self.caja(x, y + 2.2, w, 3.2, valor, relleno="white", tam=8)

    def boton(self, x, y, w, h, etiqueta, oscuro=True):
        self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2,rounding_size=0.8",
                                         fc="#8a8a8a" if oscuro else GRIS_CLARO, ec=BORDE, lw=1))
        self.texto(x + w / 2, y + h / 2, etiqueta, tam=9, negrita=True, ha="center", va="center",
                   color="white" if oscuro else TEXTO)

    def casilla(self, x, y, etiqueta, marcada=False):
        self.caja(x, y, 2.2, 2.2, "x" if marcada else "", relleno="white", tam=8, centrado=True)
        self.texto(x + 3, y + 0.2, etiqueta, tam=8)

    def guardar(self, nombre):
        SALIDA.mkdir(parents=True, exist_ok=True)
        self.fig.savefig(SALIDA / nombre, dpi=150, bbox_inches="tight", facecolor="white")
        plt.close(self.fig)


def w01():
    p = Pantalla("W-01 · Recepción del vehículo (HU-01, HU-06, HU-07; CU-02)")
    p.caja(2, 8, 96, 4, "AVISO: Sin bahías disponibles. El vehículo pasa al estacionamiento de espera.",
           relleno=GRIS, tam=9)
    p.campo(2, 14, 46, "Buscar cliente o vehículo (teléfono o placas)", "971 000 0000 / PRB-001")
    p.campo(52, 14, 46, "Cita previa (opcional)", "Folio de cita")
    p.campo(2, 22, 22, "Placas"); p.campo(26, 22, 22, "Marca y modelo"); p.campo(52, 22, 22, "Kilometraje")
    p.texto(76, 22, "Combustible (5 niveles)", tam=8)
    for i, n in enumerate(["Vacío", "1/4", "1/2", "3/4", "Lleno"]):
        p.caja(76 + i * 4.4, 24.2, 4.2, 3.2, n, relleno="white", tam=6, centrado=True)
    p.texto(2, 30, "Checklist de carrocería e interiores", tam=9, negrita=True)
    for i, t in enumerate(["Carrocería", "Cristales", "Llantas", "Interiores", "Accesorios", "Tablero"]):
        p.casilla(2 + (i % 3) * 16, 33 + (i // 3) * 3.4, t, marcada=i < 4)
    p.texto(52, 30, "Fotografías obligatorias (4 de 4)", tam=9, negrita=True)
    for i, t in enumerate(["Frente", "Trasera", "Izquierda", "Derecha"]):
        p.caja(52 + i * 11.5, 33, 10.5, 9, f"[foto]\n{t}", centrado=True)
    p.caja(52, 43.5, 46, 2.5, "Indicador: 4 de 4 fotografías completas", relleno="white", tam=7)
    p.caja(2, 41, 46, 6, "Observaciones de la recepción", relleno="white")
    p.boton(70, 58, 28, 7, "Abrir orden")
    p.boton(40, 58, 26, 7, "Cancelar", oscuro=False)
    p.guardar("wireframe-w01.png")


def w02():
    p = Pantalla("W-02 · Tableta del jefe de mecánicos (HU-08, HU-09, HU-11; CU-05)")
    for i, (estado, folio, placas) in enumerate([("OCUPADA", "OS-2026-0012", "PRB-001"), ("LIBRE", "", ""),
                                                 ("OCUPADA", "OS-2026-0010", "FLT-001"), ("LIBRE", "", "")]):
        x = 2 + i * 24.25
        p.caja(x, 8, 23, 15, relleno=GRIS if estado == "OCUPADA" else "white")
        p.texto(x + 11.5, 10, f"Bahía {i + 1}", tam=11, negrita=True, ha="center")
        p.texto(x + 11.5, 14.5, estado, tam=10, ha="center")
        p.texto(x + 11.5, 18.5, f"{folio}\n{placas}" if folio else "—", tam=8, ha="center")
    p.campo(2, 26, 46, "Orden", "OS-2026-0013 · Nissan Versa · PRB-002")
    p.campo(52, 26, 46, "Mecánico responsable", "Seleccionar mecánico  v")
    p.campo(2, 33, 96, "Colaboradores (opcional)", "Agregar mecánico +")
    p.texto(2, 41, "Diagnóstico", tam=9, negrita=True)
    p.caja(2, 43.5, 84, 12, "Escribir o dictar el diagnóstico...", relleno="white")
    p.boton(88, 43.5, 10, 12, "Dictar")
    p.boton(62, 58, 36, 8, "Guardar diagnóstico (mín. 48 x 48 px)")
    p.guardar("wireframe-w02.png")


def w03():
    p = Pantalla("W-03 · Generación de cotización (HU-12, HU-16; CU-05)")
    p.texto(2, 8, "Orden OS-2026-0013 · Re-cotización v2", tam=9, negrita=True)
    cols = [("Concepto", 34), ("Tipo", 18), ("Cantidad", 12), ("Precio", 16), ("Opcional", 16)]
    x = 2
    for nombre, w in cols:
        p.caja(x, 11, w, 3.5, nombre, relleno=GRIS, tam=8)
        x += w
    filas = [("Cambio de balatas", "Mano de obra", "1", "$600.00", "no"),
             ("Juego de balatas", "Refacción", "1", "$900.00", "no"),
             ("Lavado de motor", "Mano de obra", "1", "$250.00", "sí"),
             ("Disco de freno (adicional)", "Refacción", "1", "$176.00", "no")]
    for r, fila in enumerate(filas):
        x = 2
        for (_, w), valor in zip(cols, fila):
            p.caja(x, 14.5 + r * 3.5, w, 3.5, valor, relleno="white", tam=8)
            x += w
    p.boton(2, 29.5, 22, 4.5, "+ Agregar concepto", oscuro=False)
    p.caja(52, 29.5, 46, 4.5, "Total: $1,926.00", relleno=GRIS_CLARO, tam=10)
    p.caja(52, 35, 46, 4.5, "Vence: 5 días naturales (07/11/2026)", relleno="white", tam=9)
    p.caja(2, 41, 96, 7, "Incremento sobre lo autorizado: +10.06 %. Supera el 10 %: el cliente debe autorizar\n"
                         "de nuevo con su código antes de continuar el trabajo (RN-04).", relleno=GRIS, tam=9)
    p.boton(62, 58, 36, 7, "Enviar al cliente")
    p.guardar("wireframe-w03.png")


def w04():
    p = Pantalla("W-04 · Portal del cliente", ancho=40, alto=76, pulgadas=(4.6, 8.6))
    p.texto(20, 8, "Celular, 360 px (RNF-01)", tam=7, ha="center")
    p.texto(2, 11, "Nissan Versa · PRB-001", tam=9, negrita=True)
    for i, t in enumerate(["Recibido", "Diagnóstico", "Cotización", "Reparación", "Listo"]):
        y = 15 + i * 3.4
        p.caja(3, y, 2.2, 2.2, "", relleno=GRIS if i < 3 else "white")
        p.texto(7, y + 0.1, t, tam=8)
    p.texto(2, 33, "Cotización", tam=9, negrita=True)
    for i, (c, m, opc) in enumerate([("Cambio de balatas", "$600", False), ("Juego de balatas", "$900", False),
                                      ("Lavado de motor", "$250", True)]):
        y = 36 + i * 4
        p.caja(2, y, 36, 3.6, f"{c}   {m}", relleno="white", tam=7)
        if opc:
            p.caja(31, y + 0.7, 6, 2.2, "on", relleno=GRIS, tam=6, centrado=True)
    p.caja(2, 49, 36, 3.6, "Total: $1,750.00", relleno=GRIS_CLARO, tam=9)
    p.boton(2, 54, 17, 5, "Autorizar")
    p.boton(21, 54, 17, 5, "Rechazar", oscuro=False)
    p.texto(2, 61.5, "Código de 6 dígitos (vence en 04:59)", tam=7)
    for i in range(6):
        p.caja(2 + i * 6, 64, 5, 5, "", relleno="white")
    p.boton(2, 70.5, 36, 4, "Confirmar código")
    p.guardar("wireframe-w04.png")


def w05():
    p = Pantalla("W-05 · Agenda de citas (HU-03, HU-04; CU-01, CU-09)")
    p.caja(2, 8, 36, 59, relleno="white")
    p.texto(4, 9.5, "Solicitud pública de cita", tam=9, negrita=True)
    for i, t in enumerate(["Nombre", "Teléfono", "Correo", "Placas", "Servicio", "Día y hora"]):
        p.campo(4, 13 + i * 7, 32, t)
    p.casilla(4, 56, "Acepto el aviso de privacidad")
    p.boton(4, 60, 32, 5, "Solicitar cita")
    p.texto(42, 8, "Agenda de la recepcionista · 12/11/2026", tam=9, negrita=True)
    for b in range(4):
        p.caja(54 + b * 11, 11, 11, 3.5, f"Bahía {b + 1}", relleno=GRIS, tam=8, centrado=True)
    for h, hora in enumerate(["09:00", "10:00", "11:00", "12:00", "13:00"]):
        y = 14.5 + h * 6
        p.caja(42, y, 12, 6, hora, relleno=GRIS_CLARO, tam=8, centrado=True)
        for b in range(4):
            pendiente = (h, b) in ((0, 1), (2, 3))
            confirmada = (h, b) in ((1, 0), (3, 2))
            etiqueta = "PENDIENTE" if pendiente else ("Confirmada" if confirmada else "")
            p.caja(54 + b * 11, y, 11, 6, etiqueta, relleno=GRIS if pendiente else "white", tam=6, centrado=True)
    p.boton(54, 47, 44, 6, "Confirmar en bahía 2")
    p.texto(42, 56, "Las citas pendientes no apartan lugar hasta confirmarse (RN-08).", tam=8)
    p.guardar("wireframe-w05.png")


def w06():
    p = Pantalla("W-06 · Órdenes abiertas, cobro y entrega (HU-20 a HU-23; CU-04, CU-13)")
    cols = [("Folio", 18), ("Estado", 24), ("Bahía", 10), ("Responsable", 22), ("Días", 10)]
    x = 2
    for nombre, w in cols:
        p.caja(x, 8, w, 3.5, nombre, relleno=GRIS, tam=8)
        x += w
    filas = [("OS-2026-0010", "Lista para entrega", "3", "Mecánico A", "2"),
             ("OS-2026-0012", "En reparación", "1", "Mecánico B", "1"),
             ("OS-2026-0013", "Diagnosticada", "2", "Mecánico A", "0")]
    for r, fila in enumerate(filas):
        x = 2
        for (_, w), valor in zip(cols, fila):
            p.caja(x, 11.5 + r * 3.5, w, 3.5, valor, relleno=GRIS_CLARO if r == 0 else "white", tam=8)
            x += w
    p.caja(2, 25, 96, 30, relleno="white")
    p.texto(4, 26.5, "Detalle · OS-2026-0010 · Ford Ranger · FLT-001 (flotilla)", tam=9, negrita=True)
    p.caja(4, 31, 44, 4, "Total autorizado: $1,750.00", relleno=GRIS_CLARO, tam=9)
    p.caja(4, 36, 44, 4, "Saldo pendiente: $750.00", relleno=GRIS, tam=9)
    p.campo(52, 30, 22, "Monto del pago", "$")
    p.campo(76, 30, 20, "Método", "Efectivo  v")
    p.boton(52, 38, 44, 5, "Registrar pago")
    p.boton(4, 46, 44, 6, "Entregar (deshabilitado: hay saldo)", oscuro=False)
    p.boton(52, 46, 44, 6, "Autorizar crédito (solo gerente, flotillas)")
    p.guardar("wireframe-w06.png")


if __name__ == "__main__":
    for generar in (w01, w02, w03, w04, w05, w06):
        generar()
    print(f"Wireframes generados en {SALIDA}")
