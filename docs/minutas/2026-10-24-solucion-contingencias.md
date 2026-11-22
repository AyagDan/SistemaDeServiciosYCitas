# Minuta · Reunión del equipo: soluciones a las dudas del cliente

| Dato | Valor |
|---|---|
| Fecha | Sábado 24 de octubre de 2026 |
| Hora y modalidad | Pendiente |
| Asistentes | Pendiente |
| Elaboró | Developer SRS (Isis Alhelí González Maldonado) |
| Objetivo | Definir la solución a las dudas D-1 y D-2 del cliente ([minuta del 23/10/2026](2026-10-23-sesion-cliente-propuestas.md)) |

## 1. Decisiones

### 1.1 Cortes de luz prolongados (D-1)

Si el corte dura más de lo que aguantan los equipos, el taller regresa a su forma de trabajo previa: el
registro en papel, que después se captura manualmente en el sistema. Se organiza en tres niveles:

1. **Sin internet:** la PWA sigue trabajando sin conexión y sincroniza al volver la conexión.
2. **Sin luz:** igual que el nivel 1, con los equipos en batería.
3. **Contingencia en papel:** cuando el corte supera 4 horas o la batería baja del 20 %, el gerente la
   declara y todo se registra en la Bitácora de Contingencia impresa, con folios provisionales
   `C-AAAAMMDD-NN` y la firma autógrafa del cliente como única autorización válida. Al restablecerse el
   servicio, todo se captura en el sistema en las 24 horas siguientes.

### 1.2 Nivel de gasolina al entrar a servicio (D-2)

Si el medidor de combustible del tablero no funciona, la recepcionista usa el primer método disponible y
anota cuál usó:

1. **Escáner OBD-II:** lee el nivel del tanque en porcentaje y lo convierte a los 5 niveles del selector.
2. **Computadora de viaje:** autonomía restante en kilómetros, como referencia.
3. **Bomba de trasvase:** solo si la reparación implica bajar o vaciar el tanque (bomba de gasolina, sensor
   de nivel, fugas). El combustible se pasa a bidones graduados, se registran los litros y ese mismo volumen
   se regresa al tanque. No se abre el sistema de combustible solo para medir, por el riesgo de incendio.
4. **Declaración del cliente:** si nada de lo anterior es posible, con la leyenda «Declarado por el
   cliente, no verificable».

En todos los casos se fotografía el tablero, el nivel queda como «No verificable» con el método usado y el
cliente lo acepta con su firma. Al entregar, el nivel se mide con el mismo método.

## 2. Acuerdos

| # | Acuerdo | Responsable | Fecha |
|---|---|---|---|
| 1 | Registrar las soluciones como RN-14, RN-15 y los procedimientos de contingencia de 4.7.1. | Developer SRS | Pendiente |
| 2 | Presentar las soluciones al cliente. | Product Owner | 09/11/2026 ([minuta](2026-11-09-sesion-cliente-soluciones.md)) |
