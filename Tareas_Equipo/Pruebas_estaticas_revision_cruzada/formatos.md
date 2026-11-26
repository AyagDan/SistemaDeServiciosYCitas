# Formatos de la prueba estática

Se imprimen o se copian para llenarlos a mano. Solo datos ficticios: placas que empiezan con `TST` y correos
de `ejemplo.com`.

## 1. Caso de prueba en papel

Uno por requisito. Si no puedes llenar «Resultado esperado» sin inventar un dato, el requisito falla y anotas
en «Preguntas sin respuesta» qué le falta.

| Campo | Contenido |
| --- | --- |
| Requisito | (ID y texto copiado del SRS) |
| Revisor | |
| Precondiciones | (estado del sistema y datos antes de empezar) |
| Datos de entrada | (valores concretos: placa, monto, fecha, rol) |
| Pasos | 1. … 2. … 3. … |
| Resultado esperado | (lo que debe verse o guardarse, con el dato exacto) |
| Preguntas sin respuesta | (lo que tuviste que suponer: fórmula, límite, caso de error) |
| ¿Se puede escribir sin inventar? | Sí / No |
| Característica que falla | Verificable / Completo / Sin ambigüedad / Otra: ____ |

Ejemplo de la guía (requisito de la cooperativa, no de este SRS): «El sistema calculará el pago semanal de las
socias». Al escribir el caso faltan la fórmula, los anticipos, el precio si cambió a media semana y qué pasa si
el resultado es negativo. Conclusión: no es verificable ni completo; se propone agregar la fórmula y un ejemplo
con números.

## 2. Recorrido con un escenario real

El revisor narra un día del taller paso a paso y anota qué requisito cubre cada paso. Un paso sin requisito es
un hallazgo de completitud.

Revisor: ____________________  Fecha: ____ / ____ / 2026

| # | Paso del escenario | Quién lo hace | Requisito que lo cubre (RF, HU o RN) | ¿Hallazgo? |
| --- | --- | --- | --- | --- |
| 1 | Un cliente llega al taller con su vehículo | | | |
| 2 | Se registra el vehículo | | | |
| 3 | Se diagnostica | | | |
| 4 | El cliente no autoriza la reparación | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |

Los primeros cuatro pasos son el ejemplo del documento del profesor. El revisor continúa el día con otros
casos: un cliente sin cita, un aumento en la cotización, una refacción que no llega, un pago incompleto, una
falla de luz.

## 3. Registro de la reunión

Lo llena el registrador durante la reunión de 40 minutos. No se discuten soluciones: solo se decide si el
hallazgo es válido.

| Dato | Valor |
| --- | --- |
| Fecha y hora | |
| Moderador (Equipo A) | |
| Registrador | |
| Autores presentes (Equipo B) | |
| Revisores presentes | |
| Versión revisada | v0.2.20 |

| # | Requisito | Característica que falla | Hallazgo (una frase) | Técnica | ¿Válido? | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | Sí / No | # |
| 2 | | | | | Sí / No | # |
| 3 | | | | | Sí / No | # |
| 4 | | | | | Sí / No | # |
| 5 | | | | | Sí / No | # |
| 6 | | | | | Sí / No | # |

Hallazgos rechazados y su razón:

## 4. Observación del prototipo

La sesión con el cliente es presencial. El Equipo B le pide al cliente que haga una tarea real con el
prototipo y el revisor del Equipo A anota.

| Dato | Valor |
| --- | --- |
| Fecha | |
| Prototipo usado | (pantallas de 4.10) |
| Tarea que se le pidió al cliente | |
| Observador (Equipo A) | |

| # | Momento | Dónde se confundió o qué pidió | ¿Está en el SRS? (ID) | ¿Hallazgo? |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

Si el cliente pide algo que no está en el SRS, no es un defecto: se abre como solicitud de cambio
(`tipo:cambio`, S8-T6).
