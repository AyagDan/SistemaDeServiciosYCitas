# Reglas de negocio y protección de datos personales

Oct 22, 2026 Florentino Ruiz Aquino

## 1. Reglas de negocio y requisitos de dominio

**Qué son.** Una regla de negocio es una política o condición del negocio del cliente. Existe aunque no haya software: hoy se cumple en papel, de palabra o "a ojo", y el sistema tiene que respetarla. No describe una función del sistema, sino una restricción sobre cómo deben funcionar las funciones.

**Cómo se distingue de un requisito funcional:**

* **Requisito funcional:** "El sistema deberá permitir registrar la autorización de una cotización".
* **Regla de negocio:** "Ninguna reparación inicia sin autorización del cliente". Esta regla es la que obliga a que exista el requisito funcional y a que el sistema impida avanzar sin la autorización.

**Ejemplos de los proyectos:**

| Equipo A · Cooperativa | Equipo B · Taller |
| --- | --- |
| Un cliente que supera su límite de crédito no recibe un nuevo pedido a crédito sin autorización | Una cotización vence a los 5 días |
| A la socia solo se le pagan los paquetes aceptados; los rechazados por calidad no se pagan | Si un trabajo adicional sube el costo más de 10%, se requiere nueva autorización |
| Los pedidos se hacen con al menos 24 h de anticipación | Una bahía no puede tener dos vehículos en reparación a la vez |

**Por qué son importantes.** Una regla de negocio se refleja en todo el proyecto:

* **SRS:** en los requisitos funcionales que la implementan.
* **Diagramas de estados:** en las transiciones permitidas y prohibidas.
* **Pruebas:** en los casos de prueba de valores límite, como una cotización con 5 días frente a una con 6.
* **Código:** en las validaciones.

Una regla que falta o está mal entendida produce un sistema que "funciona" pero que el cliente no puede usar.

**Cómo se documenta.** Cada regla lleva un ID (RN-01), su enunciado, su fuente (anteproyecto o entrevista con fecha) y los requisitos que afecta.

**Errores típicos:**

* Copiar solo las reglas del anteproyecto. Ambos clientes tienen reglas que solo aparecen si se pregunta.
* No preguntar por las excepciones: ¿quién puede autorizar que se rompa la regla y queda registro de ello?
* Mezclar reglas con funciones de pantalla.

## 2. Requisitos de protección de datos personales

**Por qué aplican.** Los dos sistemas guardan datos de personas identificables. En México esto lo regula la **Ley Federal de Protección de Datos Personales en Posesión de los Particulares**. La versión nueva se publicó en el DOF el 20 de marzo de 2025 y entró en vigor al día siguiente. Las funciones del INAI en esta materia pasaron a la Secretaría Anticorrupción y Buen Gobierno.

**Qué datos personales hay en cada proyecto:**

* **Equipo A:** nombre, teléfono y dirección de clientes; datos de las socias y lo que se les paga; nombre o foto de quien recibe una entrega.
* **Equipo B:** nombre, teléfono y correo de clientes; placas y VIN ligados a una persona; fotos del vehículo; registro de quién autorizó y cuándo.

**Qué deben especificar los equipos (sección 4.8 del machote):**

1. **Inventario y finalidad:** qué dato se recaba y para qué. Si no tiene una finalidad clara, no se pide (principio de proporcionalidad).
2. **Aviso de privacidad:** un borrador que diga quién es el responsable, qué datos se recaban, para qué y cómo ejercer los derechos.
3. **Derechos ARCO:** acceso, rectificación, cancelación y oposición. El sistema debe permitir que el negocio consulte, corrija o dé de baja los datos de una persona.
4. **Control de acceso por rol:** cada quien ve solo lo suyo. Una socia no debe ver los saldos de los clientes, y un cliente del taller no debe poder abrir la orden de otro cambiando el número en la URL.
5. **Medidas de seguridad:** contraseñas cifradas, conexión HTTPS, respaldos y registro de quién modificó qué.
6. **Datos de prueba:** siempre ficticios. Nunca datos reales en el repositorio ni en herramientas de IA.

**Cómo se conecta con lo técnico.** El punto 4 corresponde al riesgo número uno del OWASP Top 10:2025, el control de acceso roto. Por eso aparece en el banco de verificaciones del cliente del manual del profesor. Cada requisito de datos personales debe tener al menos un caso de prueba, por ejemplo: "entrar con rol mecánico e intentar cambiar el precio de una cotización".

**Error típico:** escribir "el sistema será seguro". Igual que con cualquier requisito no funcional, debe ser verificable: "solo el rol Administradora puede consultar el saldo de un cliente".

Para la clase basta con que identifiquen los datos, las finalidades, el aviso y las medidas, sin exigir un análisis jurídico. Este material no es asesoría legal; para profundizar, conviene revisar el texto de la ley en el sitio de la Cámara de Diputados.

## Fuentes

* [<u>Ley Federal de Protección de Datos Personales en Posesión de los Particulares (DOF 20-03-2025)</u>](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)
* [<u>EY: Entrada en vigor de la nueva LFPDPPP</u>](https://www.ey.com/es_mx/technical/tax/boletines-fiscales/nueva-ley-federal-proteccion-datos-personal-posesion-particulares)
* [<u>OWASP Top 10:2025</u>](https://owasp.org/Top10/2025/)