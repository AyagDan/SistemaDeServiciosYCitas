# Sistema de Órdenes de Servicio y Citas

Proyecto de Ingeniería de Software I (IDSSI-27) · Universidad del Istmo, Campus Ixtepec · Equipo B.

Cliente: Servicio Automotriz Hermanos Ruiz, S.A. de C.V. El sistema digitalizará el ciclo de atención del
taller: citas, recepción del vehículo con checklist y fotografías, diagnóstico y asignación de bahía,
cotización con autorización del cliente por código de verificación, refacciones, cobro y entrega.

## Equipo

| Integrante | Rol | Rama |
|---|---|---|
| Ángel Yael Avendaño Guzmán | Product Owner | `rama/ANGEL` |
| Abdías Daniel Chávez Cruz | Scrum Master / Tech Lead | `rama/ABDIAS` |
| Dulce María Estudillo Rosado | QA Lead | `rama/DULCE` |
| Isis Alhelí González Maldonado | Developer | `rama/ALHELI` |
| Isis Yamilet Meléndez Hernández | Developer | `rama/ISIS` |

## Entregas del Documento de Ingeniería

| Corte | Versión | Secciones | Archivos |
|---|---|---|---|
| Review 0 | v0.1 | Portada, 1, 2.1–2.4, 3 | `IS1_Fase1_EquipoB_Documento_Ingenieria-v0.1.docx` (versión en Word, antes de migrar a LaTeX) |
| Review 1 | v0.2 | + 4.1–4.5 (borrador), 4.6, 4.7 | Se genera desde `docs/documento/` en `docs/entregas/IS1-Fase1-EquipoB-v0.2.pdf` y `.docx` |

## Contenido del repositorio

| Ruta | Contenido |
|---|---|
| `docs/documento/` | Documento de Ingeniería en LaTeX, un archivo por sección en `secciones/` |
| `docs/entregas/` | Cada entrega en PDF y Word (`IS1-Fase1-EquipoB-v<versión>`) |
| `docs/03-vision/` | Fuentes de las figuras de la sección 3 (proceso actual y mapa de poder/interés) |
| `docs/04-requisitos/` | Fuente del story map de la sección 4.5 |
| `CONTRIBUTING.md` | Acuerdos de trabajo del equipo |

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
