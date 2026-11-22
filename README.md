# Sistema de Órdenes de Servicio y Citas

Proyecto de Ingeniería de Software I (IDSSI-27) · Universidad del Istmo, Campus Ixtepec · Equipo B.

Cliente: Servicio Automotriz Hermanos Ruiz, S.A. de C.V. El sistema digitalizará el ciclo de atención del
taller: citas, recepción del vehículo con checklist y fotografías, diagnóstico y asignación de bahía,
cotización con autorización del cliente por código de verificación, refacciones, cobro y entrega.

## Datos del proyecto

| Dato | Valor |
|---|---|
| Universidad | Universidad del Istmo · Campus Ixtepec |
| Carrera | Ingeniería en Desarrollo de Software y Sistemas Inteligentes |
| Materia | Ingeniería de Software I (IDSSI-27) |
| Semestre y grupo | Quinto semestre · grupo 517 |
| Profesor(a) | Florentino Ruiz Aquino |
| Equipo | B (5 integrantes) |
| Cliente | Servicio Automotriz Hermanos Ruiz, S.A. de C.V. |
| Entrega | Review 1 corregida · versión **v0.2.10** · 18/11/2026 |

## Problema que resuelve

Hoy las citas se apuntan en un cuaderno, las órdenes se llenan en papel y la comunicación con el cliente es por
teléfono o WhatsApp. Eso provoca disputas por cobros que el cliente dice no haber autorizado, reclamos por daños
sin evidencia del estado en que llegó el vehículo, muchas llamadas para preguntar por el avance y poca
visibilidad de qué vehículo ocupa cada una de las 4 bahías del taller.

## Objetivos

**Objetivo general:** digitalizar el ciclo de atención del taller (cita, recepción, diagnóstico, cotización y
autorización, cobro y entrega) para que cada paso quede registrado y consultable.

**Objetivos específicos** (con el indicador de la sección 3.2 del documento):

1. Eliminar las disputas por cobros no autorizados: el 100 % de las órdenes cerradas con la autorización digital
   registrada (fecha, hora, IP y monto).
2. Reducir las llamadas de seguimiento a recepción: al menos 50 % menos que la medición inicial.
3. Contar con evidencia del estado del vehículo al recibirlo: el 100 % de las recepciones con el checklist
   completo y las 4 fotografías obligatorias.

## Integrantes

| Integrante | Matrícula | GitHub | Rol |
|---|---|---|---|
| Ángel Yael Avendaño Guzmán | 0224170023 | AyagDan | Product Owner |
| Abdías Daniel Chávez Cruz | 0224170024 | AbdiasChavez | Scrum Master / Tech Lead |
| Dulce María Estudillo Rosado | 0224170028 | DulceRosado | QA Lead / Developer |
| Isis Alhelí González Maldonado | 0224170030 | IsisAlheliGonzalezMaldonado | Developer |
| Isis Yamilet Meléndez Hernández | 0224170037 | IsisMelendezHernandez | Developer |

Cada historia o tarea se trabaja en su propia rama `tipo/número-descripción` (GitHub Flow); ver
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Tecnologías

| Componente | Tecnología y versión |
|---|---|
| Lenguaje | Python 3.12 o superior (probado con 3.13) |
| API REST | FastAPI 0.164.0 y Uvicorn 0.54.0 |
| Acceso a datos | SQLAlchemy 2.0.58 |
| Validación | Pydantic 2.14.3 y python-multipart 0.0.34 |
| Base de datos | SQLite (desarrollo y pruebas) y PostgreSQL 14 o superior (esquema en `db/schema.sql`) con psycopg 3.3.9 |
| Pruebas | pytest 9.2.0 y httpx 0.28.1 |
| Documento | LaTeX (`pdflatex`), PlantUML y matplotlib para las figuras |

Las versiones del backend están fijadas en `backend/requirements.txt`.

## Requisitos previos

- Python 3.12 o superior y Git.
- Opcional: PostgreSQL 14 o superior, si no se usa SQLite.
- Para compilar el documento: una distribución de LaTeX (MiKTeX o TeX Live) con `pdflatex`.
- Para regenerar los diagramas: Java y el `.jar` de PlantUML, y matplotlib para los scripts de Python.

