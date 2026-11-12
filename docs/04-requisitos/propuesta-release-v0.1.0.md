# Propuesta de alcance del Release v0.1.0

| Dato | Valor |
|---|---|
| Observación que atiende | B2 de la Review 1 (issue #29) |
| Elabora | Product Owner (Ángel Yael Avendaño Guzmán) |
| Fecha | 12 de noviembre de 2026 |
| Estado | **Propuesta. Pendiente de negociar con el cliente.** |

Este documento es la propuesta que se llevará al cliente. No cambia todavía el alcance: las secciones 3.3,
3.6 y 4.5 y el story map se actualizan cuando el cliente la acepte y quede registrado en la minuta.

## 1. Por qué se propone reducir el alcance

- **Hoy casi todo el sistema está en el Release v0.1.0:** 25 de las 30 historias, 92 de los 106 puntos.
- **El anteproyecto pide menos para la Fase 1:** que el flujo núcleo funcione de extremo a extremo y que el
  resto quede especificado y diseñado.
- **La operación sin conexión es el mayor riesgo técnico** (R-02): HU-25 y HU-26 suman 16 puntos y están
  comprometidas para v0.1.0.

El flujo núcleo del anteproyecto tiene cuatro pasos: recepción, diagnóstico y asignación, cotización y
autorización, y monitoreo gerencial.

## 2. Propuesta: historias que se quedan en v0.1.0

| Paso del flujo núcleo | Historia | Prioridad | Puntos |
|---|---|---|---|
| Recepción | HU-01 Recepción e inspección con evidencia fotográfica | Must | 3 |
| Diagnóstico y asignación | HU-07 Alerta de bahías ocupadas | Must | 3 |
| Diagnóstico y asignación | HU-08 Asignación de bahía y mecánico | Must | 5 |
| Diagnóstico y asignación | HU-09 Registro de diagnóstico en tableta | Must | 3 |
| Cotización y autorización | HU-12 Generación de presupuesto desglosado | Must | 5 |
| Cotización y autorización | HU-02 Autorización digital de cotización por el cliente | Must | 3 |
| Cotización y autorización | HU-14 Firma digital y autorización por 2FA | Must | 5 |
| Cotización y autorización | HU-15 Rechazo de cotización y cancelación | Should | 2 |
| Necesarias para todo el flujo | HU-27 Gestión de roles y permisos de seguridad | Must | 3 |
| Necesarias para todo el flujo | HU-28 Accesibilidad PWA responsiva para clientes | Must | 5 |
| Necesarias para todo el flujo | HU-30 Cumplimiento de privacidad y uso de datos ficticios | Must | 3 |
| | **Total: 11 historias** | | **40** |

## 3. Propuesta: historias que pasan a la Fase 2

En la Fase 1 quedan especificadas y diseñadas (SRS, modelos y prototipos), pero no se construyen. Conservan
su prioridad en el Product Backlog.

| Grupo | Historias | Puntos | Motivo |
|---|---|---|---|
| Operación sin conexión | HU-25, HU-26 | 16 | Mayor riesgo técnico (R-02); no forma parte del flujo núcleo |
| Cobro, entrega y crédito | HU-20, HU-21, HU-22, HU-23 | 11 | El flujo núcleo del anteproyecto termina en la autorización |
| Refacciones y proveedores | HU-10, HU-17, HU-18 | 9 | No forma parte del flujo núcleo |
| Citas en línea y agenda | HU-03, HU-04, HU-06 | 8 | No forma parte del flujo núcleo |
| Re-cotización por sobrecosto | HU-16 | 5 | Ocurre durante la reparación, después del flujo núcleo |
| Servicios opcionales en la cotización | HU-13 | 3 | Variante de la autorización; no es indispensable |
| | **Total: 14 historias** | **52** | |

Las cinco historias que ya estaban en la Fase 2 no cambian: HU-05, HU-11, HU-19, HU-24 y HU-29 (14 puntos).

## 4. Resultado

| | Hoy | Propuesta |
|---|---|---|
| Historias en v0.1.0 | 25 | 11 |
| Puntos en v0.1.0 | 92 | 40 |
| Historias en Fase 2 | 5 | 19 |
| Puntos en Fase 2 | 14 | 66 |

## 5. Puntos que debe decidir el cliente

1. **Monitoreo gerencial.** El anteproyecto incluye en el flujo núcleo un panel del gerente con las órdenes
   abiertas, su estado y la carga del taller. Hoy las historias más cercanas (HU-11 y HU-29) están en la
   Fase 2. Se le pregunta al cliente si quiere en v0.1.0 una vista mínima de órdenes abiertas y su estado,
   o si el panel completo puede esperar a la Fase 2.
2. **Cobro y cierre de la orden.** Sin HU-21 y HU-23 (6 puntos) la orden no se cobra ni se cierra dentro
   del sistema en v0.1.0. Se le pregunta si acepta cerrar las órdenes como hasta hoy durante la Fase 1.
3. **Citas en línea.** El producto se llama «Órdenes de Servicio y Citas», pero las citas no están en el
   flujo núcleo del anteproyecto. Se le pregunta si acepta que queden diseñadas y se construyan en la Fase 2.
4. **Operación sin conexión.** Se le explica el riesgo R-02 y se le pregunta si acepta operar con conexión
   en v0.1.0, con los procedimientos de contingencia de 4.7.1 mientras tanto. Esos procedimientos se validan
   en la misma sesión (observación B10).

## 6. Siguientes pasos

1. Agendar la sesión con el cliente en la semana del 17 al 20 de noviembre de 2026.
2. Registrar en la minuta qué aceptó, qué rechazó y qué cambió.
3. Actualizar 3.3, 3.6, el release de cada historia en 4.5 y el story map con el alcance acordado
   (fecha límite: viernes 20 de noviembre de 2026).
