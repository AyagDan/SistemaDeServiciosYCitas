"""Genera el story map con el corte del release v0.1.0 (Figura 4.1).

Uso (desde la raíz del repositorio):
    python docs/04-requisitos/story-map.py

Escribe docs/documento/figuras/story-map.png. Las historias, su prioridad y su release
salen de la tabla resumen de la sección 4.5.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

SALIDA = Path(__file__).resolve().parents[1] / "documento" / "figuras" / "story-map.png"

# Actividad -> historias (ID, nombre corto, prioridad, release)
ACTIVIDADES = {
    "Agendar cita": [
        ("HU-03", "Cita en línea", "Must", "v0.1.0"),
        ("HU-04", "Confirmar citas", "Must", "v0.1.0"),
    ],
    "Recibir vehículo": [
        ("HU-01", "Recepción con fotos", "Must", "v0.1.0"),
        ("HU-07", "Alerta de bahías", "Must", "v0.1.0"),
        ("HU-25", "Operación offline", "Must", "v0.1.0"),
        ("HU-06", "Recepción con cita", "Should", "v0.1.0"),
        ("HU-05", "Buscar cliente", "Should", "Fase 2"),
    ],
    "Asignar y\ndiagnosticar": [
        ("HU-08", "Asignar bahía", "Must", "v0.1.0"),
        ("HU-09", "Diagnóstico", "Must", "v0.1.0"),
        ("HU-11", "Estatus de bahías", "Should", "Fase 2"),
    ],
    "Cotizar y\nautorizar": [
        ("HU-12", "Presupuesto", "Must", "v0.1.0"),
        ("HU-02", "Enlace de cotización", "Must", "v0.1.0"),
        ("HU-14", "Autorización 2FA", "Must", "v0.1.0"),
        ("HU-16", "Re-cotización >10 %", "Must", "v0.1.0"),
        ("HU-13", "Servicios opcionales", "Should", "v0.1.0"),
        ("HU-15", "Rechazo", "Should", "v0.1.0"),
    ],
    "Reparar y\nrefacciones": [
        ("HU-10", "Pedir refacciones", "Should", "v0.1.0"),
        ("HU-17", "Proveedores", "Should", "v0.1.0"),
        ("HU-18", "Costos de compra", "Should", "v0.1.0"),
        ("HU-19", "Stock interno", "Could", "Fase 2"),
    ],
    "Cobrar y\nentregar": [
        ("HU-21", "Bloqueo por saldo", "Must", "v0.1.0"),
        ("HU-23", "Pago y cierre", "Must", "v0.1.0"),
        ("HU-20", "Aviso de fin", "Should", "v0.1.0"),
        ("HU-22", "Crédito a flotillas", "Should", "v0.1.0"),
        ("HU-24", "Garantía 30 días", "Could", "Fase 2"),
    ],
    "Supervisar y\ntransversales": [
        ("HU-26", "Sincronización", "Must", "v0.1.0"),
        ("HU-27", "Roles y permisos", "Must", "v0.1.0"),
        ("HU-28", "Portal responsivo", "Must", "v0.1.0"),
        ("HU-30", "Aviso de privacidad", "Must", "v0.1.0"),
        ("HU-29", "Reportes", "Could", "Fase 2"),
    ],
}

COLOR = {"Must": "#cfe0f3", "Should": "#fde9c4", "Could": "#e3e3e3"}
ANCHO, ALTO, SEP_X, SEP_Y = 2.0, 0.62, 0.25, 0.18


def tarjeta(ax, x, y, color, texto, peso="normal"):
    ax.add_patch(FancyBboxPatch((x, y), ANCHO, ALTO, boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=color, ec="#555555", lw=0.8))
    ax.text(x + ANCHO / 2, y + ALTO / 2, texto, ha="center", va="center", fontsize=8, weight=peso)


def main() -> None:
    max_release = max(sum(h[3] == "v0.1.0" for h in hs) for hs in ACTIVIDADES.values())
    max_fase2 = max(sum(h[3] == "Fase 2" for h in hs) for hs in ACTIVIDADES.values())
    y_corte = -(max_release * (ALTO + SEP_Y)) - 0.15
    ancho_total = len(ACTIVIDADES) * (ANCHO + SEP_X)

    fig, ax = plt.subplots(figsize=(15, 8.2))
    for i, (actividad, historias) in enumerate(ACTIVIDADES.items()):
        x = i * (ANCHO + SEP_X)
        tarjeta(ax, x, 0.4, "#1f4e79", "", "bold")
        ax.text(x + ANCHO / 2, 0.4 + ALTO / 2, actividad, ha="center", va="center",
                fontsize=9, weight="bold", color="white")
        enRelease = [h for h in historias if h[3] == "v0.1.0"]
        fase2 = [h for h in historias if h[3] == "Fase 2"]
        for j, (hu, nombre, prioridad, _) in enumerate(enRelease):
            tarjeta(ax, x, -(j + 1) * (ALTO + SEP_Y), COLOR[prioridad], f"{hu}\n{nombre}")
        for j, (hu, nombre, prioridad, _) in enumerate(fase2):
            tarjeta(ax, x, y_corte - 0.25 - (j + 1) * (ALTO + SEP_Y), COLOR[prioridad], f"{hu}\n{nombre}")

    ax.plot([-0.2, ancho_total], [y_corte, y_corte], color="#c00000", lw=2, ls="--")
    ax.text(ancho_total - 0.1, y_corte + 0.08, "Corte del release v0.1.0", ha="right", va="bottom",
            fontsize=9, color="#c00000", weight="bold")
    ax.text(ancho_total - 0.1, y_corte - 0.08, "Fase 2", ha="right", va="top",
            fontsize=9, color="#c00000", weight="bold")

    for k, (prioridad, color) in enumerate(COLOR.items()):
        ax.add_patch(FancyBboxPatch((k * 1.6, 1.35), 0.35, 0.3, boxstyle="round,pad=0.02",
                                    fc=color, ec="#555555", lw=0.8))
        ax.text(k * 1.6 + 0.45, 1.5, prioridad, va="center", fontsize=9)

    ax.set_xlim(-0.3, ancho_total + 0.1)
    ax.set_ylim(y_corte - 0.35 - (max_fase2 + 1) * (ALTO + SEP_Y), 1.8)
    ax.axis("off")
    fig.tight_layout()
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(SALIDA, dpi=200)
    print("Generado:", SALIDA.name)


if __name__ == "__main__":
    main()
