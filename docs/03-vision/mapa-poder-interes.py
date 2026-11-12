"""Genera el mapa de poder/interés de los stakeholders (Figura 3.1).

Uso (desde la raíz del repositorio):
    python docs/03-vision/mapa-poder-interes.py

Escribe docs/documento/figuras/mapa-poder-interes.png. Los datos salen de la tabla 3.4.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SALIDA = Path(__file__).resolve().parents[1] / "documento" / "figuras" / "mapa-poder-interes.png"

# (nombre, interés 0-10, poder 0-10) según la clasificación de la tabla 3.4
STAKEHOLDERS = [
    ("Dueños del taller", 8.6, 9.2),
    ("Gerente", 8.0, 8.2),
    ("Jefe de mecánicos", 8.8, 6.7),
    ("Recepcionista", 9.0, 3.9),
    ("Mecánicos de bahía\ny de apoyo", 6.4, 1.7),
    ("Encargado de almacén", 7.6, 2.9),
    ("Clientes particulares", 8.9, 1.2),
    ("Clientes de flotillas", 5.0, 5.0),
]

CUADRANTES = [
    (2.5, 9.6, "Mantener satisfechos"),
    (7.5, 9.6, "Gestionar de cerca"),
    (2.5, 0.4, "Monitorear"),
    (7.5, 0.4, "Mantener informados"),
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(8.5, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axvline(5, color="#888888", lw=1)
    ax.axhline(5, color="#888888", lw=1)
    ax.fill_between([5, 10], 5, 10, color="#dbe7f5")
    ax.fill_between([5, 10], 0, 5, color="#e8f2e3")
    ax.fill_between([0, 5], 5, 10, color="#fbf0d9")
    for x, y, texto in CUADRANTES:
        ax.text(x, y, texto, ha="center", va="center", fontsize=11, weight="bold", color="#444444")
    for nombre, interes, poder in STAKEHOLDERS:
        ax.plot(interes, poder, "o", color="#1f4e79", ms=8)
        ax.annotate(nombre, (interes, poder), xytext=(-8, 0), textcoords="offset points",
                    ha="right", va="center", fontsize=9)
    ax.set_xlabel("Interés en el sistema", fontsize=11)
    ax.set_ylabel("Poder sobre el proyecto", fontsize=11)
    ax.set_xticks([0, 5, 10], ["Bajo", "Medio", "Alto"])
    ax.set_yticks([0, 5, 10], ["Bajo", "Medio", "Alto"])
    fig.tight_layout()
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(SALIDA, dpi=200)
    print("Generado:", SALIDA.name)


if __name__ == "__main__":
    main()
