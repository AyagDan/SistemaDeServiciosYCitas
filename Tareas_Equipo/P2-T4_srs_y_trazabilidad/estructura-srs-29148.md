# P2-T4 · El SRS frente a la estructura de ISO/IEC/IEEE 29148:2018

La tarea P2-T4 pide el SRS v1.0 con la estructura de la norma, la tabla de versiones y la matriz de trazabilidad.
El SRS vive en el Documento de Ingeniería (`docs/documento/`), que sigue la numeración del machote. La guía dice
que, si el machote numera distinto, se sigue el machote: la norma dice qué debe contener, no cómo numerarlo.

Por eso aquí no se reescribe el SRS. Se revisa qué parte del documento cubre cada contenido de la norma y qué
falta para poder llamarlo v1.0.

## Correspondencia

| Contenido según 29148 | Dónde está en el documento | Estado en `main` |
| --- | --- | --- |
| Propósito, alcance y audiencia | 4.1 | Completo |
| Perspectiva del producto y funciones principales | 3.1 a 3.3 | Completo |
| Características de los usuarios | 4.3.1 | Completo |
| Limitaciones, supuestos y dependencias | 4.3.2 | Completo (las restricciones ya están separadas de los RNF, B8) |
| Definiciones y acrónimos | 4.2 Glosario | Completo |
| Referencias | 13 Referencias | Completo |
| Requisitos funcionales | 4.4 y 4.5 | Completo; los criterios se corrigen en el PR #95 (B9) |
| Usabilidad, desempeño y atributos de calidad | 4.6 | Completo (B8) |
| Requisitos lógicos de la base de datos | 6.2 y `db/schema.sql` | Falta la sección 6.2 en el documento |
| Cumplimiento de normas y leyes | 4.8 Protección de datos | Falta en el documento LaTeX |
| Reglas de negocio | 4.7 y 4.7.1 | Completo; RN-12 a RN-15 por validar |
| Casos de uso | 4.9 | Solo están los diagramas; faltan los casos documentados (ver P2-T3) |
| Verificación de cada requisito | 5 Plan de pruebas y trazabilidad | Falta la sección 5 (ver P2-T6 y la matriz de esta carpeta) |
| Apéndices: modelos y prototipos | 4.10, 6 y anexos | Parcial: hay wireframes y máquina de estados; faltan DFD y modelo E-R (P2-T7 y P2-T8) |

## Tabla de versiones propuesta para llegar a v1.0

La versión actual es la v0.2.x con las correcciones de la Review 1. La v1.0 es la primera que aprueba el
cliente, así que no se puede asignar hasta tener su firma.

| Versión | Qué cambia | Quién la hace | Quién aprueba |
| --- | --- | --- | --- |
| 0.2.x | Correcciones B1 a B11 de la Review 1 | Equipo | — |
| 0.3 | Secciones 4.9 (casos de uso), 5 (pruebas y trazabilidad), 6.1 (DFD) y 6.2 (modelo de datos), tomadas de las tareas P2-T3, P2-T4, P2-T6, P2-T7 y P2-T8 | Developers y QA Lead | — |
| 0.4 | Corte del release y reglas RN-12 a RN-15 con la decisión del cliente | Product Owner | — |
| 1.0 | Versión validada con el cliente | Product Owner | Cliente (firma en «Aprobación del cliente», que el machote pide después del control de versiones) |

## Qué falta para el v1.0

1. Integrar al documento las secciones que salen de estas tareas.
2. Que el cliente decida el corte del release y las reglas pendientes (minuta del 20/11/2026, todavía sin decisiones).
3. Agregar al documento la sección «Aprobación del cliente» del machote, que todavía no existe, y conseguir la firma.
4. Que portada, control de versiones y contenido digan la misma versión.
