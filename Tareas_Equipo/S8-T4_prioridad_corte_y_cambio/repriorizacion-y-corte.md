# S8-T4 · Repriorización MoSCoW y corte del Release v0.1.0

Tarea de equipo S8-T4 de la guía de la semana 8. Es una propuesta para el Product Owner: la prioridad la decide
él y el corte lo acepta el cliente. Ninguna prioridad del Documento de Ingeniería ni de los issues se cambió.

## 1. Prueba del Must

Para cada historia se hizo la pregunta de la guía: si mañana nos dicen que no estará, ¿detendríamos la entrega?
Si existe cualquier forma manual de hacerlo, aunque sea incómoda, no es Must.

| Historia | Hoy | Resultado de la prueba | Justificación en una línea |
| --- | --- | --- | --- |
| HU-01 Recepción con fotografías | Must | Must | Sin evidencia de llegada vuelven los reclamos por daños, que es el dolor principal del cliente |
| HU-02 Autorización digital | Must | Must | Es el corazón del sistema: sin ella las autorizaciones siguen siendo verbales |
| HU-03 Cita en línea | Must | Should | Las citas se pueden seguir pidiendo por teléfono o WhatsApp |
| HU-04 Agenda y confirmación | Must | Should | La recepcionista puede seguir usando su agenda mientras no haya citas en línea |
| HU-05 Búsqueda rápida | Should | Should | Ya está bien clasificada |
| HU-06 Vehículo con cita previa | Should | Could | Depende de las citas en línea; sin ellas no aporta |
| HU-07 Alerta de bahías ocupadas | Must | Should | La recepcionista puede ver las bahías; la alerta ayuda pero no detiene la entrega |
| HU-08 Asignación de bahía y mecánico | Must | Must | Sin asignación no hay orden que diagnosticar ni cotizar |
| HU-09 Diagnóstico en tableta | Must | Must | La cotización sale del diagnóstico |
| HU-10 Solicitud de refacciones | Should | Should | Ya está bien clasificada |
| HU-11 Estatus de bahías | Should | Should | Ya está bien clasificada |
| HU-12 Presupuesto desglosado | Must | Must | Sin cotización no hay nada que autorizar |
| HU-13 Servicios opcionales | Should | Should | Ya está bien clasificada |
| HU-14 Firma con código 2FA | Must | Must | Es lo que vuelve defendible la autorización (RN-02) |
| HU-15 Rechazo de cotización | Should | Should | Ya está bien clasificada |
| HU-16 Re-cotización por más de 10 % | Must | Should | Mientras no esté, el taller puede pedir una nueva cotización completa; es incómodo, pero existe |
| HU-17 Proveedores | Should | Should | Ya está bien clasificada |
| HU-18 Costos y tickets | Should | Should | Ya está bien clasificada |
| HU-19 Stock interno | Could | Could | Ya está bien clasificada |
| HU-20 Aviso de trabajo terminado | Should | Should | Ya está bien clasificada |
| HU-21 Bloqueo de entrega con saldo | Must | Should | Hoy se cobra en caja antes de entregar; la regla se sigue a mano |
| HU-22 Crédito a flotillas | Should | Should | Ya está bien clasificada |
| HU-23 Pago y cierre de la orden | Must | Should | La orden se puede cerrar como hoy durante la Fase 1 (pregunta 1.2 de la minuta del 20/11) |
| HU-24 Vigencia de garantía | Could | Could | Ya está bien clasificada |
| HU-25 Operación sin conexión | Must | Should | Existe la contingencia en papel (RN-15), que el cliente aceptó el 09/11 |
| HU-26 Sincronización | Must | Should | Va con HU-25 |
| HU-27 Roles y permisos | Must | Must | Sin inicio de sesión por rol nadie puede usar el sistema |
| HU-28 Portal responsivo | Must | Must | El cliente autoriza desde su celular; sin esto no hay HU-02 |
| HU-29 Reportes gerenciales | Could | Could | Ya está bien clasificada |
| HU-30 Aviso de privacidad | Must | Must | Lo exige la LFPDPPP; no se pueden pedir datos sin él |

Con la prueba quedan 9 historias Must en lugar de 17.

## 2. Puntos Must frente a la velocidad

| Dato | Valor |
| --- | --- |
| Historias del release propuesto | 11 historias, 40 puntos (`docs/04-requisitos/propuesta-release-v0.1.0.md`) |
| Must del release con la prioridad de hoy | 10 historias, 38 puntos: 95 % del release |
| Must del release después de la prueba | 9 historias, 35 puntos: 87.5 % del release |
| Límite recomendado | Alrededor de 60 % del esfuerzo (Agile Business Consortium): 24 puntos de 40 |
| Velocidad del equipo | Todavía no hay: los sprints 0 y 1 fueron de especificación y no terminaron historias (sección 2.3) |

Aun con la prueba, los Must pasan del 60 %. El release propuesto es casi todo flujo núcleo, así que casi todo es
Must, y no queda margen para imprevistos. Hay dos salidas que el Product Owner puede llevar al cliente:

1. Mantener el corte y aceptar el riesgo, con el compromiso de medir la velocidad al cerrar el Sprint 2.
2. Partir HU-12 o HU-14 para dejar una parte en Should, por ejemplo la firma presencial de HU-14 separada de la
   remota.

Cuando exista la velocidad del Sprint 2, se repite la cuenta con los puntos reales.

## 3. Corte del Release v0.1.0

El corte limitado al flujo núcleo ya existe y es el de la propuesta del 12/11/2026: recepción, diagnóstico y
asignación, cotización y autorización, más roles, portal y privacidad. La prueba del Must no lo cambia; solo
cambia la prioridad dentro de él (HU-07 pasa de Must a Should).

La presentación al cliente estaba en la minuta del 20/11/2026, pero esa minuta no tiene fecha, asistentes ni
decisiones. Mientras no se registre la decisión del cliente, el corte sigue siendo una propuesta.
