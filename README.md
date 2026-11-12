# Sistema de Órdenes de Servicio y Citas

Proyecto de Ingeniería de Software I (IDSSI-27) · Universidad del Istmo, Campus Ixtepec · Equipo B.

Cliente: Servicio Automotriz Hermanos Ruiz, S.A. de C.V. El sistema digitalizará el ciclo de atención del
taller: citas, recepción del vehículo con checklist y fotografías, diagnóstico y asignación de bahía,
cotización con autorización del cliente por código de verificación, refacciones, cobro y entrega.

## Equipo

| Integrante | Rol |
|---|---|
| Ángel Yael Avendaño Guzmán | Product Owner |
| Abdías Daniel Chávez Cruz | Scrum Master / Tech Lead |
| Dulce María Estudillo Rosado | QA Lead |
| Isis Alhelí González Maldonado | Developer |
| Isis Yamilet Meléndez Hernández | Developer |

Cada historia o tarea se trabaja en su propia rama `tipo/número-descripción` (GitHub Flow); ver
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Entregas del Documento de Ingeniería

| Corte | Versión | Secciones | Archivos |
|---|---|---|---|
| Review 0 | v0.1 | Portada, 1, 2.1–2.4, 3 | `docs/entregas/IS1-Fase1-EquipoB-v0.1.docx` (versión en Word, antes de migrar a LaTeX) |
| Review 1 | v0.2 | + 4.1–4.5 (borrador), 4.6, 4.7 | Se genera desde `docs/documento/` en `docs/entregas/IS1-Fase1-EquipoB-v0.2.pdf` y `.docx` |

Cada corrección aumenta en uno el tercer dígito de la versión y tiene una etiqueta de Git con ese nombre.
Versión vigente: **v0.2.3**.

| Versión | Corrección de la Review 1 | Issue | PR |
|---|---|---|---|
| v0.2.1 | B11 · Versión y stakeholders | #9 | #15 |
| v0.2.2 | B5 · Una rama por historia o tarea | #10 | #16 |
| v0.2.3 | B3 · Guion y minuta de la entrevista | #20 | #21 |

## Contenido del repositorio

| Ruta | Contenido |
|---|---|
| `docs/documento/` | Documento de Ingeniería en LaTeX, un archivo por sección en `secciones/` |
| `docs/entregas/` | Cada entrega en PDF y Word (`IS1-Fase1-EquipoB-v<versión>`) |
| `docs/03-vision/` | Fuentes de las figuras de la sección 3 (proceso actual y mapa de poder/interés) |
| `docs/04-requisitos/` | Fuente del story map de la sección 4.5 |
| `informacion/` | Material de referencia del curso: machote del documento, observaciones de la Review 1 y su plan de atención, reglas de negocio y de datos, propuesta de solución (resumen en `contexto.md` y original en Word) e indicaciones de clase |
| `docs/minutas/` | Minutas de las Sprint Reviews |
| `CONTRIBUTING.md` | Acuerdos de trabajo del equipo |

Las historias de usuario (HU-01 a HU-30) están registradas como issues del repositorio (#31 a #60),
con las etiquetas `historia de usuario` y su prioridad (`Must`, `Should` o `Could`).

## Compilar el documento

```bash
cd docs/documento
pdflatex -interaction=nonstopmode IS1-Fase1-EquipoB.tex   # dos veces, por el índice
cd ../..
python docs/documento/generar-docx.py                     # versión Word (requiere pandoc o pypandoc-binary)
```

Las figuras generadas se regeneran con `python docs/03-vision/mapa-poder-interes.py` y
`python docs/04-requisitos/story-map.py` (requieren matplotlib). El diagrama del proceso actual está en
PlantUML (`docs/03-vision/proceso-as-is.puml`).