## Instalación y ejecución

```bash
git clone https://github.com/AyagDan/SistemaDeServiciosYCitas.git
cd SistemaDeServiciosYCitas/backend
python -m venv .venv
.venv\Scripts\activate            # Windows  (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env            # Linux/macOS: cp .env.example .env
python -m app.semilla --demo      # 4 bahías, un usuario por rol y clientes FICTICIOS
uvicorn app.main:app --reload     # documentación interactiva en http://localhost:8000/docs
```

Todo valor de `.env` es opcional: sin cambios la API usa SQLite local y genera una `SECRET_KEY` al arrancar (las
sesiones se invalidan al reiniciar). Para fijar la contraseña de los usuarios de demostración, define
`SEED_PASSWORD` en `.env`; si no, se genera una y se imprime una sola vez. El archivo `.env` nunca se sube.

Para usar PostgreSQL:

```bash
createdb taller
psql -d taller -f db/schema.sql
```

y en `backend/.env`: `DATABASE_URL=postgresql+psycopg://USUARIO:CONTRASENA@localhost:5432/taller`.

## Uso

Con los datos de demostración, los usuarios son `gerente@`, `recepcion@`, `jefe@` y `almacen@taller.test`, todos
con la contraseña de `SEED_PASSWORD`. Ejemplo con la API en marcha:

```bash
curl -X POST http://localhost:8000/auth/login -H "Content-Type: application/json" -d '{"correo": "gerente@taller.test", "contrasena": "<SEED_PASSWORD>"}'
curl http://localhost:8000/panel -H "Authorization: Bearer <token>"
```

Cada endpoint indica en `/docs` qué rol puede usarlo. Todos los datos de prueba y demostración son ficticios.

## Prototipos y diagramas

El sistema todavía no tiene interfaz gráfica: el backend se usa desde la documentación interactiva `/docs`.
Estos son los prototipos de baja fidelidad de las pantallas del flujo núcleo (Figuras 4.5 a 4.10 del documento).
Las capturas de pantalla del sistema en funcionamiento: Pendiente, hasta que exista la interfaz.

| Recepción del vehículo (W-01) | Tableta del jefe de mecánicos (W-02) |
|---|---|
| ![W-01](docs/documento/figuras/wireframe-w01.png) | ![W-02](docs/documento/figuras/wireframe-w02.png) |

| Cotización (W-03) | Portal del cliente (W-04) |
|---|---|
| ![W-03](docs/documento/figuras/wireframe-w03.png) | ![W-04](docs/documento/figuras/wireframe-w04.png) |

| Agenda de citas (W-05) | Órdenes, cobro y entrega (W-06) |
|---|---|
| ![W-05](docs/documento/figuras/wireframe-w05.png) | ![W-06](docs/documento/figuras/wireframe-w06.png) |

Diagramas del documento, en `docs/documento/figuras/`: casos de uso (`casos-de-uso-1.png` a `-3.png`), máquina de
estados de la orden (`maquina-estados-orden.png`), story map y proceso actual. Sus fuentes están en
`docs/03-vision/`, `docs/04-requisitos/` y `docs/06-analisis/`.

Diagrama de clases del dominio, generado a partir de `backend/app/models.py` con
`docs/06-analisis/clases/generar_clases.py`:

- [`clases-1-operacion.png`](docs/06-analisis/clases/clases-1-operacion.png): clientes, citas, recepción y orden de servicio.
- [`clases-2-cotizacion-cobro.png`](docs/06-analisis/clases/clases-2-cotizacion-cobro.png): cotización, autorización, cobro y garantía.

Mapa de tecnologías y cómo se comunican:

![Mapa de tecnologías](docs/07-arquitectura/tecnologias/diagrama-tecnologias.png)

## Pruebas

```bash
cd backend
python -m pytest              # 42 pruebas
```

La evidencia de la última ejecución está en [`docs/pruebas/resultado-pruebas.txt`](docs/pruebas/resultado-pruebas.txt).

## Entregas del Documento de Ingeniería

