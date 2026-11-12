"""Genera la versión Word (.docx) del Documento de Ingeniería con pandoc.

Uso (desde la raíz del repositorio):
    python docs/documento/generar-docx.py

Escribe docs/entregas/IS1-Fase1-EquipoB-v<versión>.docx. Requiere pandoc en el PATH
o el paquete pypandoc-binary. El PDF se sigue compilando con pdflatex.

pandoc no entiende algunos macros del preámbulo (\\ruta, \\figurapendiente, la columna L)
y descarta las celdas de tabla que solo contienen un número; por eso se trabaja sobre una
copia temporal con un preámbulo simplificado, columnas p{} y las celdas numéricas entre llaves.
"""
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

DOC = Path(__file__).resolve().parent
ENTREGAS = DOC.parent / "entregas"

PREAMBULO_PANDOC = r"""\documentclass{article}
\usepackage{graphicx,longtable,booktabs,array,calc,xcolor,soul,hyperref}
\newcommand{\ruta}[1]{\texttt{#1}}
\newcommand{\figura}[5]{%
  \begin{figure}\centering\includegraphics{#1}
  \caption{\textbf{Figura #3.} #4. Fuente: \texttt{#5}}\end{figure}}
\newcommand{\figurapendiente}[4]{%
  \begin{quote}\textcolor{red}{\textbf{Pendiente}}\par \textbf{Descripción:} #3\par
  \textbf{Archivo fuente:} \texttt{#4}\end{quote}
  \textbf{Figura #1.} #2. Fuente: \texttt{#4}\par}
\newcommand{\pendiente}{\textcolor{red}{Pendiente}}
"""

CELDA_NUMERICA = re.compile(r"(&[ \t]*)(\d[\d.,]*)(?=[ \t]*(?:&|\\\\))")
COLUMNA_L = re.compile(r"L\{([\d.]+\\linewidth)\}")  # tipo de columna propio del preámbulo


def pandoc() -> str:
    exe = shutil.which("pandoc")
    if exe:
        return exe
    import pypandoc  # pip install pypandoc-binary
    return pypandoc.get_pandoc_path()


def main() -> None:
    principal = (DOC / "IS1-Fase1-EquipoB.tex").read_text(encoding="utf8")
    version = re.search(r"\\newcommand\{\\versiondoc\}\{([^}]*)\}", principal).group(1)
    salida = ENTREGAS / f"IS1-Fase1-EquipoB-v{version}.docx"

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "secciones").mkdir()
        (tmp / "preambulo.tex").write_text(PREAMBULO_PANDOC, encoding="utf8")
        # El índice lo genera pandoc (--toc); la portada se conserva.
        (tmp / "IS1-Fase1-EquipoB.tex").write_text(
            principal.replace("\\tableofcontents", ""), encoding="utf8")
        for sec in (DOC / "secciones").glob("*.tex"):
            texto = CELDA_NUMERICA.sub(r"\1{\2}", sec.read_text(encoding="utf8"))
            texto = COLUMNA_L.sub(r"p{\1}", texto)
            (tmp / "secciones" / sec.name).write_text(texto, encoding="utf8")

        subprocess.run(
            [pandoc(), "IS1-Fase1-EquipoB.tex", "-f", "latex", "-t", "docx",
             "--toc", "--metadata", "toc-title=Índice", "--metadata", "lang=es-MX",
             f"--resource-path={DOC}", "-o", str(salida)],
            cwd=tmp, check=True)
    print("Generado:", salida.relative_to(DOC.parent.parent))


if __name__ == "__main__":
    main()
