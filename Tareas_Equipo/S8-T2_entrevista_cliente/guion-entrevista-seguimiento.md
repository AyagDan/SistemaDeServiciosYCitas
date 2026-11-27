# S8-T2 · Guion de la entrevista de seguimiento con el cliente

| Dato | Valor |
| --- | --- |
| Tarea | S8-T2 (guía de la semana 8) |
| Cliente | El profesor, que actúa como cliente (Servicio Automotriz Hermanos Ruiz) |
| Duración | 30 minutos |
| Conduce | Product Owner (Ángel Yael Avendaño Guzmán) |
| Toma la minuta | Developer (Isis Yamilet Meléndez Hernández) |
| Controla el tiempo | QA Lead (Dulce María Estudillo Rosado) |
| Fecha | Por agendar con el profesor |

## Objetivo

Cerrar lo que sigue abierto en el SRS: las reglas que el equipo propuso y el cliente no ha confirmado, las
suposiciones del glosario y las preguntas que salieron al escribir los casos de uso. Sin estas respuestas, esas
reglas no pueden sostener una historia Must.

## Antes de empezar

- Pedir permiso para grabar y explicar que solo sirve para escribir la minuta.
- Recordar en un minuto lo que se acordó el 19/10 y el 09/11.

## 1. Reglas pendientes de validar

1. RN-12 pide al menos 4 fotografías al recibir un vehículo (frente, trasera y los dos costados). ¿Con esas
   cuatro basta para defenderse de un reclamo, o hay alguna parte del vehículo que siempre deban fotografiar?
2. RN-13 dice que la mano de obra tiene 30 días de garantía desde la entrega. ¿De dónde sale ese plazo y hay
   trabajos que tengan otro?
3. Para la contingencia en papel (RN-15) propusimos pasar a papel cuando el corte pasa de 4 horas o la batería
   baja del 20 %, y capturar todo en 24 horas. ¿Esos números le funcionan en su taller?

## 2. Casos que el SRS no cubre

4. Si llegan vehículos cuando las 4 bahías y los 5 lugares del estacionamiento están ocupados, ¿qué hacen hoy?
5. Cuando un cliente se equivoca varias veces al escribir el código de verificación, ¿qué le gustaría que pasara?
6. ¿Quién debe poder dar de alta a una flotilla como cliente con crédito?

## 3. Corte del Release v0.1.0

Se presenta `docs/04-requisitos/propuesta-release-v0.1.0.md` (11 historias, 40 puntos) y se le pide decidir los
cuatro puntos de la sección 5 de esa propuesta:

7. ¿Quiere en v0.1.0 una vista mínima de órdenes abiertas para el gerente, o el panel completo puede esperar?
8. ¿Acepta cerrar y cobrar las órdenes como hoy durante la Fase 1?
9. ¿Acepta que las citas en línea se construyan en la Fase 2?
10. ¿Acepta trabajar con conexión en v0.1.0 y usar la contingencia en papel mientras tanto?

## 4. Cierre

11. Si mañana el sistema solo pudiera hacer una cosa, ¿cuál sería?
12. ¿Qué no le preguntamos que debimos preguntar?

## Después

- La minuta se escribe el mismo día con `plantilla-minuta.md` y se envía al cliente para que la confirme por
  escrito. Plazo: 24 horas después de la entrevista.
- Ruta final: `docs/minutas/AAAA-MM-DD-entrevista-cliente.md`.
- Cada respuesta que cambie una regla o una historia abre su issue.
