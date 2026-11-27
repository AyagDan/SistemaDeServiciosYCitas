# S8-T8 · Evidencia del proceso

Tarea de equipo S8-T8 de la guía de la semana 8. Reúne en un solo lugar lo que el repositorio muestra del
proceso y lo que todavía no.

## 1. Resumen de sprints

| Sprint | Fechas | Objetivo | ¿Se cumplió? | Puntos comprometidos | Puntos terminados | Retrospectiva en una línea |
| --- | --- | --- | --- | --- | --- | --- |
| S0 | 14/10/2026 a 29/10/2026 | Conocer al cliente, levantar requisitos y preparar el repositorio | Sí | — | — | Minuta `2026-10-29-retrospectiva-sprint-0.md` (PR #88) |
| S1 | 30/10/2026 a 10/11/2026 | SRS en borrador para validarlo en la Review 1 | Sí | 0 | 0 | Minuta `2026-11-10-retrospectiva-sprint-1.md` (PR #88) |
| S2 | Después del 10/11/2026 (inicio por registrar) | Correcciones de la Review 1 y primeras historias del flujo núcleo | En curso | Por registrar | Por registrar | Al cierre del sprint |

Las fechas de S0 y S1 vienen del PR #88, que todavía no se integra. La velocidad se empieza a medir con el S2.

## 2. Historias enlazadas a issues

Las 30 historias del backlog ya tienen su issue, y la sección 4.5 del documento cita el número.

| Historias | Issues |
| --- | --- |
| HU-01 a HU-10 | #31 a #40 |
| HU-11 a HU-20 | #41 a #50 |
| HU-21 a HU-30 | #51 a #60 |

Cada issue tiene la etiqueta `historia de usuario` y su prioridad (`Must`, `Should` o `Could`). Ninguno tiene
asignado ni estimación en el tablero; eso se completa en la planeación del sprint.

## 3. Ramas

Revisado el 24/11/2026 en `AyagDan/SistemaDeServiciosYCitas`:

| Rama | Issue | Sigue `tipo/número-descripción` |
| --- | --- | --- |
| `docs/85-minutas-reuniones` | #85 | Sí |
| `docs/87-registros-internos` | #87 | Sí |
| `docs/91-checklist-entrega` | #91 | Sí |
| `docs/94-criterios-aceptacion-verificables` | #94 | Sí |
| `feat/89-campos-contingencia` | #89 | Sí |

A estas se suman las ramas de las tareas de `Tareas_Equipo`, una por tarea y con el mismo formato. Ya no quedan ramas por rol ni por integrante (B5, issue #10). Las ramas integradas se borran después de cada merge.

## 4. Protección de `main` y revisiones

| Punto | Estado |
| --- | --- |
| `main` protegida | **No.** La API de GitHub responde «Branch not protected» |
| Repositorio público | Sí, así que GitHub Free sí permite proteger la rama |
| PR con revisión aprobada | Ninguno tiene revisiones registradas |

El `CONTRIBUTING.md` dice que `main` está protegida y que todo PR necesita al menos una revisión de otro
integrante. Hoy el repositorio no lo cumple. Activar la protección es una decisión del equipo, porque desde ese
momento ningún PR se puede integrar sin que alguien lo apruebe.
