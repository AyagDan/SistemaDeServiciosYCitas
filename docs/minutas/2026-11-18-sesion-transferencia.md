# Minuta · Sesión interna de transferencia de conocimiento

| Dato | Valor |
|---|---|
| Observación que atiende | B6 de la Review 1, segunda parte (issue #30) |
| Objetivo | Que todo el equipo pueda explicar el trabajo hecho con ayuda de IA, que concentró un solo integrante |
| Expone | Tech Lead (Abdías Daniel Chávez Cruz) |
| Fecha límite | Miércoles 18 de noviembre de 2026 |
| Fecha | Miércoles 18 de noviembre de 2026 |
| Hora | 10:00 a 12:00 |
| Modalidad | Presencial, en la universidad |
| Temas expuestos | Estructura del backend, reglas de negocio implementadas y pruebas (1.1, 1.4 y 1.5) |
| Asistentes | Ángel Yael Avendaño Guzmán, Abdías Daniel Chávez Cruz, Dulce María Estudillo Rosado, Isis Alhelí González Maldonado, Isis Yamilet Meléndez Hernández |

En la Review cualquier integrante puede ser preguntado sobre cualquier parte del documento o del
repositorio. Por eso cada tema termina con preguntas de comprobación que responde alguien distinto de quien
expone.

## 1. Temas de la sesión

### 1.1 Estructura del repositorio

| Ruta | Qué contiene |
|---|---|
| `docs/documento/` | Documento de Ingeniería en LaTeX: `IS1-Fase1-EquipoB.tex` (portada, control de versiones), `preambulo.tex` y un archivo por sección en `secciones/` |
| `docs/documento/generar-docx.py` | Genera la versión Word del documento con pandoc |
| `docs/03-vision/`, `docs/04-requisitos/` | Fuentes de las figuras (PlantUML y scripts de Python) y la propuesta de alcance del Release v0.1.0 |
| `docs/minutas/` | Minutas de las Reviews y de esta sesión |
| `docs/entregas/` | Entregas en PDF y Word con el nombre del machote |
| `informacion/` | Machote, observaciones de la Review 1, reglas de negocio y de datos, propuesta de solución |

Preguntas de comprobación:

- ¿En qué archivo se cambia la versión del documento y dónde aparece después?
- ¿Cómo se compila el PDF y qué se revisa si falla?

### 1.2 Flujo de trabajo en GitHub

- GitHub Flow: una rama por historia o tarea con la convención `tipo/número-descripción`, creada desde `main`.
- Cada cambio entra a `main` con un Pull Request que cierra su issue; la rama se borra al integrarse.
- Commits en español, en presente, con el formato `Rol: mensaje`.
- Cada corrección aumenta en uno el tercer dígito de la versión (v0.2.1, v0.2.2…) y se registra en la
  portada, el control de versiones, el Anexo F, el README y una etiqueta de Git.

Preguntas de comprobación:

- ¿Cómo se llamaría la rama para atender la historia HU-12?
- ¿Qué versión le toca a la siguiente corrección y en qué lugares se registra?

### 1.3 Correcciones de la Review 1 ya integradas

| Versión | Corrección | Qué se cambió |
|---|---|---|
| v0.2.1 | B11 | Versión según el machote; se retiraron de 3.4 los que no son stakeholders del producto |
| v0.2.2 | B5 | Una rama por historia o tarea (CONTRIBUTING.md, README y 2.1) |
| v0.2.3 | B3 | Guion y minuta de la entrevista (Anexo A); cada regla de 4.7 cita su hallazgo E-01 a E-11 |
| v0.2.4 | B4 | Historias como issues #31 a #60; puntos y minuta de la Review 1 (2.3); evidencia por integrante (12.2) |
| v0.2.5 | B2 (propuesta) | Release v0.1.0 reducido a 11 historias (40 puntos) del flujo núcleo |
| v0.2.6 | B6 (declaración) | Sección 2.6 con el uso de IA, cómo se verificó y quién responde |

Preguntas de comprobación:

- ¿Qué historias quedan en el Release v0.1.0 según la propuesta, y por qué la operación sin conexión pasa a
  la Fase 2?
- ¿De dónde sale cada fila de la declaración de IA y quién responde por ella?

### 1.4 Reglas de negocio implementadas en el SRS (4.7)

Las reglas RN-01 a RN-15 de la sección 4.7 indican su fuente (anteproyecto o hallazgo de la entrevista) y el
requisito que las implementa. Se repasan las que más afectan al flujo núcleo:

- RN-02: doble verificación con código de 6 dígitos al autorizar una cotización.
- RN-03: el cliente aprueba o rechaza por separado los conceptos opcionales.
- RN-04: re-cotización obligatoria si el sobrecosto supera el 10%.
- RN-05: 4 bahías y 5 lugares de espera.
- RN-08: las citas en línea no apartan lugar hasta que la recepcionista las confirma.
- RN-10: no se entrega un vehículo con saldo pendiente, salvo crédito a flotillas autorizado por el gerente.
- RN-11: la cotización vale 5 días naturales.

Preguntas de comprobación:

- ¿Qué pasa si una cotización autorizada sube exactamente 10%? ¿Y si sube 10.06%?
- ¿Qué hallazgo de la minuta respalda RN-08?

### 1.5 Pruebas

- La Definición de Terminado (2.2) exige pruebas automatizadas y la integración continua en verde para cada
  historia.
- El backend FastAPI (`backend/app/`) separa rutas, servicios y modelos; sus 42 pruebas automatizadas
  (`backend/tests/`) se ejecutan con `python -m pytest` y cubren acceso, recepción, cotización, estados de
  la orden, cobro, citas y panel.
- Se explica cómo se verificó cada cambio hecho con IA: compilación del documento sin errores y comprobación
  de los datos contra GitHub y contra `informacion/`.

Preguntas de comprobación:

- ¿Qué tiene que cumplir una historia para darse por terminada?
- ¿Cómo se comprobó que la declaración de IA y la evidencia de 12.2 son correctas?

## 2. Desarrollo de la sesión

Pendiente: se registra al realizar la sesión.

| Tema | Quién respondió las preguntas de comprobación | Dudas que surgieron | Resuelta (sí / no) |
|---|---|---|---|
| 1.1 Estructura del repositorio | Pendiente | Pendiente | Pendiente |
| 1.2 Flujo de trabajo en GitHub | Pendiente | Pendiente | Pendiente |
| 1.3 Correcciones integradas | Pendiente | Pendiente | Pendiente |
| 1.4 Reglas de negocio | Pendiente | Pendiente | Pendiente |
| 1.5 Pruebas | Pendiente | Pendiente | Pendiente |

## 3. Acuerdos

| # | Acuerdo | Responsable | Fecha |
|---|---|---|---|
| 1 | Cada autor declara en 2.6 si usó IA en el contenido original de las secciones 1 a 4 y cómo verificó el resultado, para eliminar la fila «Pendiente». | Cada integrante | 25/11/2026 |
| 2 | Registrar en la tabla de la sección 2 quién respondió cada pregunta de comprobación y las dudas que surgieron. | Cada integrante | 25/11/2026 |
| 3 | Las Developers y la QA Lead hacen los commits de contenido de su área; el Scrum Master se queda con issues, coordinación y versiones. | Scrum Master | 18/11/2026 |
