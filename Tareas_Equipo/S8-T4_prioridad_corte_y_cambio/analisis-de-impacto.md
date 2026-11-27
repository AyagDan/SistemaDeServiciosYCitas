# S8-T4 · Análisis de impacto de las solicitudes de cambio del cliente

La guía pide responder la solicitud de cambio del cliente con la plantilla de la sección 5. El cliente planteó
dos cambios en la sesión del 23/10/2026 (minuta `docs/minutas/2026-10-23-sesion-cliente-propuestas.md`, que
agrega el PR #86). Los dos ya se resolvieron y el cliente aceptó las soluciones el 09/11/2026, pero nunca se
documentó su análisis de impacto. Aquí queda.

Si el profesor manda otra solicitud de cambio en este sprint, se analiza con la misma plantilla en un archivo
nuevo de esta carpeta.

---

## Cambio D-1 · Cortes de luz de más de un par de horas

| Campo | Contenido |
| --- | --- |
| Solicitud | «Qué pasa cuando los cortes de luz duran más de un par de horas.» |
| Motivo | Los cortes de luz e internet son frecuentes (E-10) y la operación sin conexión de HU-25 depende de la batería de los equipos |
| Elementos afectados | RN-15 (nueva), sección 4.7.1 parte B, RNF-08, RNF-09, HU-25, HU-26, RF-04, RF-06, RF-10, bitácora de contingencia impresa, riesgo R-02 |
| Esfuerzo | Sin puntos nuevos en v0.1.0: es un procedimiento en papel. La captura posterior de lo registrado en papel se suma a HU-26 cuando se construya |
| Riesgo | Baja el riesgo R-02: si la operación sin conexión no está lista, el taller no se detiene |
| Opciones | **A.** Seguir en la PWA con batería y pasar a papel si el corte supera 4 horas o la batería baja del 20 %; capturar en 24 horas. **B.** Registrar en una hoja de cálculo durante el corte. **C.** No cubrir el caso y suspender la recepción durante el corte |
| Recomendación del equipo | A: no depende de tener luz y deja evidencia firmada por el cliente. B se descartó porque también necesita luz (minuta del 24/10/2026) |
| Decisión del cliente | Opción A aceptada el 09/11/2026 (`docs/minutas/2026-11-09-sesion-cliente-soluciones.md`). Faltan por confirmar los umbrales de 4 horas y 24 horas |

## Cambio D-2 · Precisión del nivel de gasolina al recibir el vehículo

| Campo | Contenido |
| --- | --- |
| Solicitud | «Cómo se asegura que el nivel de gasolina del vehículo sea preciso al momento de entrar a servicio.» |
| Motivo | Evitar reclamos por diferencias de combustible cuando el medidor del tablero no funciona |
| Elementos afectados | RN-14 (nueva), sección 4.7.1 parte A, RF-04, HU-01, CU-02 (extensión 3a), selector de combustible de la recepción, tabla `recepcion_vehicular` |
| Esfuerzo | No se estimó por separado; entra en HU-01 (3 puntos): opción «No verificable» con método, valor y fotografía del tablero. Los campos ya están en el PR #92. Conviene que el equipo revise si HU-01 sigue valiendo 3 puntos |
| Riesgo | Ninguno nuevo; reduce las disputas por combustible |
| Opciones | **A.** Usar el primer método disponible (escáner OBD-II, computadora de viaje, medición en litros o declaración del cliente) y marcar «No verificable». **B.** Pedir siempre la declaración del cliente. **C.** Dejar el campo vacío cuando no se pueda medir |
| Recomendación del equipo | A: deja constancia de cómo se obtuvo el dato y quién lo dio |
| Decisión del cliente | Opción A aceptada el 09/11/2026 (`docs/minutas/2026-11-09-sesion-cliente-soluciones.md`) |

## Qué sigue

1. Registrar los dos cambios como issues con la etiqueta `tipo:cambio` (ver la tarea S8-T6) y enlazar este análisis.
2. Confirmar con el cliente los umbrales de D-1 en la entrevista de seguimiento (guion de S8-T2, pregunta 3).
