# Pruebas estáticas · Revisión cruzada del SRS por el Equipo A

Material para que el Equipo A pruebe nuestros requisitos sin producto, como indica «Pruebas de requisitos sin
producto» (18/11/2026). Responsable: QA Lead (Dulce María Estudillo Rosado). Issue #120.

La prueba estática revisa el documento, no el software. Las tres primeras técnicas **verifican** (¿el
requisito está bien escrito?) y la cuarta **valida** (¿es lo que el cliente necesita?).

| Técnica | Quién la hace | Formato |
| --- | --- | --- |
| 1. Inspección con lista de verificación | Revisor del Equipo A | [`lista-de-verificacion.md`](lista-de-verificacion.md) |
| 2. Casos de prueba escritos en papel | Revisor del Equipo A | [`formatos.md`](formatos.md#1-caso-de-prueba-en-papel) |
| 3. Recorrido con un escenario real | Revisor del Equipo A | [`formatos.md`](formatos.md#2-recorrido-con-un-escenario-real) |
| 4. Validación con el cliente mediante un prototipo | Equipo B con el cliente; el Equipo A observa | [`formatos.md`](formatos.md#4-observación-del-prototipo) |

## 1. Qué se revisa

- **Documento:** `docs/documento/secciones/04-srs.tex`, versión v0.2.20 (rama `main`).
- **Requisitos:** 16 RF (4.4), 30 historias HU (4.5), 13 RNF (4.6; RNF-07 pasó a restricciones en 4.3.2) y
  15 reglas de negocio RN (4.7).
- **Apoyo:** glosario (4.2), restricciones (4.3.2), contingencia (4.7.1) y prototipos (4.10), para comprobar
  la consistencia.

## 2. Reparto por secciones

La QA Lead del Equipo A asigna a sus revisores. Del lado del Equipo B asiste el autor de cada sección para
responder dudas en la reunión. La columna del Equipo B es una propuesta que confirma nuestra QA Lead.

| Bloque | Requisitos | Revisor (Equipo A) | Autor presente (Equipo B) |
| --- | --- | --- | --- |
| A | RF-01 a RF-11 y diagramas de casos de uso (4.4) | | Isis Alhelí González Maldonado |
| B | HU-01 a HU-15 (4.5) | | Isis Alhelí González Maldonado |
| C | HU-16 a HU-30 (4.5) | | Dulce María Estudillo Rosado |
| D | RNF-01 a RNF-14 (4.6) | | Isis Alhelí González Maldonado |
| E | RN-01 a RN-15 y contingencia (4.7) | | Ángel Yael Avendaño Guzmán |
| F | Glosario y prototipos (4.2, 4.10), solo consistencia | | Isis Yamilet Meléndez Hernández |

## 3. Cómo se organiza (ISO/IEC 20246:2017)

1. **Preparación individual (fuera de clase, 2 días).** Cada revisor aplica la lista de verificación a su
   bloque y escribe los casos de prueba en papel. Si no puede escribir el resultado esperado sin inventar un
   dato, el requisito está mal.
2. **Reunión de revisión (en clase, 40 min).** Roles: un moderador del Equipo A, el autor presente y un
   registrador. Se leen los hallazgos sin discutir soluciones; solo se confirma si el hallazgo es válido. Se
   llena el [registro de la reunión](formatos.md#3-registro-de-la-reunión).
3. **Registro.** Cada hallazgo confirmado se abre como issue en este repositorio con el formulario
   [`ISSUE_TEMPLATE/hallazgo-requisito.yml`](ISSUE_TEMPLATE/hallazgo-requisito.yml). Lleva el ID del
   requisito, la característica que falla, la descripción y la propuesta, con las etiquetas `requisitos` y
   `tipo:defecto-doc`.
4. **Corrección y verificación.** El autor corrige el SRS en una rama `docs/<issue>-...` y un PR que cite
   el issue. El revisor que lo reportó verifica y cierra el issue, o lo reabre con un comentario. Quien
   corrige no cierra su propia incidencia.

## 4. Reglas

- Se reporta sobre el producto, nunca sobre las personas.
- Un issue por hallazgo. Cada uno cita el requisito, la sección o el caso de prueba.
- El Equipo B puede rechazar un hallazgo, pero con una razón escrita en el issue.
- La severidad la propone el revisor; la prioridad la decide el Product Owner en el triage (S8-T6).
- Cuenta la calidad del reporte, no la cantidad. La guía pide al menos cuatro hallazgos por revisor (P2-T5).
- Solo datos ficticios.

## 5. Pendiente

- El formulario se activa al copiarlo a `.github/ISSUE_TEMPLATE/`, junto con los de S8-T6 (PR #117).
- Falta que el Equipo A asigne sus revisores en la tabla de la sección 2.
- La reunión de revisión y la validación con el cliente son presenciales y las hace el equipo.
