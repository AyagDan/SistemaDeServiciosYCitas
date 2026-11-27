# P2-T3 · Casos de uso documentados con la plantilla de Cockburn

Tarea de equipo P2-T3 de la guía del segundo parcial: dos casos de uso completos y el diagrama de casos de uso
del sistema (`diagrama-casos-de-uso.puml`, en esta carpeta).

Se eligieron dos casos del flujo núcleo del Release v0.1.0: la recepción (CU-02) y la autorización remota de la
cotización (CU-11). Los identificadores son los mismos de las figuras 4.2 a 4.4 del Documento de Ingeniería.

---

## CU-02 · Recepción del vehículo y apertura de la orden

| Campo | Contenido |
| --- | --- |
| Nombre e ID | CU-02 Recepción del vehículo y apertura de la orden |
| Actor principal | Recepcionista |
| Actores secundarios | Ninguno |
| Nivel | Objetivo de usuario |
| Interesados | Dueños (quieren evidencia contra reclamos por daños), cliente (quiere que conste cómo dejó su vehículo) |
| Precondiciones | La recepcionista inició sesión con su rol (RF-01). El vehículo está en el taller. |
| Garantía mínima | Si la recepción no se completa, no se abre ninguna orden y no queda un registro a medias. |
| Garantía de éxito | Queda una orden en estado «Abierta» con folio, la recepción con kilometraje, combustible, checklist completo y al menos 4 fotografías, y el sello de fecha y hora. |
| Disparador | Llega un cliente a dejar su vehículo, con cita o sin ella. |

**Escenario principal**

1. La recepcionista busca la cita confirmada del cliente por su folio.
2. El sistema precarga los datos del cliente y del vehículo de la cita.
3. La recepcionista captura el kilometraje y el nivel de combustible.
4. La recepcionista llena el checklist de carrocería e interiores.
5. La recepcionista toma las fotografías del frente, la parte trasera, el costado izquierdo y el costado derecho.
6. El sistema comprueba que el checklist esté completo y que estén las 4 fotografías.
7. La recepcionista confirma la recepción.
8. El sistema abre la orden con su folio y guarda la fecha y hora de recepción.
9. El sistema muestra las bahías libres para que el jefe de mecánicos asigne la orden (CU-05).

**Extensiones**

- **1a. El cliente llega sin cita:** la recepcionista busca al cliente por teléfono o placas; si no existe, lo
  registra con su vehículo (RF-03.1). El caso continúa en el paso 3.
- **2a. El vehículo no es ligero** (bicicleta, tráiler, maquinaria o camioneta de más de 3 toneladas): el sistema
  no permite registrarlo y muestra el motivo (RN-07). El caso termina sin abrir orden.
- **3a. El medidor de combustible no funciona:** la recepcionista elige «No verificable», anota el método usado y
  el nivel que declara el cliente (RN-14, procedimiento de 4.7.1).
- **5a. Falta alguna de las 4 fotografías:** el sistema indica cuál falta y no deja confirmar (RN-12). El caso
  regresa al paso 5.
- **6a. El checklist está incompleto:** el sistema marca los puntos que faltan y no deja confirmar. El caso
  regresa al paso 4.
- **9a. Las 4 bahías están ocupadas:** el sistema muestra «Sin bahías disponibles» y la orden queda en espera de
  bahía; el vehículo pasa al estacionamiento de recepción (HU-07, RN-05).
- **9b. Las 4 bahías y los 5 lugares del estacionamiento están ocupados:** el SRS no dice qué pasa. Queda como
  pregunta abierta para el cliente.

**Requisitos especiales:** el registro con 5 fotografías se guarda en máximo 2 s, percentil 95 (RNF-06); la
interfaz de la tableta usa botones de al menos 48 × 48 px (RNF-02).

**Trazabilidad:** RF-03.1, RF-04, HU-01, HU-06, HU-07, RN-05, RN-07, RN-12, RN-14, CPA-01 a CPA-06.

---

## CU-11 · Aprobación remota de la cotización con código de verificación

| Campo | Contenido |
| --- | --- |
| Nombre e ID | CU-11 Aprobación remota de la cotización (2FA) |
| Actor principal | Cliente del taller |
| Actores secundarios | Servicio de correo (envía el código de verificación) |
| Nivel | Objetivo de usuario |
| Interesados | Cliente (no pagar trabajos que no aprobó), dueños (tener prueba de lo autorizado) |
| Precondiciones | La orden está «Diagnosticada», tiene una cotización emitida y el cliente recibió el enlace de seguimiento (RF-02.1). |
| Garantía mínima | Si el cliente no termina, la cotización sigue «Pendiente» y no se autoriza ningún trabajo. |
| Garantía de éxito | Queda una autorización «Confirmada» con el monto aceptado, los conceptos elegidos, la fecha, la hora y el medio «Remoto»; la orden pasa a «Autorizada». |
| Disparador | El cliente abre el enlace que le llegó por correo. |

**Escenario principal**

1. El cliente abre el enlace de seguimiento desde su celular.
2. El sistema muestra la cotización desglosada en mano de obra y refacciones, con su fecha de vencimiento.
3. El cliente marca o desmarca los conceptos opcionales.
4. El sistema recalcula el total con lo que el cliente dejó marcado.
5. El cliente pulsa «Aprobar».
6. El sistema envía al correo registrado del cliente un código de 6 dígitos, de un solo uso y válido 5 minutos (RN-02).
7. El cliente escribe el código.
8. El sistema valida el código, registra la autorización y cambia la orden a «Autorizada».
9. El sistema muestra al cliente el resumen de lo que autorizó.

**Extensiones**

- **1a. El enlace ya expiró** porque el vehículo se entregó y se saldó: el sistema muestra que el enlace no es
  válido y que puede pedir uno nuevo al taller (RN-01). El caso termina.
- **2a. La cotización tiene más de 5 días naturales:** el sistema la muestra como «Vencida» y no deja aprobarla;
  el taller debe emitir una nueva versión (RN-11). El caso termina.
- **3a. El cliente deja sin marcar todos los opcionales:** el total queda solo con los conceptos obligatorios
  (RN-03).
- **5a. El cliente pulsa «Rechazar»:** se ejecuta el caso extendido «Rechazar cotización» (HU-15); la orden pasa a
  «Cancelada» y se coordina la recolección del vehículo.
- **7a. El código es incorrecto:** el sistema avisa y deja escribirlo otra vez. El SRS no fija cuántos intentos
  hay; queda como pregunta abierta.
- **7b. Pasaron más de 5 minutos:** el sistema indica que el código venció y ofrece enviar uno nuevo. El caso
  regresa al paso 6.

**Requisitos especiales:** se usa desde el navegador del celular sin instalar nada (HU-28, RNF-01); la
autorización guarda evidencia que no se puede alterar (RNF-04).

**Trazabilidad:** RF-02.1, RF-06, HU-02, HU-13, HU-14, HU-15, RN-01, RN-02, RN-03, RN-11, CPA-10 a CPA-17, CPA-30.

---

## Preguntas abiertas que salieron al escribir los casos

| # | Pregunta | Caso | Para quién |
| --- | --- | --- | --- |
| 1 | ¿Qué se hace si llegan vehículos y no hay bahía ni lugar en el estacionamiento? | CU-02, 9b | Cliente |
| 2 | ¿Cuántos intentos tiene el cliente para escribir bien el código antes de bloquearlo? | CU-11, 7a | Cliente |
