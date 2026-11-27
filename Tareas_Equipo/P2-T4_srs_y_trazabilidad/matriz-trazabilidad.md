# P2-T4 · Matriz de trazabilidad

Enlaza cada requisito funcional con su fuente, sus historias, sus casos de uso y sus casos de prueba. Se armó con
lo que hoy dice `main`: la sección 4.4 (RF), 4.5 (historias y sus casos CPA), 4.7 (reglas y sus fuentes), las
figuras 4.2 a 4.4 (casos de uso) y el plan de pruebas de la tarea P2-T6 (CPA-35 a CPA-50).

## Matriz

| Requisito | Prioridad | Fuente | Historias | Casos de uso | Casos de prueba |
| --- | --- | --- | --- | --- | --- |
| RF-01 Autenticación por rol | Must | Anteproyecto | HU-27 | «include» Autenticarse | CPA-28, CPA-29 |
| RF-02.1 Enlace seguro del cliente | Must | RN-01 · minuta A.2, E-03 | HU-02, HU-28 | CU-10, CU-11 | CPA-10, CPA-30 |
| RF-02.2 Expiración del enlace | Should | RN-01 · minuta A.2, E-03 | HU-02, HU-23 | CU-10 | **Sin caso** |
| RF-02.3 Enlace por SMS | Could | **Sin fuente registrada** | HU-02 | CU-11 | **Sin caso** |
| RF-03.1 Clientes y vehículos | Must | RN-07 · minuta A.2, E-06 | HU-05, HU-06 | CU-02 | CPA-33, CPA-48 |
| RF-03.2 Historial y garantía | Should | RN-13 · fuente por confirmar | HU-23, HU-24 | CU-07 | CPA-22, CPA-23 |
| RF-04 Recepción con fotografías | Must | RN-12 · anteproyecto; RN-14 · propuesta del equipo | HU-01, HU-25, HU-26 | CU-02 | CPA-01 a CPA-04, CPA-35, CPA-36, CPA-46, CPA-47 |
| RF-05 Órdenes, bahías y mecánico | Must | RN-05 (E-04), RN-06 (E-05), RN-09 (E-08) | HU-07, HU-08, HU-09, HU-11 | CU-05 | CPA-02, CPA-03, CPA-05 a CPA-08, CPA-44, CPA-45 |
| RF-06 Cotización y firma 2FA | Must | RN-02 (E-01), RN-03 (E-02), RN-11 · anteproyecto | HU-02, HU-12 a HU-15 | CU-03, CU-05, CU-11 | CPA-10 a CPA-17, CPA-39 a CPA-43 |
| RF-07 Re-cotización por más de 10 % | Must | RN-04 · anteproyecto | HU-16 | CU-11 | CPA-18, CPA-19, CPA-37, CPA-38 |
| RF-08.1 Solicitud de refacciones | Should | **Sin fuente registrada** | HU-10, HU-19 | CU-06 | **Sin caso** |
| RF-08.2 Proveedores y costos | Should | RN-06 · minuta A.2, E-05 | HU-17, HU-18 | CU-08 | **Sin caso** |
| RF-08.3 Ticket de compras | Could | **Sin fuente registrada** | HU-18 | CU-08 | **Sin caso** |
| RF-09 Agenda y confirmación de citas | Should | RN-05 (E-04), RN-08 (E-07) | HU-03, HU-04, HU-06 | CU-01, CU-09 | CPA-31, CPA-32, CPA-33, CPA-34 |
| RF-10 Entrega con saldo y crédito | Must | RN-10 · minuta A.2, E-09 | HU-21, HU-22, HU-23 | CU-04, CU-13 | CPA-21 a CPA-25, CPA-49, CPA-50 |
| RF-11 Panel del gerente | Should | Anteproyecto (monitoreo gerencial) | HU-29 | CU-12 | **Sin caso** |

## Lo que encontramos al armarla

Estos puntos se tienen que registrar como incidencias con la etiqueta `requisitos` y corregirse en el SRS.

1. **El mismo caso de prueba aparece en dos historias distintas.** CPA-02 y CPA-03 están en HU-01 y en HU-09;
   CPA-10 está en HU-02 y en HU-12; CPA-31 está en HU-03 y en HU-30. Un caso prueba una sola cosa, así que hay
   que renumerar.
2. **Historias Must sin ningún caso de prueba:** HU-25, HU-26 y HU-28. HU-25 y HU-26 la propuesta las pasa a la
   Fase 2, pero HU-28 sigue en el release.
3. **Requisitos sin caso de prueba:** RF-02.2, RF-02.3, RF-08.1, RF-08.2, RF-08.3 y RF-11. Ninguno es Must.
4. **Requisitos sin fuente:** RF-02.3, RF-08.1 y RF-08.3 no tienen ninguna regla ni hallazgo de minuta que los
   respalde. Hay que preguntarle al cliente o marcarlos como propuesta del equipo.
5. **RN-12 y RN-13** siguen con la fuente «por validar con el cliente». RN-14 y RN-15 el cliente las aceptó el
   09/11/2026 (minuta que agrega el PR #86), pero faltan los umbrales de 4 horas y 24 horas. Mientras no se
   validen, una historia Must que dependa de ellas no debería darse por cerrada.

## Requisitos no funcionales

| RNF | Característica (ISO/IEC 25010:2023) | Verificación prevista en el SRS |
| --- | --- | --- |
| RNF-01 | Flexibilidad | Pruebas manuales en 2 celulares reales |
| RNF-02, RNF-03 | Capacidad de interacción | Auditoría con Lighthouse o axe y prueba cronometrada |
| RNF-04 | Seguridad | Prueba con 20 autorizaciones y verificación de la huella SHA-256 |
| RNF-05 | Seguridad | Revisión de datos ficticios en cada PR |
| RNF-06 | Eficiencia de desempeño | 20 repeticiones cronometradas, percentil 95 |
| RNF-08 a RNF-10 | Fiabilidad | Pruebas sin conexión (Fase 2 si se acepta el corte) |
| RNF-11 a RNF-14 | Adecuación funcional, compatibilidad, protección y mantenibilidad | Según la sección 4.6 |

Los RNF todavía no tienen identificador de caso de prueba propio. La guía propone el prefijo `CPN-` para ellos.
