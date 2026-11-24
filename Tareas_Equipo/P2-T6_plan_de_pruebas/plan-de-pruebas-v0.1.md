# P2-T6 · Plan de pruebas v0.1

| Dato | Valor |
| --- | --- |
| Tarea | P2-T6 (guía del segundo parcial) |
| Responsable | QA Lead (Dulce María Estudillo Rosado) |
| Versión | 0.1 |
| Referencia | ISO/IEC/IEEE 29119-3:2021 (plan de pruebas) y 29119-4:2021 (técnicas de caja negra) |
| Producto | Sistema de Órdenes de Servicio y Citas, Release v0.1.0 |

## 1. Alcance

Se prueba el flujo núcleo propuesto para el Release v0.1.0 (`docs/04-requisitos/propuesta-release-v0.1.0.md`):
recepción, diagnóstico y asignación, cotización y autorización, más las reglas que lo rodean (roles, privacidad
y entrega con saldo).

Queda fuera: operación sin conexión (HU-25, HU-26), citas en línea, refacciones y reportes gerenciales, que la
propuesta pasa a la Fase 2. Si el cliente cambia el corte, este alcance se ajusta.

## 2. Supuestos y restricciones

- Se prueba sobre el backend de `backend/` con su base de datos de prueba.
- Solo se usan datos ficticios (LFPDPPP, RNF-05). Los correos son de `ejemplo.com` y las placas empiezan con `TST`.
- No hay presupuesto: se usan herramientas gratuitas (pytest, navegador, Swagger de FastAPI).
- El reloj del sistema se controla en las pruebas (`backend/app/reloj.py`) para probar plazos sin esperar días.

## 3. Riesgos del plan

| Riesgo | Efecto en el plan | Qué se hace |
| --- | --- | --- |
| Un criterio de aceptación sigue siendo ambiguo (B9) | No se puede escribir el resultado esperado | Se registra como incidencia `tipo:defecto-doc` antes de ejecutar |
| El cliente cambia el corte del release | Cambia el alcance de la sección 1 | Se actualiza el plan en la misma rama del cambio |
| Varias historias comparten el mismo ID de caso (CPA-02, CPA-03, CPA-10, CPA-31) | No se sabe qué caso prueba qué historia | Se corrige la numeración en el SRS (ver P2-T4) |

## 4. Estrategia

| Nivel | Qué se prueba | Cómo |
| --- | --- | --- |
| Unitario | Reglas de negocio en `backend/app/servicios/` | pytest, automatizado |
| Integración | Rutas de la API con la base de datos | pytest con el cliente de pruebas de FastAPI |
| Aceptación | Criterios de las historias Must | Casos de esta sección, manuales y después automatizados |

Técnicas de caja negra (29119-4): partición de equivalencia y análisis de valores límite. Cada regla con umbral
se prueba a los dos lados del límite.

## 5. Criterios de entrada y salida

- **Entrada:** la historia tiene sus criterios en formato Dado / Cuando / Entonces y el ambiente levanta sin errores.
- **Salida:** 100 % de los casos de historias Must ejecutados, cero incidencias S1 abiertas y las S2 con una
  decisión del Product Owner.

## 6. Suspensión y reanudación

Se suspende si el ambiente no levanta o si una incidencia S1 bloquea el flujo núcleo. Se reanuda cuando la
corrección está integrada en `main` y quien la reportó la verificó.

## 7. Ambiente y datos

- Python 3 con las dependencias de `backend/requirements.txt`; `pytest` desde la carpeta `backend/`.
- Datos semilla de `backend/app/semilla.py` más los datos ficticios de cada caso.

## 8. Roles y calendario

| Rol | Persona | Qué hace |
| --- | --- | --- |
| QA Lead | Dulce María Estudillo Rosado | Mantiene el plan, asigna casos y revisa los reportes |
| Tester | Isis Alhelí González Maldonado | Casos de recepción y asignación (CPA-35, CPA-36, CPA-44 a CPA-48) |
| Tester | Isis Yamilet Meléndez Hernández | Casos de cotización, autorización y entrega (CPA-37 a CPA-43, CPA-49, CPA-50) |
| Product Owner | Ángel Yael Avendaño Guzmán | Decide la prioridad de las incidencias |

Calendario: se ejecutan en el sprint en que se construye cada historia, con las fechas de la sección 2.3 del
Documento de Ingeniería.

## 9. Entregables

