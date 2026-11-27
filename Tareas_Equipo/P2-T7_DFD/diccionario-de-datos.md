# P2-T7 · Diagramas de flujo de datos y diccionario de datos

Tarea de equipo P2-T7 de la guía del segundo parcial. Los tres diagramas están en esta carpeta como fuente
PlantUML:

| Archivo | Qué muestra |
| --- | --- |
| `dfd-contexto.puml` | El sistema como un solo proceso (0) con sus 6 entidades externas y 23 flujos |
| `dfd-nivel-0.puml` | El proceso 0 abierto en 8 procesos y 8 almacenes |
| `dfd-nivel-1-proceso-4.puml` | El proceso 4 «Cotizar y autorizar» abierto en 5 subprocesos |

Se usa una aproximación a la notación de Gane y Sarson: entidades en rectángulo azul, procesos en rectángulo
redondeado con su número arriba y almacenes en gris con su identificador D1 a D8.

## Balanceo

**Contexto → nivel 0.** Los 23 flujos entre entidades y el proceso 0 aparecen en el diagrama 0, cada uno en el
proceso que lo atiende. No aparece ningún flujo nuevo con entidades externas.

| Proceso del diagrama 0 | Flujos con entidades externas |
| --- | --- |
| 1 Gestionar citas | solicitud de cita, confirmación de cita, agenda del día |
| 2 Recibir vehículo y abrir orden | datos del cliente y vehículo, datos de recepción, alerta de bahías ocupadas |
| 3 Diagnosticar y asignar | asignación de bahía y mecánico, diagnóstico, órdenes asignadas |
| 4 Cotizar y autorizar | conceptos de la cotización, respuesta a la cotización, código de verificación, cotización, notificación al cliente |
| 5 Gestionar refacciones | solicitud de refacciones, datos de la compra, solicitudes pendientes |
| 6 Cobrar y entregar | datos del pago, autorización de crédito, comprobante de entrega |
| 7 Consultar y monitorear | estado del vehículo, panel del taller |
| 8 Administrar personal | datos del personal |

**Nivel 0 → nivel 1 (proceso 4).** Entran los mismos tres flujos (conceptos de la cotización, respuesta a la
cotización, código de verificación), salen los mismos dos (cotización, notificación al cliente) y se usan los
mismos almacenes (D1, D3 y D5).

**Reglas que se revisaron:** todo proceso tiene al menos una entrada y una salida; ningún flujo va directo entre
entidades, entre almacenes ni entre una entidad y un almacén; el diagrama de contexto no tiene almacenes; cada
flujo tiene nombre.

## Notación del diccionario

`=` está compuesto de · `+` y · `{ }` se repite · `[ | ]` uno de · `( )` opcional

## Flujos de datos

| Flujo | Definición |
| --- | --- |
| solicitud de cita | nombre_cliente + telefono + correo + placas + fecha + hora |
| confirmación de cita | id_cita + numero_bahia + [Confirmada \| Cancelada] |
| agenda del día | fecha + {cita} |
| datos del cliente y vehículo | telefono + correo + [nombre \| razon_social] + placas + marca + modelo + anio + (vin) + tipo_vehiculo |
| datos de recepción | (id_cita) + kilometraje + nivel_combustible + checklist + {fotografia} |
| alerta de bahías ocupadas | fecha_hora + "Sin bahías disponibles" + lugares_libres_estacionamiento |
| asignación de bahía y mecánico | folio + numero_bahia + id_mecanico_responsable + ({id_mecanico_colaborador}) |
| diagnóstico | folio + descripcion + fecha_hora |
| órdenes asignadas | {folio + placas + estado + numero_bahia} |
| conceptos de la cotización | folio + {concepto} |
| cotización | folio + version + fecha_emision + fecha_vencimiento + {concepto} + total |
| respuesta a la cotización | folio + version + [aprobar + {id_concepto_seleccionado} \| rechazar] |
| código de verificación | 6{digito}6 |
| notificación al cliente | correo + asunto + [enlace_seguimiento \| codigo_verificacion] |
| solicitud de refacciones | folio + {id_refaccion + cantidad} |
| solicitudes pendientes | {id_solicitud + folio + id_refaccion + cantidad + estado_solicitud} |
| datos de la compra | id_proveedor + numero_ticket + fecha_compra + {id_refaccion + cantidad + precio_unitario} |
| datos del pago | folio + monto + metodo_pago |
| autorización de crédito | folio + id_gerente + fecha_hora |
| comprobante de entrega | folio + fecha_entrega + total_pagado + [saldado \| a_credito] |
| estado del vehículo | folio + placas + estado + (cotizacion) |
| panel del taller | {orden abierta + estado} + ocupacion_bahias + tiempo_estancia + ingresos_acumulados |
| datos del personal | nombre + correo + rol + activo |

## Elementos que se repiten

| Elemento | Definición |
| --- | --- |
| concepto | id_concepto + descripcion + [ManoDeObra \| Refaccion \| Insumo] + cantidad + precio_unitario + opcional |
| checklist | carroceria + interiores + (observaciones) + completo |
| fotografia | archivo + [Frente \| Trasera \| Izquierda \| Derecha \| Otra] + fecha_hora |
| nivel_combustible | [Reserva \| UnCuarto \| Mitad \| TresCuartos \| Lleno] |
| tipo_vehiculo | [Automovil \| Motocicleta \| Camioneta] |
| rol | [Gerente \| Recepcionista \| Mecanico \| JefeMecanicos \| EncargadoAlmacen] |
| estado | [Abierta \| EnEsperaDeBahia \| Diagnosticada \| Autorizada \| EnReparacion \| EsperandoRefaccion \| EsperandoAutorizacionAdicional \| ListaParaEntrega \| Cerrada \| Cancelada] |

## Flujos internos del nivel 1

| Flujo | Definición |
| --- | --- |
| cotización emitida | id_cotizacion + folio + version + fecha_emision + {concepto} |
| cotización vigente | id_cotizacion + fecha_vencimiento + estado_cotizacion |
| conceptos seleccionados | id_cotizacion + {id_concepto + seleccionado} |
| monto a autorizar | id_cotizacion + monto_aceptado + correo |
| autorización verificada | id_cotizacion + monto_aceptado + fecha_hora + ip + [Remoto \| Presencial] |
| rechazo | id_cotizacion + fecha_hora |

## Almacenes

| Almacén | Definición | Tablas de `db/schema.sql` |
| --- | --- | --- |
| D1 Clientes y vehículos | {cliente + {vehiculo}} | cliente, cliente_particular, flotilla, vehiculo |
| D2 Citas | {cita} | cita |
| D3 Órdenes de servicio | {folio + estado + numero_bahia + responsable + {historial_estado}} | orden_servicio, bahia, asignacion_colaborador, historial_estado, diagnostico |
| D4 Recepciones | {recepcion + checklist + {fotografia}} | recepcion_vehicular, checklist_inspeccion, fotografia |
| D5 Cotizaciones y autorizaciones | {cotizacion + {concepto} + {autorizacion}} | cotizacion, detalle_cotizacion, autorizacion, token_acceso |
| D6 Refacciones y compras | {refaccion} + {solicitud} + {compra} | refaccion, solicitud_refaccion, proveedor, compra, detalle_compra, entrega_refaccion |
| D7 Pagos | {pago} | pago, garantia |
| D8 Personal | {usuario} | usuario |

Cada almacén corresponde a una o más tablas del esquema, como pide la guía para la Review 3.
