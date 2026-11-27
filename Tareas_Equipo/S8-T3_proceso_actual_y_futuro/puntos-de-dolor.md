# S8-T3 · Proceso actual, proceso futuro y puntos de dolor

| Diagrama | Archivo | Qué muestra |
| --- | --- | --- |
| Proceso actual (as-is) | `docs/03-vision/proceso-as-is.puml` (ya integrado, figura 3.2) | Cómo trabaja hoy el taller, sin el sistema, con carriles Cliente, Recepcionista, Mecánico y Registro manual |
| Proceso futuro (to-be) | `proceso-to-be.puml` (esta carpeta) | El mismo flujo con el sistema, con carriles Cliente, Recepcionista, Jefe de mecánicos y Sistema |

El proceso actual ya cumple lo que pide la guía: no menciona el sistema y usa las herramientas reales del
cliente (llamadas, WhatsApp, cuaderno y órdenes en papel). Por eso aquí solo se agrega el proceso futuro y la
tabla que une los dos.

## Puntos de dolor

| ID | Punto de dolor del proceso actual | Fuente | Paso del proceso futuro que lo resuelve | ¿Entra en v0.1.0? |
| --- | --- | --- | --- | --- |
| PD-01 | Disputas por cobros que el cliente dice no haber autorizado, porque las autorizaciones son verbales o por mensaje | Minuta A.2, problemas expresados por el cliente; E-01 | El cliente aprueba en el enlace con un código de 6 dígitos y el sistema guarda la autorización (HU-02, HU-14) | Sí |
| PD-02 | Reclamos por daños, porque no hay checklist ni fotografías del estado de llegada | Minuta A.2, problemas expresados por el cliente; as-is, nota de la recepción | La recepción exige checklist completo y 4 fotografías antes de abrir la orden (HU-01, RN-12) | Sí |
| PD-03 | Muchas llamadas para preguntar por el avance, que interrumpen a la recepcionista | Minuta A.2, problemas expresados por el cliente; as-is, nota de la reparación | El cliente consulta el estado en el enlace de seguimiento (HU-28, RF-02.1) | Sí. El aviso automático de trabajo terminado (HU-20) pasa a la Fase 2 |
| PD-04 | Bahías y carga de trabajo asignadas de palabra, con vehículos detenidos sin justificación | Minuta A.2, problemas expresados por el cliente; E-04, E-05 | El jefe de mecánicos asigna bahía y responsable en el sistema y ve la alerta de bahías ocupadas (HU-07, HU-08) | Sí. La vista de estatus de bahías (HU-11) es de la Fase 2 |
| PD-05 | Historial de reparaciones y garantías archivado en carpetas, difícil de consultar | Minuta A.2, problemas expresados por el cliente; as-is, nota del archivo | El historial queda en el sistema con cada orden (RF-03.2, HU-23, HU-24) | No: la propuesta lo pasa a la Fase 2 |
| PD-06 | Citas anotadas en cuaderno, con riesgo de errores u omisiones | As-is, nota de la solicitud de cita | Solicitud de cita en línea y confirmación manual (HU-03, HU-04) | No: la propuesta lo pasa a la Fase 2 |
| PD-07 | Cotización armada a mano, con demoras y errores en los costos | As-is, nota de la cotización | El sistema genera la cotización desglosada con vigencia de 5 días (HU-12) | Sí |

PD-05 y PD-06 quedan fuera del to-be del Release v0.1.0 porque así lo propone el corte del release. Si el
cliente no acepta la propuesta, se agregan al diagrama.

## Qué falta

- Validar con el cliente que reconoce el proceso futuro como «así queremos trabajar».
- Exportar la imagen del to-be y agregarla al documento como figura de la sección 6.6.