Casos de prueba (sección 10), registro de ejecución (`docs/pruebas/resultado-pruebas.txt`), incidencias en
GitHub e informe de cierre al final del release.

## 10. Casos de prueba de caja negra

Los casos siguen la numeración de la sección 4.5 del Documento de Ingeniería, que llega hasta CPA-34. Cada par
prueba los dos lados de un mismo límite.

| ID | Regla y técnica | Precondiciones y datos | Pasos | Resultado esperado | Trazabilidad |
| --- | --- | --- | --- | --- | --- |
| CPA-35 | RN-12 · límite inferior inválido | Recepción de la placa TST-001-A con checklist completo y 3 fotografías (frente, trasera, izquierda) | Confirmar la recepción | No se confirma; el sistema indica que falta la fotografía del costado derecho y la orden no se abre | RF-04, HU-01 |
| CPA-36 | RN-12 · límite válido | Mismo vehículo, con las 4 fotografías | Confirmar la recepción | Se abre la orden en estado «Abierta» con folio y fecha y hora de recepción | RF-04, HU-01 |
| CPA-37 | RN-04 · límite exacto | Orden en reparación con cotización autorizada de $10,000.00; nueva cotización de $11,000.00 (10 % exacto) | Emitir la nueva cotización | El trabajo no se detiene; la cotización queda «Autorizada» | RF-07, HU-16 |
| CPA-38 | RN-04 · justo arriba del límite | Misma orden; nueva cotización de $11,000.01 | Emitir la nueva cotización | La orden pasa a «EsperandoAutorizacionAdicional» y se pide código al cliente | RF-07, HU-16 |
| CPA-39 | RN-11 · último día válido | Cotización emitida el lunes 02/11/2026 (vence el 07/11/2026); reloj en 07/11/2026 | El cliente abre el enlace y aprueba | Se permite aprobar | RF-06, HU-12 |
| CPA-40 | RN-11 · primer día vencido | Misma cotización; reloj en 08/11/2026 | El cliente abre el enlace | La cotización aparece «Vencida» y no hay botón de aprobar | RF-06, HU-12 |
| CPA-41 | RN-02 · dentro del plazo | Código enviado a las 10:00:00 | Capturar el código correcto a las 10:04:59 | Autorización «Confirmada» | RF-06, HU-14 |
| CPA-42 | RN-02 · fuera del plazo | Código enviado a las 10:00:00 | Capturar el código correcto a las 10:05:01 | Mensaje «El código expiró (5 minutos); solicita uno nuevo»; no se autoriza | RF-06, HU-14 |
| CPA-43 | RN-02 · partición inválida | Código vigente de 6 dígitos | Capturar 5 dígitos (`12345`) | No se autoriza y se avisa que el código no es válido | RF-06, HU-14 |
| CPA-44 | RN-05 · última bahía libre | Bahías 1, 2 y 3 ocupadas; bahía 4 libre | Asignar una orden nueva | Se asigna a la bahía 4 | RF-05, HU-08 |
| CPA-45 | RN-05 · sin bahías | Las 4 bahías ocupadas | Intentar asignar una orden nueva | Alerta «Sin bahías disponibles»; la orden queda «EnEsperaDeBahia» | RF-05, HU-07 |
| CPA-46 | Kilometraje · partición inválida | Recepción con kilometraje `-1` | Guardar la recepción | Se rechaza el dato y no se guarda | RF-04, HU-01 |
| CPA-47 | Kilometraje · límite válido | Recepción con kilometraje `0` (vehículo nuevo) | Guardar la recepción | Se guarda | RF-04, HU-01 |
| CPA-48 | RN-07 · particiones del tipo de vehículo | Alta de un vehículo | Abrir el selector de tipo | Solo aparecen Automóvil, Motocicleta y Camioneta | RF-03.1, HU-06 |
| CPA-49 | RN-10 · saldo mínimo pendiente | Orden de un cliente particular con saldo de $0.01 | Registrar la entrega | Se bloquea la entrega y se muestra el saldo | RF-10, HU-21 |
| CPA-50 | RN-10 · saldo en cero | Misma orden con saldo de $0.00 | Registrar la entrega | Se registra la entrega y se cierra la orden | RF-10, HU-21, HU-23 |

Son 16 casos: la tarea pide al menos 10. Los pares CPA-49 y CPA-50 son de historias que la propuesta pasa a la
Fase 2; se dejan escritos para cuando se construyan.
