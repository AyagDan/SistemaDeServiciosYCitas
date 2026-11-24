# S8-T6 · Gestión de incidencias en GitHub

Tarea de equipo S8-T6 de la guía de la semana 8. Responsable: QA Lead (Dulce María Estudillo Rosado).

## 1. Formularios de issue

En `ISSUE_TEMPLATE/` de esta carpeta están los dos formularios, en YAML y con campos obligatorios:

| Archivo | Para qué | Etiquetas que pone solo |
| --- | --- | --- |
| `reporte-defecto.yml` | Algo no se comporta como dice el requisito o el documento se contradice | `tipo:defecto`, `estado:triage` |
| `solicitud-cambio.yml` | El cliente pide algo nuevo; trae la plantilla de análisis de impacto | `tipo:cambio`, `estado:triage` |

GitHub solo los muestra al abrir un issue si están en `.github/ISSUE_TEMPLATE/`. Cuando el equipo los apruebe,
se copian ahí tal cual.

## 2. Etiquetas

| Etiqueta | Para qué | Estado en el repositorio |
| --- | --- | --- |
| `tipo:defecto` | Defecto en código o en el comportamiento | Creada con esta tarea |
| `tipo:defecto-doc` | Defecto en un documento o diagrama | Ya existía |
| `tipo:cambio` | Solicitud de cambio del cliente | Creada con esta tarea |
| `requisitos` | Hallazgo de la revisión cruzada sobre el SRS (P2-T5) | Creada con esta tarea |
| `sev:S1` | Bloqueante: impide usar el flujo núcleo | Creada con esta tarea |
| `sev:S2`, `sev:S3`, `sev:S4` | Alta, media y baja | Ya existían |
| `prio:P1` | Se corrige en este sprint, antes que cualquier historia nueva | Creada con esta tarea |
| `prio:P2` | En este sprint si hay capacidad, o al inicio del siguiente | Creada con esta tarea |
| `prio:P3` | Se agenda en el backlog | Creada con esta tarea |
| `estado:triage` | Nueva, falta revisarla en el triage | Creada con esta tarea |
| `origen:cliente` | Observación que viene del cliente o del profesor | Ya existía |

## 3. Tablero

El tablero de GitHub Projects necesita un campo «Estado» con los mismos estados del ciclo de vida de la guía:
Nuevo, Triage, Asignado, En progreso, En revisión, Por verificar y Cerrado. No se pudo revisar ni configurar
porque la sesión de GitHub CLI no tiene el permiso de proyectos.

## 4. Triage

Lo conduce el Product Owner con la QA Lead, al menos dos veces por sprint. Para cada issue nuevo:

1. ¿Se reproduce? Si no, se pide información o se cierra como no reproducible.
2. ¿Es duplicado? Se enlaza al original y se cierra.
3. ¿Es defecto o cambio? Si pide algo nuevo, pasa a `tipo:cambio`.
4. Se confirma la severidad y el Product Owner asigna la prioridad.
5. Se asigna a una persona. Una incidencia sin asignado no está en el sprint.

Quien corrige no cierra su propia incidencia: la cierra quien la reportó, después de verificar.

## 5. Hallazgos de la Review 1 registrados

Todos los hallazgos B1 a B11 ya están como issues con `tipo:defecto-doc`, severidad, `origen:cliente` y
responsable. Lo que les falta es la prioridad, que se decide en el primer triage.

| Hallazgo | Issue | Severidad | Responsable | Estado al 24/11/2026 | Prioridad |
| --- | --- | --- | --- | --- | --- |
| B1 Diagramas y wireframes como figuras | #67 | S2 | IsisMelendezHernandez | Cerrado | No aplica |
| B2 Reducir el release y negociarlo | #29 | S2 | AyagDan | Abierto | Por decidir en triage |
| B3 Guion y minuta de la entrevista | #20 | S3 | AyagDan | Cerrado | No aplica |
| B3 Completar la minuta y registrar reuniones | #85 | S3 | AyagDan | Abierto (PR #86) | Por decidir en triage |
| B4 Issues, fechas, puntos y minutas | #28 | S2 | AbdiasChavez | Cerrado | No aplica |
| B4 Completar registros internos | #87 | S2 | AbdiasChavez | Abierto (PR #88) | Por decidir en triage |
| B5 Una rama por historia | #10 | S3 | AbdiasChavez | Cerrado | No aplica |
| B6 Declaración de IA y sesión de transferencia | #30 | S3 | AbdiasChavez | Abierto | Por decidir en triage |
| B7 Máquina de estados de la orden | #68 | S3 | AbdiasChavez | Cerrado | No aplica |
| B8 Reclasificar los RNF | #83 | S4 | IsisAlheliGonzalezMaldonado | Cerrado | No aplica |
| B9 Criterios de aceptación verificables | #94 | S4 | IsisAlheliGonzalezMaldonado, DulceRosado | Abierto (PR #95) | Por decidir en triage |
| B10 Validar la contingencia con el cliente | #81 | S4 | AyagDan | Abierto | Por decidir en triage |
| B11 Versión y stakeholders | #9 | S4 | AbdiasChavez | Cerrado | No aplica |
