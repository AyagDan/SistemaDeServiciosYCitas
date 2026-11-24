# P2-T8 · Modelo entidad-relación y esquema relacional en 3FN

Tarea de equipo P2-T8 de la guía del segundo parcial. El diagrama está en `er-flujo-nucleo.puml` (notación de
pata de gallo) y cubre las tablas del flujo núcleo. El esquema completo, con refacciones, compras, pagos y
garantía, está en `db/schema.sql`.

## 1. Cómo leer el diagrama

- Un cliente tiene cero o muchos vehículos; cada vehículo es de un solo cliente.
- Un cliente es particular o flotilla: `cliente_particular` y `flotilla` comparten la llave de `cliente`.
- Cada vehículo recibe cero o muchas órdenes de servicio; cada orden es de un solo vehículo.
- Una orden ocupa como máximo una de las 4 bahías (RN-05) y tiene como máximo un mecánico responsable (RN-09).
- Cada orden tiene a lo más una recepción; cada recepción tiene un checklist y sus fotografías (RN-12 pide al
  menos 4, y eso se valida en la API, no en la cardinalidad).
- Una cotización tiene uno o más conceptos (`detalle_cotizacion`) y cero o muchas autorizaciones.

## 2. Relaciones muchos a muchos que se resolvieron

| Relación N:M | Entidad asociativa | Llave | Qué guarda que no es de ninguna de las dos |
| --- | --- | --- | --- |
| Orden de servicio y mecánicos que colaboran | `asignacion_colaborador` | (folio, id_usuario) | fecha_asignacion |
| Cotización y conceptos de trabajo | `detalle_cotizacion` | id_detalle | cantidad, precio_unitario, seleccionado |

El precio unitario se copia al detalle de la cotización porque el precio de una refacción puede cambiar después.

## 3. Normalización paso a paso

### Punto de partida: la orden de servicio en papel

Así se vería la orden que hoy se llena a mano en la recepción (proceso actual, sección 3.5), pasada tal cual a
una hoja de cálculo. Los datos son ficticios.

| folio | fecha | cliente | telefono | correo | placas | marca y modelo | bahia | mecanico | conceptos | total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OS-0001 | 2026-11-02 | Ana Prueba | 971 000 0001 | ana@ejemplo.com | TST-001-A | Nissan Versa 2019 | 2 | Luis Ficticio | Afinación x1 $900; Bujías x4 $480 | $1,380 |
| OS-0002 | 2026-11-05 | Ana Prueba | 971 000 0001 | ana@ejemplo.com | TST-001-A | Nissan Versa 2019 | 1 | Luis Ficticio | Balatas x1 $750 | $750 |

Problemas: el teléfono y el correo de Ana se repiten en cada orden; si cambia de número hay que corregir todas las
filas. La columna «conceptos» guarda una lista y «marca y modelo» junta dos datos.

### Primera forma normal (1FN)

**Regla:** cada celda tiene un solo valor y no hay grupos repetidos.

- «conceptos» se separa en una fila por concepto, con su cantidad y precio unitario.
- «marca y modelo» se separa en marca, modelo y año.
- La llave queda compuesta: (folio, concepto).

### Segunda forma normal (2FN)

**Regla:** está en 1FN y cada atributo depende de toda la llave, no de una parte.

- fecha, placas, bahía y mecánico dependen solo del folio, no del concepto. Se separan en **orden_servicio**
  con llave folio.
- cantidad y precio unitario sí dependen de la orden y del concepto. Se quedan en **detalle_cotizacion**.
- El total no se guarda: se calcula con la suma de cantidad × precio_unitario de los conceptos seleccionados.

### Tercera forma normal (3FN)

**Regla:** está en 2FN y ningún atributo depende de otro atributo que no es llave.

- marca, modelo y año dependen de las placas, no del folio. Se separan en **vehiculo**.
- teléfono y correo dependen del cliente, no del vehículo. Se separan en **cliente**.
- el nombre del mecánico depende del mecánico. Se separa en **usuario** y la orden guarda solo
  `id_usuario_responsable`.
- el estado de la bahía depende de la bahía. Se separa en **bahia**.

Resultado: si Ana cambia de teléfono, se corrige en una sola fila de `cliente`.

## 4. Esquema lógico

PK = llave primaria, FK = llave foránea, UQ = valor único.

| Tabla | Llave primaria | Llaves foráneas | Por qué existe la FK |
| --- | --- | --- | --- |
| cliente | id_cliente | — | — |
| cliente_particular | id_cliente | id_cliente → cliente | Subtipo de cliente: comparte su llave |
| flotilla | id_cliente | id_cliente → cliente | Subtipo de cliente con crédito (RN-10) |
| vehiculo | id_vehiculo | id_cliente → cliente | Relación 1:N; la FK va del lado «muchos» |
| usuario | id_usuario | — | — |
| bahia | numero | — | — |
| orden_servicio | folio | id_vehiculo → vehiculo; id_usuario_abre, id_usuario_responsable, id_usuario_autoriza_credito → usuario; numero_bahia → bahia | Cada orden es de un vehículo, la abre una persona, tiene un responsable y ocupa una bahía |
| asignacion_colaborador | (folio, id_usuario) | folio → orden_servicio; id_usuario → usuario | Resuelve la relación N:M de colaboración (RN-09) |
| recepcion_vehicular | id_recepcion | folio → orden_servicio (UQ) | Relación 1:1: una recepción por orden |
| checklist_inspeccion | id_checklist | id_recepcion → recepcion_vehicular (UQ) | Relación 1:1 |
| fotografia | id_foto | id_recepcion → recepcion_vehicular | Relación 1:N (RN-12) |
| diagnostico | id_diagnostico | folio → orden_servicio; id_usuario → usuario | Quién diagnosticó cada orden |
| cotizacion | id_cotizacion | folio → orden_servicio | Una orden puede tener varias versiones (RN-04, RN-11) |
| detalle_cotizacion | id_detalle | id_cotizacion → cotizacion | Conceptos de cada cotización |
| autorizacion | id_autorizacion | id_cotizacion → cotizacion | Cada autorización inicial o por incremento mayor al 10 % (RN-02, RN-04) |

Todas las tablas están en 3FN: sus atributos dependen solo de su llave. Los nombres van sin acentos ni espacios,
como pide la guía para el modelo físico.

## 5. Coherencia con el resto del proyecto

- Cada almacén del diagrama 0 de la tarea P2-T7 corresponde a una o más de estas tablas.
- Los estados de `estado_orden` son los mismos de la máquina de estados de la sección 6.5.
- El PR #92 agrega al repositorio un diagrama E-R de todo el esquema en `docs/06-analisis/er/`. Este archivo
  cubre solo el flujo núcleo y suma la justificación de la normalización que pide la tarea.