| Corte | Versión | Secciones | Archivos |
|---|---|---|---|
| Review 0 | v0.1 | Portada, 1, 2.1–2.4, 3 | `docs/entregas/IS1-Fase1-EquipoB-v0.1.docx` (versión en Word, antes de migrar a LaTeX) |
| Review 1 (corregida) | v0.2.10 | + 4.1–4.7, 6.5 y 13 | `docs/entregas/IS1-Fase1-EquipoB-v0.2.10.pdf` |

Cada corrección aumenta en uno el tercer dígito de la versión y tiene una etiqueta de Git con ese nombre.
Versión vigente: **v0.2.19**.

| Versión | Corrección de la Review 1 | Issue | PR |
|---|---|---|---|
| v0.2.1 | B11 · Versión y stakeholders | #9 | #15 |
| v0.2.2 | B5 · Una rama por historia o tarea | #10 | #16 |
| v0.2.3 | B3 · Guion y minuta de la entrevista | #20 | #21 |
| v0.2.4 | B4 · Evidencia del proceso | #28 | #61 |
| v0.2.5 | B2 · Propuesta de alcance del Release v0.1.0 (primera parte) | #29 | #62 |
| v0.2.6 | B6 · Declaración de uso de IA (primera parte) | #30 | #63 |
| v0.2.7 | B6 · Sesión interna de transferencia (segunda parte) | #30 | #76 |
| v0.2.8 | B1 · Diagramas de casos de uso y wireframes | #67 | #77 |
| v0.2.9 | B6 · Declaración de uso de IA (complemento) | #30 | #77 |
| v0.2.10 | B7 · Máquina de estados de la Orden | #68 | #77 |
| v0.2.11 | B2 · Guion de la sesión con el cliente (segunda parte) | #29 | #82 |
| v0.2.12 | B10 · Procedimientos de contingencia en la sesión con el cliente | #81 | #82 |
| v0.2.13 | B8 · Reclasificación y complemento de los RNF | #83 | #84 |
| v0.2.14 | B10 · Aceptación del cliente de los procedimientos de contingencia | #81 | #86 |
| v0.2.15 | B3 · Minuta de la entrevista con la transcripción y registro de reuniones | #85 | #86 |
| v0.2.16 | B4 · Fechas de sprints, retrospectivas, minutas internas y aportes (seguimiento) | #87 | #88 |
| v0.2.17 | B1 · Validación de la QA Lead (seguimiento) | #87 | #88 |
| v0.2.18 | B6 · Declaración de IA de cada integrante y minuta de la sesión interna (tercera parte) | #30 | #88 |
| v0.2.19 | B10 · Campos del modelo y formatos de la Bitácora de Contingencia (implementación) | #81 | #88 |

## Contenido del repositorio

| Ruta | Contenido |
|---|---|
| `docs/documento/` | Documento de Ingeniería en LaTeX, un archivo por sección en `secciones/` |
| `docs/entregas/` | Cada entrega en PDF y Word (`IS1-Fase1-EquipoB-v<versión>`) |
| `docs/03-vision/` | Fuentes de las figuras de la sección 3 (proceso actual y mapa de poder/interés) |
| `docs/04-requisitos/` | Fuentes del story map, los diagramas de casos de uso y los wireframes (4.5 y 4.10), y la propuesta de alcance |
| `docs/06-analisis/` | Máquina de estados de la Orden (6.5) y diagrama de clases del dominio, con sus fuentes |
| `docs/07-arquitectura/` | Mapa de tecnologías, su generador y los íconos que usa |
| `backend/` | Backend FastAPI y sus pruebas automatizadas (`backend/tests/`) |
| `db/` | Esquema de PostgreSQL (`schema.sql`) |
| `docs/pruebas/` | Evidencia de la ejecución de las pruebas automatizadas |
| `informacion/` | Material de referencia del curso: machote del documento, observaciones de la Review 1 y su plan de atención, reglas de negocio y de datos, propuesta de solución (resumen en `contexto.md` y original en Word) e indicaciones de clase |
| `docs/minutas/` | Minutas de las reuniones con el cliente, del equipo y de las Sprint Reviews, con su cronología (`README.md`) |
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
