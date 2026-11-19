# Minuta · Sesión con el cliente: alcance del Release v0.1.0 y procedimientos de contingencia

| Dato | Valor |
|---|---|
| Observaciones que atiende | B2 de la Review 1, negociación (issue #29), y B10 (issue #81) |
| Objetivo | Que el cliente decida el alcance del Release v0.1.0 y el estado de los procedimientos de contingencia de 4.7.1 |
| Conduce | Product Owner (Ángel Yael Avendaño Guzmán) |
| Material | `docs/04-requisitos/propuesta-release-v0.1.0.md` y la sección 4.7.1 del Documento de Ingeniería |
| Fecha límite | Viernes 20 de noviembre de 2026 |
| Fecha, hora y modalidad | Pendiente: se registra al realizar la sesión |
| Asistentes | Pendiente: se registran al realizar la sesión |

Las secciones 3.3, 3.6, 4.5, 4.7.1 y el story map no cambian hasta que el cliente decida y su decisión
conste en esta minuta.

## 1. Alcance del Release v0.1.0 (B2)

Se presenta la propuesta: el Release v0.1.0 pasa de 25 historias (92 puntos) a 11 historias (40 puntos)
del flujo núcleo del anteproyecto (recepción, diagnóstico y asignación, cotización y autorización). Las
otras 14 historias pasan a la Fase 2, especificadas y diseñadas, pero sin construirse.

Decisión del cliente sobre la propuesta en general: Pendiente.

### 1.1 Monitoreo gerencial

El anteproyecto incluye en el flujo núcleo un panel del gerente con las órdenes abiertas, su estado y la
carga del taller. Las historias más cercanas (HU-11 y HU-29) están en la Fase 2.

Pregunta: ¿quiere en v0.1.0 una vista mínima de órdenes abiertas y su estado, o el panel completo puede
esperar a la Fase 2?

Decisión del cliente: Pendiente.

### 1.2 Cobro y cierre de la orden

Sin HU-21 y HU-23 (6 puntos), la orden no se cobra ni se cierra dentro del sistema en v0.1.0.

Pregunta: ¿acepta cerrar las órdenes como hasta hoy durante la Fase 1?

Decisión del cliente: Pendiente.

### 1.3 Citas en línea

El producto se llama «Órdenes de Servicio y Citas», pero las citas (HU-03, HU-04 y HU-06) no están en el
flujo núcleo del anteproyecto.

Pregunta: ¿acepta que queden diseñadas y se construyan en la Fase 2?

Decisión del cliente: Pendiente.

### 1.4 Operación sin conexión

La operación sin conexión (HU-25 y HU-26, 16 puntos) es el mayor riesgo técnico del proyecto (R-02).

Pregunta: ¿acepta operar con conexión en v0.1.0, con los procedimientos de contingencia de 4.7.1 mientras
tanto?

Decisión del cliente: Pendiente.

## 2. Procedimientos de contingencia de 4.7.1 (B10)

Son una propuesta del equipo que detalla RN-14 y RN-15. Para cada uno, el cliente decide si lo acepta
(queda en el SRS), lo pasa a la Fase 2 o lo rechaza (se retira del SRS).

### 2.1 Vehículo con el medidor de combustible descompuesto (RN-14, parte A)

Cuando el indicador del tablero no funciona, la recepcionista usa el primer método disponible y anota cuál
usó:

1. Lectura del nivel del tanque con el escáner OBD-II del taller.
2. Autonomía restante que muestra la computadora de viaje.
3. Medición en litros con la bomba de trasvase, solo si la reparación implica vaciar el tanque.
4. Nivel que declara el cliente, con la leyenda «Declarado por el cliente, no verificable».

En el sistema, el selector de combustible de la recepción gana la opción «No verificable», con el método,
el valor obtenido y una fotografía del tablero.

Decisión del cliente: Pendiente.

### 2.2 Cortes prolongados de luz o de internet (RN-15, parte B)

Tres niveles: sin internet, sin luz (con batería) y contingencia en papel. La contingencia en papel se
declara cuando el corte supera 4 horas o la batería de los equipos baja del 20 %. Se usa la Bitácora de
Contingencia impresa, con folios provisionales `C-AAAAMMDD-NN`, autorización solo con firma autógrafa del
cliente y recibos provisionales en efectivo. Al restablecerse el servicio, todo se captura en el sistema en
las 24 horas siguientes.

Decisión del cliente: Pendiente.

Preguntas de detalle, si el cliente acepta el procedimiento:

- ¿El umbral de 4 horas para pasar a papel es adecuado? Decisión del cliente: Pendiente.
- ¿El plazo de 24 horas para capturar en el sistema lo registrado en papel es adecuado? Decisión del
  cliente: Pendiente.

## 3. Acuerdos

Pendiente: se registran al realizar la sesión.

| # | Acuerdo | Responsable | Fecha |
|---|---|---|---|
| — | Pendiente | Pendiente | Pendiente |

## 4. Cambios que se harán en el documento según las decisiones

Se hacen después de la sesión, solo con lo que el cliente haya aceptado:

- **B2:** el alcance del Release v0.1.0 en 3.3, las restricciones de 3.6, el release de cada historia en
  4.5 y el story map (Figura 4.1).
- **B10:** los procedimientos aceptados se quedan en 4.7.1 y RN-14 y RN-15 dejan de decir «Propuesta del
  equipo; validar con el cliente». Los que pasen a la Fase 2 o se rechacen se mueven o se retiran del SRS.

Firma de conformidad del cliente: Pendiente.
