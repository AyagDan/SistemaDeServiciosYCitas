# Acuerdos de trabajo · Equipo B

Este archivo resume cómo trabajamos. La sección 2.1 del Documento de Ingeniería lo cita.

## Comunicación

- **Canal del equipo:** grupo de WhatsApp (mensajes y llamadas, para lo urgente). No se comparten ahí datos reales de clientes.
- **GitHub** (issues y Pull Requests) para todo lo técnico: requisitos, código, documentos y revisiones.
- **Tiempo máximo de respuesta:** 24 horas en días hábiles.

## Reuniones

- **Modalidad:** presencial o por llamada en el grupo de WhatsApp. Lo que se decide se registra en GitHub.
- **Daily:** breve, de lunes a viernes (qué hice, qué haré, qué me bloquea).
- **Eventos de Scrum:** Planning al inicio de cada sprint de dos semanas; Review y Retrospectiva al cierre.

## Decisiones

Se toman por consenso. Si no se logra:

- el **Product Owner** decide sobre alcance y prioridad del backlog;
- el **Scrum Master** decide sobre el proceso.

## Ramas y Pull Requests

- `main` está protegida: solo se integra mediante Pull Request.
- Hay una rama por integrante: `rama/ANGEL`, `rama/ABDIAS`, `rama/DULCE`, `rama/ALHELI` y `rama/ISIS`.
  Cada quien trabaja en la suya y la integra a `main` mediante Pull Request.
- Todo Pull Request necesita **al menos una revisión de otro integrante** antes de integrarse.
- Antes de abrir un PR, revisa que no haya datos personales reales, contraseñas ni llaves.

## Commits

- Formato **`Rol: mensaje`**, en español y en presente:
  `Developers: implementa recepción con checklist (HU-01)`, `QA Lead: agrega pruebas de cotización (CPA-10)`.
- Roles válidos: `Product Owner`, `Scrum Master`, `QA Lead`, `Developers`.
- Con referencia a la historia, el caso de prueba o la sección del documento cuando aplique.

## Documentos

- El Documento de Ingeniería está en LaTeX en `docs/documento/`, **un archivo por sección** en
  `docs/documento/secciones/`. Cada rol edita sus secciones y git fusiona los cambios. El `.docx` solo se genera
  para la entrega (`python docs/documento/generar-docx.py`).
- Compila con `pdflatex -interaction=nonstopmode IS1-Fase1-EquipoB.tex` (dos veces) y revisa el `.log`
  si hay errores. El PDF entregable va en `docs/entregas/IS1-Fase1-EquipoB-v<versión>.pdf`.
- Los diagramas se guardan con su archivo fuente (PlantUML, draw.io, Mermaid o script) junto a la imagen.
- Una figura que todavía no existe se deja con `\figurapendiente{número}{título}{qué debe mostrar}{ruta}`:
  sale en rojo con su descripción hasta que alguien la reemplace por `\figura{...}`.

## Datos personales

Solo datos ficticios en desarrollo, pruebas y demostraciones (LFPDPPP). Nunca se suben correos, teléfonos
ni datos reales de clientes o del equipo al repositorio.

## Incumplimiento

Se registra en la retrospectiva. A la segunda falta en el mismo sprint, el Scrum Master lo informa al profesor.
