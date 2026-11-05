<!-- converted from IS1-Fase1-EquipoB-v0.1.docx -->

Índice

Universidad del Istmo · Campus Ixtepec
Ingeniería en Desarrollo de Software y Sistemas Inteligentes
Ingeniería de Software I (IDSSI-27) · Quinto semestre
Documento de Ingeniería del Proyecto – Fase 1
Sistema de Órdenes de Servicio y Citas
Servicio Automotriz Hermanos Ruiz, S.A. de C.V.
| Equipo: | B (5 integrantes) |
| --- | --- |
| Cliente: | Servicio Automotriz Hermanos Ruiz |
| Producto: | Sistema de Órdenes de Servicio y Citas |
| Versión del documento: | v0.1 |
| Fecha: | 29/10/2026 |
| Repositorio: | https://github.com/AbdiasChavez/Florentino |
# 1. Información general del proyecto
## 1.1 Integrantes y roles
| Nombre completo | Matrícula | Usuario GitHub | Rol(es) y sprints | Áreas principales de contribución |
| --- | --- | --- | --- | --- |
| Ángel Yael Avendaño Guzmán | 0224170023 | AyagDan | Product Owner (S0–S6) | Enlace con el cliente, levantamiento de requerimientos en entrevistas, priorización del Product Backlog y aceptación de entregables. |
| Abdías Daniel Chávez Cruz | 0224170024 | absdan | Scrum Master / Tech Lead (S0–S6) | Facilitación de Scrum, arquitectura del backend en FastAPI, diseño de la base de datos relacional y gestión técnica de Pull Requests. |
| Dulce María Estudillo Rosado | 0224170028 | DulceRosado | QA Lead / Developer (S0–S6) | Diseño del plan de pruebas, ejecución de casos de aceptación, validación de calidad y realización del QA cruzado al otro equipo. |
| Isis Alhelí González Maldonado | 0224170030 | IsisAlheliGonzalezMaldonado | Developer (S0–S6) | Redacción de la especificación de requisitos de software (SRS), historias de usuario y modelado de procesos del negocio. |
| Isis Yamilet Meléndez Hernández | 0224170037 | IsisMelendezHernandez | Developer (S0–S6): especialista en interfaz, datos y documentación | Integración y compilación del Documento de Ingeniería (migración a LaTeX/Word), configuración de flujos de CI en GitHub Actions, despliegue y apoyo en el desarrollo de los componentes de la interfaz (PWA). |
## 1.2 Enlaces del proyecto
| Recurso | Enlace |
| --- | --- |
| Repositorio | https://github.com/AbdiasChavez/Florentino (original: https://github.com/AyagDan/SistemaDeServiciosYCitas) |
| Integración continua | https://github.com/AbdiasChavez/Florentino/actions |
| Tablero (GitHub Projects / Jira) | Pendiente |
| Prototipo de UI (Figma / Penpot) | Pendiente |
| Ambiente de pruebas (staging) | Pendiente |
| Release v0.1.0 | Pendiente |
| Canal de comunicación del equipo | Grupo de WhatsApp del equipo (mensajes y llamadas); reuniones presenciales en la escuela. |
## 1.3 Resumen ejecutivo
Servicio Automotriz Hermanos Ruiz opera hoy con cuadernos, órdenes en papel y llamadas. Esto provoca disputas por cobros que el cliente dice no haber autorizado, reclamos por daños sin evidencia del estado en que llegó el vehículo, muchas llamadas para preguntar por el avance y poca visibilidad de qué vehículo ocupa cada una de las 4 bahías.
El Sistema de Órdenes de Servicio y Citas digitaliza el ciclo de atención: la cita, la recepción del vehículo con checklist y fotografías, el diagnóstico y la asignación de bahía, la cotización que el cliente autoriza desde su celular con un código de verificación, y el cobro y la entrega. El cliente consulta el estado de su vehículo con un enlace seguro, sin instalar aplicaciones.
Estado actual (v0.1): se levantaron los requisitos con el cliente (entrevista del 19/10/2026) y se definió el alcance. Ya funciona, en una versión de desarrollo sin pantallas todavía, el corazón del sistema: abrir una orden con checklist y fotografías, asignar bahía y mecánico, registrar el diagnóstico, enviar la cotización al cliente, autorizarla con el código de verificación, cobrar y entregar sin saldo pendiente. Cada una de estas reglas se comprueba automáticamente con 35 pruebas. Falta: las pantallas para el personal y para el cliente, el envío real de correos, la operación sin internet, el almacén y el ambiente de pruebas en línea. La Fase 2 agregará reportes gerenciales, consulta de existencias y de garantías, y el tablero simplificado de bahías.
# 2. Gestión del proyecto con Scrum
## 2.1 Acuerdos de trabajo
Los acuerdos completos están en CONTRIBUTING.md del repositorio. En resumen:
• Comunicación: grupo de WhatsApp del equipo para lo urgente y GitHub (issues y Pull Requests) para todo lo técnico. Tiempo máximo de respuesta: 24 horas en días hábiles.
• Reuniones: se hacen de manera presencial o por llamada en el grupo de WhatsApp: Daily breve de lunes a viernes y los eventos de Scrum al inicio y al cierre de cada sprint de dos semanas. Lo que se decide en una reunión se registra en GitHub (issue, minuta o documento).
• Decisiones: por consenso; si no se logra, decide el Product Owner en temas de alcance y prioridad, y el Scrum Master en temas de proceso.
• Ramas: main está protegida; hay una rama por rol de Scrum (rol/product-owner, rol/scrum-master, rol/qa-lead, rol/developers) y cada rol integra a main con un merge que deja visible su rama, mediante Pull Request con al menos una revisión de otro integrante. Las ramas personales anteriores (rama/<NOMBRE>) quedan en el historial.
• Commits: en español y en presente, con el formato «Rol: mensaje» y referencia a la historia cuando aplique (por ejemplo, «Developers: implementa recepción con checklist (HU-01)»).
• Documentos: el Documento de Ingeniería se escribe en LaTeX, un archivo por sección en docs/documento/secciones/, para que git pueda fusionar los cambios de varios roles. El entregable se publica en docs/entregas/ en PDF y en Word (.docx) con el nombre IS1-Fase1-EquipoB-v<versión> (por ejemplo, IS1-Fase1-EquipoB-v0.1.pdf).
• Incumplimiento: se registra en la retrospectiva; a la segunda falta en el mismo sprint, el Scrum Master lo informa al profesor.
## 2.2 Definición de Listo (DoR) y Definición de Terminado (DoD)
| Definición de Listo | Definición de Terminado |
| --- | --- |
| • La historia sigue el formato Como… quiero… para… y tiene ID e issue en el tablero. • Tiene al menos 2 criterios de aceptación en formato Dado/Cuando/Entonces. • El equipo la estimó en puntos y cabe en un sprint (8 puntos o menos). • Sus reglas de negocio (RN) y requisitos (RF/RNF) relacionados están identificados. • Sus dependencias (otras historias, datos, wireframe) están resueltas o planificadas. • El Product Owner la priorizó (MoSCoW). | • El código está en main mediante un Pull Request revisado por otro integrante. • Cumple todos sus criterios de aceptación y el Product Owner lo verificó. • Tiene pruebas automatizadas y la integración continua pasa sin errores. • Se probó solo con datos ficticios; no hay datos personales reales ni contraseñas en el repositorio. • La documentación afectada (SRS, modelos, README) está actualizada. • Está desplegada en el ambiente de pruebas (desde el Sprint 4). |
## 2.3 Resumen de sprints
| Sprint | Fechas | Objetivo del sprint | ¿Se cumplió? (sí / parcial / no) | Puntos comprometidos | Puntos terminados |
| --- | --- | --- | --- | --- | --- |
| S0 | Pendiente | Conocer al cliente, levantar los requisitos iniciales y preparar el repositorio y el documento base. | Sí | Pendiente | Pendiente |
| S1 | Pendiente | SRS en borrador (4.1–4.7) y validación con el cliente. | Parcial: falta validar con el cliente (4.11) | Pendiente | Pendiente |
| S2 | Pendiente | SRS completo, plan de pruebas y backend del flujo núcleo (recepción, diagnóstico, cotización y autorización 2FA). | Parcial: backend y pruebas listos; falta firma del SRS | Pendiente | Pendiente |
| S3 | Pendiente | Modelos de análisis (6) y arquitectura (7.1–7.5). | Parcial: falta generar las figuras | Pendiente | Pendiente |
| S4 | Planeado | Ambiente de pruebas, PWA del personal, almacén y operación sin conexión. | — | Pendiente | — |
| S5 | Planeado | Portal del cliente, accesibilidad, prueba con usuarios y SUS. | — | Pendiente | — |
| S6 | Planeado | Release v0.1.0, QA cruzado y transferencia a Fase 2. | — | Pendiente | — |
### Evidencia de los eventos
| Sprint | Minuta de Review | Retrospectiva | Acciones de mejora acordadas | ¿Se aplicaron? |
| --- | --- | --- | --- | --- |
| S0 | Pendiente | Pendiente | — | — |
## 2.4 Registro de riesgos
| ID | Riesgo | Probabilidad | Impacto | Respuesta y responsable | Estado |
| --- | --- | --- | --- | --- | --- |
| R-01 | Un integrante abandona el curso a mitad del semestre | Media | Alto | Mitigar: conocimiento compartido mediante revisión cruzada de PR; responsable: SM | Abierto |
| R-02 | La operación sin conexión y la sincronización posterior (RNF-08, RNF-09) resultan más complejas de lo estimado | Alta | Alto | Mitigar: prototipo técnico en el Sprint 1 y limitar lo offline a recepción y diagnóstico; responsable: equipo de desarrollo | Abierto |
| R-03 | El cliente no está disponible para validar requisitos o asistir a las Reviews | Media | Alto | Mitigar: agendar sesiones con anticipación y validar por correo cuando no pueda asistir; responsable: PO | Abierto |
| R-04 | Cambios de alcance frecuentes por parte del cliente | Media | Medio | Mitigar: registrar cada solicitud de cambio (2.5) con análisis de impacto; responsable: PO | Abierto |
| R-05 | El servicio gratuito de correo limita el envío de enlaces y códigos 2FA | Media | Alto | Mitigar: probar los límites del plan gratuito en el Sprint 1 y dejar SMS como opción (RF-02.3); responsable: equipo de desarrollo | Abierto |
| R-06 | Las fotografías de recepción saturan el almacenamiento del hospedaje gratuito | Media | Medio | Mitigar: comprimir las imágenes en el dispositivo y fijar un tamaño máximo por foto; responsable: equipo de desarrollo | Abierto |
| R-07 | Poca experiencia del equipo con FastAPI y PWA | Alta | Medio | Mitigar: capacitación en S0–S1 y trabajo en pares en las primeras historias; responsable: SM | Abierto |
| R-08 | Conflictos al editar en paralelo el documento .docx en ramas distintas | Alta | Medio | Evitar: el documento se migró a LaTeX con un archivo por sección; responsable: SM | Cerrado |
| R-09 | Se publican datos personales reales en el repositorio público | Media | Alto | Evitar: solo datos ficticios y revisión de datos personales en cada PR; .gitignore excluye .env y credenciales; responsable: todos | Abierto |
| R-10 | Código o texto generado con IA que el equipo no entiende o no revisó | Media | Alto | Mitigar: declarar el uso en 2.6, revisión de cada PR por otro integrante y pruebas automatizadas como evidencia; responsable: SM | Abierto |
| R-11 | Diferencias entre SQLite (pruebas) y PostgreSQL (staging) ocultan defectos | Media | Medio | Mitigar: la CI carga db/schema.sql en PostgreSQL 16; agregar pruebas de integración contra PostgreSQL en S4; responsable: QA Lead | Abierto |
| R-12 | Sin ambiente de pruebas no se puede mostrar el flujo núcleo al cliente | Media | Alto | Mitigar: decidir ADR-004 antes del Sprint 4; responsable: Developers | Abierto |
## 2.5 Solicitudes de cambio
| ID / issue | Fecha | Solicitud del cliente | Impacto (requisitos, modelos, pruebas, esfuerzo) | Decisión y justificación | Release |
| --- | --- | --- | --- | --- | --- |
| — | — | No se han recibido solicitudes de cambio del cliente a la fecha. | — | — | — |
## 2.6 Declaración de uso de inteligencia artificial
| Herramienta | Sección o artefacto | Para qué se usó | Cómo se verificó | Responsable |
| --- | --- | --- | --- | --- |
| Claude (Anthropic), mediante Claude Code | Revisión de consistencia del documento v0.1; borradores de 1.3, 2.1–2.4, 3.1–3.3, 3.6, 4.1 y 4.2; correcciones de trazabilidad en 4.4–4.9; esquema de base de datos (db/schema.sql). | Detectar inconsistencias y proponer redacción a partir del anteproyecto, la entrevista del 19/10/2026 y el diagrama de clases v4. | Revisión del Scrum Master / Tech Lead contra las fuentes y revisión de otro integrante en el Pull Request. | Abdías Daniel Chávez Cruz |
| Claude (Anthropic), mediante Claude Code | Migración del documento a LaTeX; backend FastAPI (backend/app); 35 pruebas automatizadas; CI; secciones 5, 6, 7, 9 y 10.1; actualizaciones de 1, 2 y 4; fuentes PlantUML de estados y actividades; Avances.txt. | Generar código, pruebas y borradores a partir del SRS, las reglas de negocio, el diagrama de clases v4 y db/schema.sql. | Las 35 pruebas pasan en local y en CI; el documento compila; cada rol revisa el código y el texto de su sección antes de la entrega. | Abdías Daniel Chávez Cruz |
| Por declarar | Secciones redactadas antes de la v0.1 y Propuesta de Solución Tecnológica | Cada autor declara la herramienta que usó o que no usó IA. | — | Cada integrante |
# 3. Visión y viabilidad del producto
## 3.1 Problema y contexto del cliente
Servicio Automotriz Hermanos Ruiz, S.A. de C.V. es un taller que atiende vehículos ligeros (automóviles particulares, motocicletas y camionetas) de clientes particulares y de pequeñas flotillas empresariales. Tiene 4 bahías de trabajo y un estacionamiento para 5 vehículos en espera. Hoy las citas se apuntan en un cuaderno, las órdenes se llenan en papel y la comunicación con el cliente es por teléfono o WhatsApp (ver el proceso actual en 3.5).
Según el anteproyecto y la entrevista con el cliente del 19/10/2026, los problemas principales son:
• Disputas por cobros: las autorizaciones son verbales o por mensaje y no queda registro de qué se aprobó ni por cuánto («dijo que sí, pero cobra otra cosa»).
• Reclamos por daños: no hay checklist ni fotografías del estado en que llega el vehículo.
• Exceso de llamadas: el cliente llama para saber el avance y la recepcionista interrumpe su trabajo para averiguarlo.
• Poca visibilidad: la carga de trabajo y las bahías se asignan de palabra, y hay vehículos detenidos sin justificación.
• Historial disperso: las órdenes se archivan en carpetas y es difícil consultar reparaciones y garantías anteriores.
Hallazgos de la entrevista que no estaban en el anteproyecto:
• El cliente quiere una doble verificación con código de 6 dígitos al autorizar cotizaciones, en forma remota o presencial (RN-02).
• El cliente puede aprobar o rechazar por separado los conceptos opcionales de una cotización (RN-03).
• Si una refacción tarda varios días, el vehículo pasa al estacionamiento para liberar la bahía (RN-06).
• Las citas pedidas en línea no apartan lugar hasta que la recepcionista las confirma (RN-08).
• Varios mecánicos pueden colaborar en una orden, pero siempre hay un responsable (RN-09).
Además, hay cortes de luz e internet, por lo que el personal necesita seguir capturando sin conexión, y el jefe de mecánicos trabajará con 1 o 2 tabletas en un ambiente con ruido, polvo y manos sucias (4.3).
## 3.2 Objetivos del producto e indicadores
| Objetivo | Indicador | Situación actual | Meta | Cómo se medirá |
| --- | --- | --- | --- | --- |
| Eliminar las disputas por cobros no autorizados | % de órdenes cerradas cuya cotización tiene autorización digital registrada (fecha, hora, IP y monto) | Autorizaciones verbales o por mensaje, sin registro | % de las órdenes cerradas | Reporte mensual del sistema: órdenes cerradas con autorización confirmada / total de órdenes cerradas |
| Reducir las llamadas de seguimiento a recepción | Llamadas por día de clientes que preguntan por el avance de su vehículo | Por medir: bitácora de llamadas de una semana antes de liberar el portal del cliente | Al menos 50 % menos que la medición inicial | Bitácora de llamadas de recepción, una semana antes y una semana después de la liberación |
| Contar con evidencia del estado del vehículo al recibirlo | % de recepciones con checklist completo y las 4 fotografías obligatorias | Órdenes en papel sin checklist ni fotografías | % de las recepciones | Reporte mensual del sistema de recepciones completas |
## 3.3 Alcance
| Dentro del alcance de la Fase 1 | Dentro del alcance de la Fase 2 | Fuera de alcance |
| --- | --- | --- |
| • Acceso del personal por rol (HU-27) • Citas en línea y agenda con confirmación manual (HU-03, HU-04, HU-06) • Recepción con checklist y fotografías, también sin conexión (HU-01, HU-25, HU-26) • Asignación de bahía y mecánico, y diagnóstico (HU-07 a HU-09) • Cotización desglosada y autorización del cliente con código 2FA (HU-02, HU-12 a HU-16) • Solicitud de refacciones y proveedores (HU-10, HU-17, HU-18) • Aviso de fin de trabajos, cobro, entrega y crédito a flotillas (HU-20 a HU-23) • Portal del cliente responsivo y aviso de privacidad (HU-28, HU-30) | • Búsqueda rápida de clientes y vehículos (HU-05) • Tablero simplificado de bahías para tableta (HU-11) • Consulta de existencias de refacciones (HU-19) • Consulta de garantías por el cliente (HU-24) • Panel y reportes gerenciales (HU-29, RF-11) • Envío del enlace por SMS (RF-02.3) | • Facturación electrónica (CFDI) y contabilidad • Pagos en línea con tarjeta • Aplicación móvil nativa (iOS o Android) • Vehículos pesados, tráileres y maquinaria (RN-07) • Nómina y control de asistencia del personal |
## 3.4 Stakeholders
| Stakeholder | Rol en el negocio | Interés en el sistema | Poder / interés | Estrategia de participación |
| --- | --- | --- | --- | --- |
| Dueños del taller | Propietarios; deciden la inversión y aprueban el proyecto. | Reducir disputas por cobros, cuidar la rentabilidad y la reputación, y no pagar licencias. | Alto poder – alto interés | Gestionar de cerca mediante entrevistas y revisiones de avance en cada entrega, validación de requisitos y aprobación formal del alcance. |
| Gerente | Supervisa la operación y autoriza entregas a crédito a flotillas. | Consultar tableros de control, controlar saldos y autorizar créditos con respaldo. | Alto poder – alto interés | Gestionar de cerca mediante sesiones de definición de reglas de crédito y de reportes, y pruebas de aceptación de su flujo. |
| Recepcionista | Registra ingresos, confirma citas y atiende a clientes. | Reducir llamadas de seguimiento y tener el registro de recepción y fotografías en un solo lugar. | Bajo poder – alto interés | Mantener informada e involucrada, participando en las pruebas de usabilidad, capacitación y retroalimentación continua. |
| Jefe de mecánicos | Centraliza diagnóstico, cotización y asignación de bahías en la tableta. | Flujos cortos, botones grandes y operación sin conexión. | Alto poder – alto interés | Gestionar de cerca los prototipos en el entrono real (tableta, pruebas con manos sucias) y ajustes por iteración. |
| Mecánicos de bahía y de apoyo | Realizan reparaciones, inspecciones y cubrimientos de turnos. | Recibir órdenes claras y enfocarse en el trabajo físico | Bajo poder – alto interés | Mantener informado con capacitaciones breves y un canal para reportar dificultades. |
| Encargado de almacén | Controla requisiciones, proveedores, costos e inventario de consumibles. | Directorio de proveedores, registro de costos y fechas, y tickets de compra por orden | Bajo poder – alto interés | Mantener informado e involucrado mediante entrevistas sobre su flujo de compras y pruebas del módulo M6. |
| Clientes particulares | Dueños de autos, motocicletas y vehículos. | Ver el estado de su vehículo, autorizar presupuestos y recibir un cobro transparente | Bajo poder – alto interés | Mantener informado con las pruebas de usabilidad con algunos clientes y alguna encuesta breve de satisfacción al finalizar el servicio. |
| Clientes de flotillas empresariales | Empresas con vehículos que pueden recibir entrega a crédito. | Condiciones de crédito claras y seguimiento de varios vehículos | Poder medio – interés medio | Mantener satisfechos al definir con el gerente las reglas del crédito y validar el flujo con un representante. |
| Equipo de desarrollo | Diseñan, construyen y prueban la plataforma. | Entregar un sistema que cumpla los requisitos y la norma ISO/IEC 25010 | Alto poder – alto interés | Gestionar de cerca con reuniones periódicas, control de versiones y revisiones internas de calidad. |
| Docente evaluador | Revisa el documento y el producto en curso. | Que el proyecto cumpla los criterios y entregas del curso | Alto poder – alto interés | Mantener satisfecho entregando a tiempo, pidiendo asesoría en los avances y pidiendo aclaraciones de dudas. |
## 3.5 Proceso actual (as-is)

Figura 3.1. Diagrama de actividades del proceso actual (as-is) de atención del taller, con los problemas identificados en cada etapa. Elaboración propia. Fuente: docs/03-vision/proceso-as-is.puml
El diagrama de actividades muestra el proceso actual de atención del taller antes de implementar la solución tecnológica. Se organiza en cuatro carriles (cliente, recepcionista, mecánico y registro manual) y recorre el flujo completo: solicitud de cita, recepción del vehículo, diagnóstico, cotización, autorización, reparación, entrega y archivo del historial. Los recuadros rojos señalan los problemas detectados en cada etapa, como el riesgo de errores en el registro de citas, los datos incompletos en las órdenes en papel, la información dispersa e ilegible, las demoras en la cotización manual, el exceso de llamadas y un historial difícil de consultar.
## 3.6 Estudio de viabilidad
| Tipo | Análisis y evidencia | Conclusión (viable / viable con condiciones / no viable) |
| --- | --- | --- |
| Técnica | La pila propuesta (Python con FastAPI, PostgreSQL y una PWA con Service Workers e IndexedDB) es de código abierto y está bien documentada. El mayor riesgo técnico es la operación sin conexión con sincronización posterior (RNF-08, RNF-09, R-02), que se validará con un prototipo en el Sprint 1. | Viable con condiciones: validar la sincronización sin conexión en el Sprint 1. |
| Económica | Costo de licencias de $0: todas las herramientas son de código abierto o de planes educativos (RNF-07). El taller usa las computadoras que ya tiene en recepción y almacén, y 1 o 2 tabletas para el jefe de mecánicos. Los planes gratuitos de correo y almacenamiento tienen límites (R-05, R-06). | Viable con condiciones: el taller aporta las tabletas y el sistema respeta los límites de los planes gratuitos. |
| Operativa | El personal tiene experiencia tecnológica baja a media (4.3.1). Se atiende con flujos de pocos pasos y botones grandes (RNF-02, RNF-03), capacitación breve y pruebas de usabilidad con el personal. Los dueños y el gerente apoyan el proyecto porque reduce disputas y llamadas (3.4). | Viable con condiciones: capacitar y probar con el personal antes de la Demo final. |
| Legal | Se tratan datos de identificación y contacto de los clientes (nombre, teléfono y correo) y datos de sus vehículos, incluidas fotografías; no se tratan datos sensibles. Las finalidades y medidas de seguridad (control de acceso por rol, HTTPS, tokens temporales y aviso de privacidad) están en 4.8, conforme a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (DOF 20-03-2025). En desarrollo y pruebas solo se usan datos ficticios (RNF-05). | Viable |
| De calendario | El semestre tiene 7 sprints (S0 a S6) hasta la Demo final de la semana 16. El backlog tiene 30 historias; el release v0.1.0 incluye el flujo núcleo y las historias Should o Could pueden pasar a la Fase 2 si la velocidad del equipo no alcanza. | Viable con condiciones: priorizar las historias Must. |
Conclusión general: el proyecto es viable con condiciones: validar en el Sprint 1 la operación sin conexión, que el taller aporte las tabletas, respetar los límites de los planes gratuitos y priorizar las historias Must del flujo núcleo.
# 4. Especificación de requisitos de software (SRS)
Estructura adaptada de ISO/IEC/IEEE 29148:2018. Cada requisito tiene un identificador único que se utiliza para la trazabilidad.
## 4.1 Propósito, alcance y audiencia del SRS
Propósito: este SRS describe qué debe hacer el Sistema de Órdenes de Servicio y Citas y con qué calidad, para que el cliente lo valide y lo firme en la Review 2, y para que el equipo lo use como base del diseño, la implementación y las pruebas.
Alcance: cubre el ciclo de atención del taller (citas, recepción, diagnóstico, cotización y autorización, refacciones, cobro y entrega) y el portal web del cliente, según el alcance de la sección 3.3.
Audiencia: los dueños y el gerente del taller (aprobación), el personal que usará el sistema (validación de sus flujos), el equipo de desarrollo y el docente evaluador.
Convenciones: cada requisito tiene un identificador único: RF (funcional), RNF (no funcional), RN (regla de negocio), HU (historia de usuario) y CU (caso de uso). Estos identificadores se usan en la matriz de trazabilidad (5.3).
## 4.2 Glosario del dominio
| Término | Definición | Sinónimos que usa el cliente |
| --- | --- | --- |
| Autorización | Aceptación de una cotización por el cliente; registra fecha, hora, IP, monto y el código de verificación. | Aprobación, firma digital |
| Bahía | Espacio de trabajo donde se repara un vehículo. El taller tiene 4 y cada una aloja un vehículo a la vez. | — |
| Checklist de inspección | Lista de verificación del estado de carrocería, interiores y accesorios al recibir el vehículo. | Lista de inspección |
| Cita | Solicitud para atender un vehículo en una fecha y hora; queda «Pendiente» hasta que la recepcionista la confirma. | — |
| Código 2FA | Código de 6 dígitos, de un solo uso y vigente 5 minutos, que se envía al correo del cliente para confirmar una autorización. | Código de verificación, doble verificación |
| Compra | Adquisición de refacciones a un proveedor, respaldada por un ticket. | Ticket de compra |
| Concepto | Renglón de una cotización: mano de obra, refacción o insumo. Puede ser opcional. | Rubro |
| Cotización | Costo desglosado de mano de obra, refacciones e insumos de una orden; vigente 5 días naturales. | Presupuesto |
| Diagnóstico | Descripción técnica de la falla y de las reparaciones necesarias que registra el jefe de mecánicos. | — |
| Enlace seguro | Liga web única que recibe el cliente para consultar su vehículo y autorizar cotizaciones sin usuario ni contraseña. | Token de acceso |
| Entrega a crédito | Entrega del vehículo con saldo pendiente; solo para flotillas registradas y con autorización del gerente. | Crédito |
| Flotilla | Empresa cliente con varios vehículos que puede recibir entrega a crédito. | Flotilla empresarial |
| Folio | Identificador único de una orden de servicio. | — |
| Fotografía de recepción | Evidencia digital del estado del vehículo al llegar. Son obligatorias cuatro: frente, trasera, costado izquierdo y costado derecho. | — |
| Garantía | Cobertura de 30 días sobre la mano de obra, contados desde la entrega del vehículo. | — |
| Insumo | Material consumible que se usa en la reparación, como aceite o líquidos. | Consumible |
| Jefe de mecánicos | Líder técnico: diagnostica, cotiza, asigna bahías y mecánicos y solicita refacciones desde la tableta. | Líder técnico |
| Mecánico responsable | Mecánico titular de una orden; otros mecánicos pueden colaborar sin cambiar la titularidad. | Mecánico principal |
| Orden de servicio | Registro de todo el trabajo sobre un vehículo, desde la recepción hasta la entrega. | Orden |
| Proveedor | Refaccionaria local a la que el almacén compra piezas. | Refaccionaria |
| Recepción vehicular | Registro de la llegada del vehículo: kilometraje, nivel de combustible, checklist y fotografías. | Check-in, registro de entrada |
| Re-cotización | Nueva versión de la cotización cuando los trabajos adicionales aumentan el monto más de 10 %. | — |
| Refacción | Pieza que se instala en el vehículo. | Pieza, repuesto |
| Saldo pendiente | Diferencia entre el total autorizado de la orden y lo que el cliente ha pagado. | — |
| Solicitud de refacción | Pedido de piezas que el jefe de mecánicos hace al almacén para una orden. | Requisición |
## 4.3 Descripción general
### 4.3.1 Usuarios y sus características
El sistema será utilizado por distintos perfiles dentro de la estructura operativa del negocio y la parte gerencial del taller mecánico, además de los clientes finales del negocio. La siguiente tabla detalla las características, nivel técnico y contexto de uso:
| Tipo de usuario | Tareas principales | Experiencia tecnológica | Dispositivo y contexto de uso |
| --- | --- | --- | --- |
| Recepcionista | Registro de clientes/vehículos, check-in con fotos, apertura de órdenes, confirmación de citas web, cobranza y entrega. | Media: Manejo fluido de navegación web, correo electrónico y paquetes de oficina. | Computadora de escritorio en mostrador de recepción. Entorno de oficina con teclado/mouse. |
| Jefe de Mecánicos (Líder Técnico) | Diagnóstico técnico, elaboración de cotizaciones, asignación de bahías/mecánicos, requisición de refacciones y sellado final. | Baja–Media: Familiarizado con smartphones personales; poca experiencia con sistemas de gestión. | Tabletas táctiles exclusivas de taller (1 o 2 dispositivos). Entorno con ruido, polvo y manipulación con manos sucias/grasosas. |
| Mecánico en Bahía | Ejecución de reparaciones físicas, notificación de hallazgos adicionales o solicitud de refacciones al Jefe de Mecánicos. | Baja: Uso de teléfonos inteligentes para uso personal cotidiano. | Sin dispositivo asignado directo; interactúa a través del Jefe de Mecánicos para evitar deterioro de hardware |
| Encargado de Almacén | Atender solicitudes de piezas, consultar directorio de proveedores locales, registrar compras/tickets e historial de insumos. | Baja–Media: Uso básico de computadora para consulta de inventarios. | Computadora de escritorio o terminal dedicada en el área de almacén/refacciones. |
| Gerente (Dueño) | Monitoreo del Dashboard de KPIs (ocupación, ingresos), aprobación de entregas a crédito a flotillas y excepciones. | Media: Manejo de smartphones y computadoras para administración del negocio. | Laptop personal o dispositivo móvil (smartphone/tableta) con acceso remoto/local |
| Cliente | Solicitud de citas en línea, seguimiento en vivo del servicio y aprobación/rechazo de cotizaciones mediante código 2FA. | Variable (Baja a Alta): Desde usuarios sin conocimientos técnicos hasta usuarios avanzados. | Dispositivo móvil personal (iOS/Android) vía navegador web progresivo (PWA) sin instalar aplicaciones. |
### 4.3.2 Restricciones, supuestos y dependencias
Restricciones:
Presupuesto y Licenciamiento: El desarrollo debe realizarse estrictamente con herramientas, lenguajes y frameworks de código abierto (Open Source como Python y FastAPI), garantizando cero costos de licencias o rentas de software.
Infraestructura Física: El taller cuenta únicamente con 4 bahías de trabajo físicas (capacidad estricta de 1 vehículo por bahía) y un estacionamiento con capacidad máxima de 5 vehículos en espera.
Dispositivos Hardware: La captura digital en taller se limita a máximo 2 tabletas táctiles centralizadas por el Jefe de Mecánicos para proteger la inversión y evitar daños.
Alcance del Vehículo: La plataforma atenderá exclusivamente vehículos ligeros (automóviles particulares, motocicletas y camionetas), excluyendo maquinaria pesada o industrial.
Supuestos:
Se asume que el taller mantiene activa una conexión de red local (Wi-Fi) para la sincronización entre computadoras de mostrador y tabletas de taller en condiciones normales.
Se asume que los clientes cuentan con un correo electrónico para recibir el enlace de seguimiento y los códigos de verificación de 6 dígitos (2FA); el número celular se usa para el envío opcional del enlace por SMS (RF-02.3).
Se asume que los datos ingresados durante la fase de desarrollo y pruebas son 100% ficticios para dar cumplimiento a la Ley Federal de Protección de Datos Personales.
Dependencias:
Infraestructura Eléctrica y Red: Operación dependiente de baterías en laptops/tabletas y arquitectura Local-First / PWA (Service Workers e IndexedDB) para permitir la captura de datos offline durante cortes de luz o fallas de internet.
Proveedores Externos de Comunicación: Dependencia del servicio de correo electrónico para entregar enlaces y códigos 2FA al cliente, y de un servicio de SMS para el envío opcional del enlace.
Disponibilidad de Refaccionarias Locales: La adquisición de piezas fuera de stock depende del directorio de proveedores locales e historial de compras del almacén.
## 4.4 Requisitos funcionales
| ID | Requisito funcional | Módulo | Prioridad (MoSCoW) | Historias relacionadas |
| --- | --- | --- | --- | --- |
| RF-01 | El sistema deberá permitir autenticar mediante credenciales seguras al personal del taller según su rol (Gerente, Recepcionista, Jefe de Mecánicos y Encargado de Almacén). | M1 – Autenticación y Seguridad | Must | HU-27 |
| RF-02.1 | El sistema deberá permitir al cliente consultar el estado de su vehículo y autorizar cotizaciones mediante un enlace web seguro enviado por correo electrónico o por SMS (RF-02.3), sin instalar aplicaciones. | M1 – Autenticación y Seguridad | Must | HU-02, HU-28 |
| RF-02.2 | El sistema deberá de expirar el enlace del cliente de manera automática una vez que el vehículo sea entregado y saldado. | M1 – Autenticación y Seguridad | Should | HU-02, HU-23 |
| RF-02.3 | El sistema deberá de permitir enviar el enlace del cliente también por SMS. | M1 – Autenticación y Seguridad | Could | HU-02 |
| RF-03.1 | El sistema deberá registrar, buscar y actualizar la información de clientes y vehículos (placas, marca, modelo, año y VIN (opcional)). | M3 – Recepción E Historial Inicial | Must | HU-05, HU-06 |
| RF-03.2 | El sistema deberá mantener el historial de servicios de cada vehículo, con fotografías de recepción, diagnósticos técnicos y garantías aplicables (30 días en mano de obra). | M7 – Portal del Cliente, Cobro y Gerencia | Should | HU-23, HU-24 |
| RF-04 | El sistema deberá registrar en la recepción el kilometraje, el nivel de combustible y un checklist de carrocería, y exigir fotografías digitales del estado inicial de la unidad. | M3 – Recepción E Historial Inicial | Must | HU-01, HU-25, HU-26 |
| RF-05 | El sistema deberá permitir abrir órdenes de servicio asociadas a una de las 4 bahías y a un mecánico responsable, controlando los estados operativos del taller. | M5 – Taller, Bahías y Expediente Técnico | Must | HU-07, HU-08, HU-09, HU-11 |
| RF-06 | El sistema deberá generar cotizaciones desglosadas (mano de obra y refacciones/insumos) con vigencia de 5 días naturales y requerir firma digital validada con un código enviado al correo del cliente, de forma remota o presencial. | M4 Cotización y Contratos 2FA | Must | HU-02, HU-12, HU-13, HU-14, HU-15 |
| RF-07 | El sistema deberá bloquear el avance del trabajo y exigir una nueva autorización con verificación cuando los trabajos adicionales incrementen el monto inicial en más de 10 %. | M4 Cotización y Contratos 2FA | Must | HU-16 |
| RF-08.1 | El sistema deberá permitir al jefe de mecánicos solicitar al almacén las piezas que requieran los mecánicos, vinculadas a una orden de servicio. | M6 – Almacén y Refacciones | Should | HU-10, HU-19 |
| RF-08.2 | El sistema deberá permitir al encargado de almacén mantener un directorio de proveedores locales (teléfonos o correos) y registrar costos y fechas de llegada de las piezas. | M6 – Almacén y Refacciones | Should | HU-17, HU-18 |
| RF-08.3 | El sistema deberá de emitir un ticket e historial de compras asociado a cada orden de servicio. | M6 – Almacén y Refacciones | Could | HU-18 |
| RF-09 | El sistema deberá ofrecer una agenda digital por día y bahía, donde las citas solicitadas en línea quedan “Pendientes” hasta que la recepcionista verifique disponibilidad y las confirme manualmente | M2 – Citas y Solicitudes | Should | HU-03, HU-04, HU-06 |
| RF-10 | El sistema deberá impedir la entrega física del vehículo con saldo pendiente, a menos que el gerente autorice la entrega a crédito para vehículos de flotillas empresariales previamente registradas. | M7 – Portal del Cliente, Cobro y Gerencia | Must | HU-21, HU-22, HU-23 |
| RF-11 | El sistema deberá ofrecer al gerente un panel con las órdenes abiertas y su estado, la ocupación de las 4 bahías, los tiempos de estancia y los ingresos acumulados. | M7 – Portal del Cliente, Cobro y Gerencia | Should | HU-29 |
## 4.5 Historias de usuario (Product Backlog)
| ID / issue | Historia (Como… quiero… para…) | Prioridad | Puntos | Release | Estado |
| --- | --- | --- | --- | --- | --- |
| HU-01 / #[1] | Como recepcionista del taller, quiero registrar la recepción del vehículo adjuntando kilometraje, nivel de combustible, checklist de carrocería y fotografías del estado inicial, para contar con un respaldo digital inalterable que evite reclamos infundados por daños o faltantes al entregar la unidad. | Must | 3 | v0.1.0 | En progreso (API) |
| HU-02 / #[2] | Como cliente del taller, quiero recibir un enlace web seguro con la cotización detallada (mano de obra y refacciones) y botones claros de aprobación o rechazo, para revisar y autorizar los trabajos desde mi teléfono sin necesidad de realizar llamadas ni acudir físicamente al taller | Must | 3 | v0.1.0 | En progreso (API) |
| HU-03 / #[3] | Como cliente del taller, quiero solicitar una cita en línea seleccionando el día y la hora disponible, para apartar un espacio sin necesidad de realizar llamadas telefónicas. | Must | 3 | v0.1.0 | En progreso (API) |
| HU-04 / #[4] | Como recepcionista del taller, quiero consultar la agenda digital por día y por bahía, para verificar las solicitudes pendientes de los clientes y realizar su confirmación manual. | Must |  | v0.1.0 | En progreso (API) |
| HU-05 / #[5] | Como recepcionista del taller, quiero buscar a un cliente o vehículo registrado mediante su número telefónico o placas, para agilizar el proceso de recepción en visitas recurrentes. | Should |  | Fase 2 | En progreso (API) |
| HU-06 / #[6] | Como recepcionista del taller, quiero registrar un vehículo con cita previa seleccionando su folio de origen, para que el sistema precargue automáticamente los datos del cliente y del auto. | Should | 2 | v0.1.0 | En progreso (API) |
| HU-07 / #[7] | Como recepcionista del taller, quiero ver la alerta de "Sin Bahías Disponibles" cuando las 4 bahías físicas estén ocupadas, para ubicar temporalmente el vehículo en el estacionamiento de recepción. | Must | 3 | v0.1.0 | En progreso (API) |
| HU-08 / #[8] | Como jefe de mecánicos, quiero asignar la orden de servicio a una de las 4 bahías físicas disponibles y a un mecánico responsable, para iniciar formalmente los trabajos en el taller. | Must | 5 | v0.1.0 | En progreso (API) |
| HU-09 / #[9] | Como jefe de mecánicos, quiero registrar el diagnóstico técnico y las observaciones iniciales en la tableta, para cambiar el estado de la orden a "En Diagnóstico". | Must | 3 | v0.1.0 | En progreso (API) |
| HU-10 / #[10] | Como jefe de mecánicos, quiero registrar las refacciones e insumos que los mecánicos detecten durante la revisión, para que el área de almacén gestione su cotización o pedido. | Should |  | v0.1.0 | Pendiente |
| HU-11 / #[11] | Como jefe de mecánicos, quiero visualizar el estatus actual de las 4 bahías de trabajo en una interfaz simplificada para tabletas, para conocer rápidamente qué unidades están listas o en proceso. | Should | 3 | Fase 2 | Pendiente |
| HU-12 / #[12] | Como recepcionista o jefe de mecánicos, quiero generar un presupuesto desglosado de mano de obra y refacciones con vigencia de 5 días naturales, para enviarlo de forma transparente al cliente. | Must | 5 | v0.1.0 | En progreso (API) |
| HU-13 / #[13] | Como cliente del taller, quiero seleccionar o deseleccionar servicios opcionales dentro de mi cotización antes de aprobarla, para adaptar el presupuesto a mis necesidades financieras. | Should | 3 | v0.1.0 | En progreso (API) |
| HU-14 / #[14] | Como cliente del taller, quiero realizar la firma digital de aprobación mediante un código de verificación de 2 pasos enviado a mi correo, para autorizar los trabajos de forma segura ya sea de forma presencial o remota. | Must | 5 | v0.1.0 | En progreso (API) |
| HU-15 / #[15] | Como cliente del taller, quiero presionar un botón de rechazo en la cotización digital, para cancelar la orden y coordinar la recolección del vehículo sin autorizar reparaciones. | Should | 2 | v0.1.0 | En progreso (API) |
| HU-16 / #[16] | Como cliente del taller, quiero que se me pida una nueva autorización con código 2FA cuando los costos imprevistos superen el 10 % del presupuesto autorizado, para no pagar trabajos que no aprobé. | Must | 5 | v0.1.0 | En progreso (API) |
| HU-17 / #[17] | Como encargado de almacén, quiero consultar y administrar un directorio de proveedores locales con teléfonos y correos electrónicos, para solicitar refacciones especiales rápidamente. | Should | 3 | v0.1.0 | Pendiente |
| HU-18 / #[18] | Como encargado de almacén, quiero registrar los costos, fechas de llegada y tickets de compra de las refacciones asociadas a una orden, para mantener un control financiero estricto. | Should | 3 | v0.1.0 | Pendiente |
| HU-19 / #[19] | Como jefe de mecánicos, quiero verificar el stock de refacciones comunes en el inventario interno, para saber si se dispone de la pieza de forma inmediata. | Could | 2 | Fase 2 | Pendiente |
| HU-20 / #[20] | Como recepcionista, quiero recibir una notificación automática cuando los trabajos del vehículo finalicen, para avisar al cliente que su unidad está lista para entrega. | Should | 2 | v0.1.0 | En progreso (API) |
| HU-21 / #[21] | Como gerente del taller, quiero que el sistema impida registrar la entrega de un vehículo cuya orden tenga saldo pendiente, para evitar pérdidas financieras al taller. | Must | 3 | v0.1.0 | En progreso (API) |
| HU-22 / #[22] | Como gerente del taller, quiero autorizar de forma excepcional la entrega a crédito únicamente para vehículos de flotillas empresariales registradas, para cumplir con los convenios comerciales. | Should | 3 | v0.1.0 | En progreso (API) |
| HU-23 / #[23] | Como recepcionista, quiero registrar el pago total del servicio y cerrar formalmente la orden, para liberar la bahía de trabajo y archivar el historial del vehículo. | Must | 3 | v0.1.0 | En progreso (API) |
| HU-24 / #[24] | Como cliente, quiero consultar la vigencia de la garantía de 30 días en mano de obra asociada a mi servicio anterior, para reclamar ajustes en caso de incidencias. | Could | 2 | Fase 2 | Pendiente |
| HU-25 / #[25] | Como recepcionista o jefe de mecánicos, quiero registrar la llegada de autos, tomar fotografías y hacer diagnósticos sin conexión a internet usando la batería del equipo, para que la operación no se detenga ante fallas eléctricas. | Must | 8 | v0.1.0 | Pendiente |
| HU-26 / #[26] | Como recepcionista o jefe de mecánicos, quiero que los registros y fotografías que capturé sin conexión se sincronicen automáticamente cuando vuelva la red, para no perder ni duplicar información. | Must | 8 | v0.1.0 | Pendiente |
| HU-27 / #[27] | Como gerente del taller, quiero dar de alta al personal y asignarle su rol (Gerente, Recepcionista, Jefe de Mecánicos o Encargado de Almacén), para que cada quien acceda solo a la información que le corresponde. | Must | 3 | v0.1.0 | En progreso (API) |
| HU-28 / #[28] | Como cliente, quiero visualizar la plataforma web desde mi teléfono celular de forma responsiva y sin instalar aplicaciones adicionales, para consultar mi estatus con facilidad. | Must | 5 | v0.1.0 | Pendiente |
| HU-29 / #[29] | Como gerente, quiero generar reportes mensuales de ingresos, servicios realizados y tiempos de ocupación de las 4 bahías, para evaluar el rendimiento general del taller. | Could | 5 | Fase 2 | Pendiente |
| HU-30 / #[30] | Como cliente del taller, quiero conocer el aviso de privacidad antes de proporcionar mis datos, para saber para qué se usarán conforme a la LFPDPPP. | Must | 3 | v0.1.0 | En progreso (API) |
Detalle de las historias de usuario
HU-01: Recepción e Inspección con Evidencia Fotográfica
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-01 / #[1] |
| Historia | Como recepcionista del taller, quiero registrar la recepción del vehículo adjuntando kilometraje, nivel de combustible, checklist de carrocería y fotografías del estado inicial, para contar con un respaldo digital inalterable que evite reclamos infundados por daños o faltantes al entregar la unidad. |
| Criterio de aceptación 1 | Dado que la recepcionista se encuentra en el módulo de recepción vehicular, cuando intenta registrar una unidad nueva, entonces el sistema exige obligatoriamente adjuntar al menos 4 fotografías (frente, parte trasera, costado izquierdo y costado derecho). |
| Criterio de aceptación 2 | Dado que se capturan las evidencias, cuando se finaliza el formulario de inspección, entonces el sistema genera una firma visual o sello digital con fecha y hora exacta de recepción, bloqueando el avance al estado "En Diagnóstico" si falta completar algún punto del checklist obligatorio. |
| Reglas de negocio | RN-12 (Evidencia fotográfica de recepción), RN-07 (Clasificación de vehículos autorizados). |
| Wireframe | Figura 4.5 |
| Casos de prueba | CPA-01 a CPA-04 |
HU-02: Autorización Digital de Cotización por Parte del Cliente
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-02 / #[2] |
| Historia | Como cliente del taller, quiero recibir un enlace web seguro con la cotización detallada (mano de obra y refacciones) y botones claros de aprobación o rechazo, para revisar y autorizar los trabajos desde mi teléfono sin necesidad de realizar llamadas ni acudir físicamente al taller |
| Criterio de aceptación 1 | Dado que la cotización ha sido generada por el taller, cuando el sistema envía el aviso, entonces el cliente recibe un enlace por correo electrónico (o por SMS cuando se habilite RF-02.3) que no requiere registro previo ni contraseña, operando mediante un token temporal firmado. |
| Criterio de aceptación 2 | Dado que el cliente revisa el desglose en su dispositivo móvil, cuando presiona el botón "Autorizar" e ingresa un código 2FA válido (HU-14), entonces el sistema registra de forma inalterable la dirección IP, fecha, hora y el monto final aceptado, cambiando automáticamente el estado de la orden a "Autorizada" y notificando al mecánico responsable. |
| Reglas de negocio | RN-01 (Expiración y vigencia de enlaces), RN-02 (Doble verificación en autorizaciones), RN-11 (Vigencia de cotizaciones). |
| Wireframe | Figura 4.8 |
| Casos de prueba | CPA-10, CPA-30 |
HU-03: Solicitud de Cita en Línea
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-03 / #[3] |
| Historia | Como cliente del taller, quiero solicitar una cita en línea seleccionando el día y la hora disponible, para apartar un espacio sin necesidad de realizar llamadas telefónicas. |
| Criterio de aceptación 1 | Dado que el cliente accede al portal web, cuando selecciona fecha, hora y tipo de servicio, entonces el sistema valida que exista disponibilidad en la agenda del taller. |
| Criterio de aceptación 2 | Dado que se envía la solicitud, cuando se registra con éxito, entonces queda en estado "Pendiente" a la espera de la confirmación manual de la recepcionista. |
| Reglas de negocio | RN-08 (Confirmación manual de citas web). |
| Wireframe | Figura 4.9 |
| Casos de prueba | CPA-31, CPA-34 |
HU-04: Consulta y Confirmación Manual de Citas
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-04 / #[4] |
| Historia | Como recepcionista del taller, quiero consultar la agenda digital por día y por bahía, para verificar las solicitudes pendientes de los clientes y realizar su confirmación manual. |
| Criterio de aceptación 1 | Dado que la recepcionista accede al módulo de agenda, cuando filtra los registros por el día actual, entonces el sistema despliega todas las citas con estatus "Pendiente". |
| Criterio de aceptación 2 | Dado que la recepcionista revisa una cita solicitada, cuando presiona el botón "Confirmar", entonces el estatus cambia a "Confirmada" y se habilita la asignación de la bahía correspondiente. |
| Reglas de negocio | RN-08 (Confirmación manual de citas web), RN-05 (Capacidad física del taller). |
| Wireframe | Figura 4.9 |
| Casos de prueba | CPA-32 |
HU-05: Búsqueda Rápida de Clientes y Vehículos
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-05 / #[5] |
| Historia | Como recepcionista del taller, quiero buscar a un cliente o vehículo registrado mediante su número telefónico o placas, para agilizar el proceso de recepción en visitas recurrentes. |
| Criterio de aceptación 1 | Dado que la recepcionista se encuentra en el módulo de búsqueda, cuando ingresa los dígitos de las placas o el teléfono, entonces el sistema filtra instantáneamente la base de datos de clientes recurrentes. |
| Criterio de aceptación 2 | Dado que se localiza el expediente, cuando el usuario lo selecciona, entonces el sistema precarga los datos generales del cliente y del auto para evitar duplicidad de registros. |
| Reglas de negocio | Sin regla de negocio específica; ver RF-03.1. |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-06: Registro de Vehículos con Cita Previa
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-06 / #[6] |
| Historia | Como recepcionista del taller, quiero registrar un vehículo con cita previa seleccionando su folio de origen, para que el sistema precargue automáticamente los datos del cliente y del auto. |
| Criterio de aceptación 1 | Dado que el cliente llega al taller con cita agendada, cuando la recepcionista introduce el número de folio de la cita, entonces el sistema recupera la información asociada. |
| Criterio de aceptación 2 | Dado que los datos están precargados, cuando se procede con el ingreso, entonces el sistema vincula la cita directamente con la nueva orden de servicio abierta. |
| Reglas de negocio | RN-08 (Confirmación manual de citas web). |
| Wireframe | Figura 4.5 |
| Casos de prueba | CPA-33 |
HU-07: Alerta de Bahías Ocupadas
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-07 / #[7] |
| Historia | Como recepcionista del taller, quiero ver la alerta de "Sin Bahías Disponibles" cuando las 4 bahías físicas estén ocupadas, para ubicar temporalmente el vehículo en el estacionamiento de recepción. |
| Criterio de aceptación 1 | Dado que las 4 bahías físicas del taller registran una orden activa, cuando la recepcionista intenta registrar la entrada de un nuevo vehículo, entonces el sistema emite una advertencia visual en pantalla indicando "Sin Bahías Disponibles". |
| Criterio de aceptación 2 | Dado que se activa la alerta de saturación, cuando el usuario acepta la notificación, entonces el sistema permite guardar el registro temporal asignando la unidad al estacionamiento de espera. |
| Reglas de negocio | RN-05 (Capacidad física del taller). |
| Wireframe | Figura 4.5 |
| Casos de prueba | CPA-05, CPA-06 |
HU-08: Asignación de Bahía y Mecánico
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-08 / #[8] |
| Historia | Como jefe de mecánicos, quiero asignar la orden de servicio a una de las 4 bahías físicas disponibles y a un mecánico responsable, para iniciar formalmente los trabajos en el taller. |
| Criterio de aceptación 1 | Dado que la orden se encuentra abierta, cuando el jefe de mecánicos selecciona una de las 4 bahías físicas libres, entonces el sistema actualiza el estado de la bahía a "Ocupada". |
| Criterio de aceptación 2 | Dado que las 4 bahías están ocupadas, cuando se intenta una asignación, entonces el sistema emite una alerta impidiendo el cruce de unidades en la misma bahía. |
| Reglas de negocio | RN-05 (Capacidad física del taller), RN-09 (Asignación y colaboración de mecánicos). |
| Wireframe | Figura 4.6 |
| Casos de prueba | CPA-07, CPA-08 |
HU-09: Registro de Diagnóstico en Tableta
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-09 / #[9] |
| Historia | Como jefe de mecánicos, quiero registrar el diagnóstico técnico y las observaciones iniciales en la tableta, para cambiar el estado de la orden a "En Diagnóstico". |
| Criterio de aceptación 1 | Dado que el jefe de mecánicos se encuentra autenticado en la tableta, cuando selecciona una orden con vehículo en bahía, entonces visualiza un formulario táctil optimizado con campos amplios para el dictamen técnico. |
| Criterio de aceptación 2 | Dado que se ingresan las observaciones de la revisión, cuando se presiona "Guardar Diagnóstico", entonces el sistema actualiza automáticamente el estado de la orden a "En Diagnóstico" y habilita la creación de cotizaciones. |
| Reglas de negocio | RN-12 (Evidencia fotográfica de recepción). Usabilidad en tableta: RNF-02 y RNF-03. |
| Wireframe | Figura 4.6 |
| Casos de prueba | CPA-02, CPA-03 |
HU-10: Solicitud de Refacciones e Insumos
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-10 / #[10] |
| Historia | Como jefe de mecánicos, quiero registrar las refacciones e insumos que los mecánicos detecten durante la revisión, para que el área de almacén gestione su cotización o pedido. |
| Criterio de aceptación 1 | Dado que un mecánico reporta piezas necesarias en la bahía, cuando el jefe de mecánicos las añade desde la tableta y las vincula a la orden, entonces la solicitud se envía automáticamente al módulo de almacén. |
| Criterio de aceptación 2 | Dado que el almacén recibe el requerimiento, cuando se procesa, entonces el sistema refleja el estatus de la refacción como "Solicitada" o "Pedida". |
| Reglas de negocio | RN-04 (Re-cotización obligatoria por sobrecostos), RN-06 (Reubicación por espera de refacciones). |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-11: Visualización del Estatus de Bahías
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-11 / #[11] |
| Historia | Como jefe de mecánicos, quiero visualizar el estatus actual de las 4 bahías de trabajo en una interfaz simplificada para tabletas, para conocer rápidamente qué unidades están listas o en proceso. |
| Criterio de aceptación 1 | Dado que el jefe de mecánicos accede al tablero de control, cuando visualiza la sección de bahías, entonces identifica mediante códigos de color las unidades activas, en diagnóstico o listas. |
| Criterio de aceptación 2 | Dado que se actualiza el estado de una reparación, cuando cambia de fase, entonces el tablero refresca la información en tiempo real para optimizar la supervisión del taller. |
| Reglas de negocio | RN-05 (Capacidad física del taller). Usabilidad en tableta: RNF-02. |
| Wireframe | Figura 4.6 |
| Casos de prueba | Pendiente |
HU-12: Generación de Presupuesto Desglosado
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-12 / #[12] |
| Historia | Como recepcionista o jefe de mecánicos, quiero generar un presupuesto desglosado de mano de obra y refacciones con vigencia de 5 días naturales, para enviarlo de forma transparente al cliente. |
| Criterio de aceptación 1 | Dado que el diagnóstico ha concluido, cuando el personal selecciona la opción de cotizar, entonces el sistema presenta apartados separados para costos de mano de obra y refacciones. |
| Criterio de aceptación 2 | Dado que se emite la cotización, entonces el sistema calcula automáticamente el total con IVA e integra una fecha de expiración exactamente a los 5 días naturales posteriores a su emisión. |
| Reglas de negocio | RN-11 (Vigencia de cotizaciones), RN-03 (Selección granular de rubros). |
| Wireframe | Figura 4.7 |
| Casos de prueba | CPA-10 |
HU-13: Selección de Servicios Opcionales en Cotización
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-13 / #[13] |
| Historia | Como cliente del taller, quiero seleccionar o deseleccionar servicios opcionales dentro de mi cotización antes de aprobarla, para adaptar el presupuesto a mis necesidades financieras. |
| Criterio de aceptación 1 | Dado que el cliente revisa el presupuesto desglosado en su celular, cuando marca o desmarca las casillas de servicios opcionales o sugeridos, entonces el sistema recalcula el costo total en tiempo real. |
| Criterio de aceptación 2 | Dado que se ajustan los opcionales, cuando el cliente procede a la firma, entonces el sistema guarda únicamente los conceptos seleccionados como parte oficial de la orden. |
| Reglas de negocio | RN-03 (Selección granular de rubros). |
| Wireframe | Figura 4.8 |
| Casos de prueba | CPA-12 |
HU-14: Firma Digital y Autorización por 2FA
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-14 / #[14] |
| Historia | Como cliente del taller, quiero realizar la firma digital de aprobación mediante un código de verificación de 2 pasos enviado a mi correo, para autorizar los trabajos de forma segura ya sea de forma presencial o remota. |
| Criterio de aceptación 1 | Dado que el cliente accede al enlace web de cotización, when solicita el código de autorización, entonces el sistema envía un token numérico de 6 dígitos al correo electrónico registrado del cliente. |
| Criterio de aceptación 2 | Dado que el cliente ingresa el código recibido en la interfaz, cuando presiona "Autorizar Presupuesto", entonces el sistema valida el token, registra la dirección IP y la marca de tiempo, cambiando la orden a "Autorizada". |
| Reglas de negocio | RN-02 (Doble verificación en autorizaciones). No repudio: RNF-04. |
| Wireframe | Figura 4.8 |
| Casos de prueba | CPA-11, CPA-13 a CPA-16 |
HU-15: Rechazo de Cotización y Cancelación
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-15 / #[15] |
| Historia | Como cliente del taller, quiero presionar un botón de rechazo en la cotización digital, para cancelar la orden y coordinar la recolección del vehículo sin autorizar reparaciones. |
| Criterio de aceptación 1 | Dado que el cliente evalúa la cotización en su dispositivo, cuando presiona el botón "Rechazar", entonces el sistema solicita una confirmación de la acción. |
| Criterio de aceptación 2 | Dado que se confirma el rechazo, cuando se procesa, entonces la orden cambia a estatus "Rechazada" y notifica a recepción para coordinar la entrega física del auto sin costo de reparación. |
| Reglas de negocio | RN-02 (Doble verificación en autorizaciones). Flujo de rechazo: CU-11 (A1). |
| Wireframe | Figura 4.8 |
| Casos de prueba | CPA-17 |
HU-16: Re-cotización por Incremento >10%
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-16 / #[16] |
| Historia | Como cliente del taller, quiero que se me pida una nueva autorización con código 2FA cuando los costos imprevistos superen el 10 % del presupuesto autorizado, para no pagar trabajos que no aprobé. |
| Criterio de aceptación 1 | Dado que surgen refacciones imprevistas, cuando el incremento total supera el 10% del presupuesto aprobado, entonces el sistema bloquea el flujo y solicita una nueva autorización con código 2FA. |
| Criterio de aceptación 2 | Dado que el cliente recibe la notificación del sobrecosto, cuando aprueba mediante el código digital, entonces se actualiza el monto total e historial de la orden. |
| Reglas de negocio | RN-04 (Re-cotización obligatoria por sobrecostos), RN-02 (Doble verificación en autorizaciones). |
| Wireframe | Figura 4.7 |
| Casos de prueba | CPA-18, CPA-19 |
HU-17: Directorio y Gestión de Proveedores Locales
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-17 / #[17] |
| Historia | Como encargado de almacén, quiero consultar y administrar un directorio de proveedores locales con teléfonos y correos electrónicos, para solicitar refacciones especiales rápidamente. |
| Criterio de aceptación 1 | Dado que el almacenista ingresa al módulo de refacciones, cuando abre el directorio de proveedores, entonces visualiza la lista con datos de contacto actualizados (teléfonos y correos). |
| Criterio de aceptación 2 | Dado que se requiere dar de alta un nuevo proveedor, cuando el almacenista completa el formulario de registro, entonces el sistema lo almacena para futuras solicitudes de piezas. |
| Reglas de negocio | RN-06 (Reubicación por espera de refacciones). |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-18: Registro de Costos e Historial de Compras
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-18 / #[18] |
| Historia | Como encargado de almacén, quiero registrar los costos, fechas de llegada y tickets de compra de las refacciones asociadas a una orden, para mantener un control financiero estricto. |
| Criterio de aceptación 1 | Dado que se adquiere una pieza externa con un proveedor, cuando el almacenista registra el ticket, costo unitario y fecha estimada de entrega, entonces el sistema lo vincula a la orden de servicio. |
| Criterio de aceptación 2 | Dado que se ingresa la compra, cuando se consolida el registro, entonces el sistema actualiza el historial de adquisiciones de la refacción para auditoría interna. |
| Reglas de negocio | Sin regla de negocio específica; ver RF-08.2 y RF-08.3. |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-19: Verificación de Stock Interno
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-19 / #[19] |
| Historia | Como jefe de mecánicos, quiero verificar el stock de refacciones comunes en el inventario interno, para saber si se dispone de la pieza de forma inmediata. |
| Criterio de aceptación 1 | Dado que el jefe de mecánicos busca un insumo estándar, cuando consulta el inventario en el sistema, entonces visualiza las existencias disponibles en almacén. |
| Criterio de aceptación 2 | Dado que hay existencia en stock, cuando se selecciona la pieza, entonces el sistema descuenta automáticamente la cantidad del inventario interno. |
| Reglas de negocio | Sin regla de negocio específica; ver RF-08.1. |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-20: Notificación Automática de Fin de Trabajos
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-20 / #[20] |
| Historia | Como recepcionista, quiero recibir una notificación automática cuando los trabajos del vehículo finalicen, para avisar al cliente que su unidad está lista para entrega. |
| Criterio de aceptación 1 | Dado que el mecánico marca la orden como terminada en bahía, cuando se actualiza el estatus, entonces el sistema envía una alerta interna a la recepcionista. |
| Criterio de aceptación 2 | Dado que la recepción recibe la alerta, cuando se verifica el estado, entonces se habilita el aviso automatizado al cliente de que su vehículo está listo. |
| Reglas de negocio | Sin regla de negocio específica; ver CU-07. |
| Wireframe | Figura 4.10 |
| Casos de prueba | Pendiente |
HU-21: Bloqueo de Entrega por Saldo Pendiente
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-21 / #[21] |
| Historia | Como gerente del taller, quiero que el sistema impida registrar la entrega de un vehículo cuya orden tenga saldo pendiente, para evitar pérdidas financieras al taller. |
| Criterio de aceptación 1 | Dado que un vehículo se encuentra en estado "Lista para Entrega", cuando la recepcionista intenta registrar la salida y el balance de pago es mayor a cero, entonces el sistema bloquea la acción de liberación. |
| Criterio de aceptación 2 | Dado que se activa el bloqueo por saldo pendiente, cuando el sistema detecta que cuenta con un convenio de crédito autorizado, entonces permite omitir la restricción exclusivamente bajo permisos del rol Gerente. |
| Reglas de negocio | RN-10 (Restricción de entrega y excepción a flotillas). |
| Wireframe | Figura 4.10 |
| Casos de prueba | CPA-21 |
HU-22: Autorización Excepcional de Crédito a Flotillas
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-22 / #[22] |
| Historia | Como gerente del taller, quiero autorizar de forma excepcional la entrega a crédito únicamente para vehículos de flotillas empresariales registradas, para cumplir con los convenios comerciales. |
| Criterio de aceptación 1 | Dado que un vehículo pertenece a una empresa con cuenta de flotilla registrada, cuando se intenta liberar sin pago en caja, entonces el sistema solicita la clave de autorización gerencial. |
| Criterio de aceptación 2 | Dado que el gerente ingresa su contraseña de aprobación, cuando valida el convenio comercial, entonces el sistema permite liberar la unidad y factura el adeudo a crédito empresarial. |
| Reglas de negocio | RN-10 (Restricción de entrega y excepción a flotillas). |
| Wireframe | Figura 4.10 |
| Casos de prueba | CPA-24, CPA-25 |
HU-23: Registro de Pago Total y Cierre de Orden
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-23 / #[23] |
| Historia | Como recepcionista, quiero registrar el pago total del servicio y cerrar formalmente la orden, para liberar la bahía de trabajo y archivar el historial del vehículo. |
| Criterio de aceptación 1 | Dado que el cliente cubre el monto total en caja, cuando la recepcionista registra el método de pago y confirma la transacción, entonces el sistema salda la cuenta a cero. |
| Criterio de aceptación 2 | Dado que el pago ha sido registrado con éxito, cuando se ejecuta el cierre, entonces la orden cambia a estado "Cerrada", liberando de inmediato la bahía física ocupada y generando el comprobante digital. |
| Reglas de negocio | RN-10 (Restricción de entrega y excepción a flotillas), RN-13 (Garantía de mano de obra), RN-01 (Expiración y vigencia de enlaces). |
| Wireframe | Figura 4.10 |
| Casos de prueba | CPA-22, CPA-23 |
HU-24: Consulta de Vigencia de Garantía
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-24 / #[24] |
| Historia | Como cliente, quiero consultar la vigencia de la garantía de 30 días en mano de obra asociada a mi servicio anterior, para reclamar ajustes en caso de incidencias. |
| Criterio de aceptación 1 | Dado que el cliente revisa el expediente de su servicio pasado en el portal web, cuando consulta el apartado de garantías, entonces visualiza la fecha exacta de expiración (30 días naturales en mano de obra). |
| Criterio de aceptación 2 | Dado que la garantía se encuentra vigente, cuando se solicita una revisión por el mismo concepto, entonces el sistema valida el estatus sin generar cargos adicionales de mano de obra. |
| Reglas de negocio | RN-13 (Garantía de mano de obra). |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-25: Operación Offline del Personal Interno
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-25 / #[25] |
| Historia | Como recepcionista o jefe de mecánicos, quiero registrar la llegada de autos, tomar fotografías y hacer diagnósticos sin conexión a internet usando la batería del equipo, para que la operación no se detenga ante fallas eléctricas. |
| Criterio de aceptación 1 | Dado que ocurre un corte de energía o caída de internet en el taller, cuando el personal opera mediante las baterías de laptops o tabletas, entonces el sistema local permite continuar capturando registros, checklists y fotografías. |
| Criterio de aceptación 2 | Dado que se trabaja de forma local (offline), cuando se guardan los datos, entonces el almacenamiento temporal mediante Service Workers e IndexedDB asegura que no exista pérdida de información. |
| Reglas de negocio | Sin regla de negocio específica; ver RNF-06 y RNF-08. |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-26: Sincronización Automática en la Nube
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-26 / #[26] |
| Historia | Como recepcionista o jefe de mecánicos, quiero que los registros y fotografías que capturé sin conexión se sincronicen automáticamente cuando vuelva la red, para no perder ni duplicar información. |
| Criterio de aceptación 1 | Dado que se restablece la conexión a internet en el taller, cuando el sistema detecta conectividad, entonces inicia de forma automática la sincronización de los datos almacenados localmente. |
| Criterio de aceptación 2 | Dado que finaliza el proceso de sincronización, cuando se actualiza la base de datos central en la nube, entonces la información multimedia y de auditoría se consolida sin duplicidades. |
| Reglas de negocio | Sin regla de negocio específica; ver RNF-09. |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-27: Gestión de Roles y Permisos de Seguridad
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-27 / #[27] |
| Historia | Como gerente del taller, quiero dar de alta al personal y asignarle su rol (Gerente, Recepcionista, Jefe de Mecánicos o Encargado de Almacén), para que cada quien acceda solo a la información que le corresponde. |
| Criterio de aceptación 1 | Dado que un usuario intenta acceder a la plataforma, cuando introduce sus credenciales, entonces el sistema autentica su identidad y restringe los menús según su rol asignado (Gerente, Recepcionista, Jefe de Mecánicos o Encargado de Almacén). |
| Criterio de aceptación 2 | Dado que un usuario sin privilegios intenta ingresar a una ruta protegida (como reportes gerenciales), entonces el sistema deniega el acceso y muestra una pantalla de error por permisos insuficientes. |
| Reglas de negocio | Sin regla de negocio específica; ver RNF-05 y 4.8 (control de acceso por rol). |
| Wireframe | Pendiente |
| Casos de prueba | CPA-28, CPA-29 |
HU-28: Accesibilidad PWA Responsiva para Clientes
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-28 / #[28] |
| Historia | Como cliente, quiero visualizar la plataforma web desde mi teléfono celular de forma responsiva y sin instalar aplicaciones adicionales, para consultar mi estatus con facilidad. |
| Criterio de aceptación 1 | Dado que el cliente abre el enlace recibido por SMS o correo en un navegador móvil (iOS/Android), cuando carga la página, entonces el diseño se adapta responsivamente a la pantalla sin requerir descargas de tiendas de aplicaciones. |
| Criterio de aceptación 2 | Dado que el cliente navega por el portal web, cuando consulta el progreso de su vehículo o galería de fotos, entonces los elementos táctiles responden de manera fluida y adaptada a dispositivos móviles. |
| Reglas de negocio | RN-01 (Expiración y vigencia de enlaces). Portabilidad: RNF-01. |
| Wireframe | Figura 4.8 |
| Casos de prueba | Pendiente |
HU-29: Generación de Reportes Gerenciales
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-29 / #[29] |
| Historia | Como gerente, quiero generar reportes mensuales de ingresos, servicios realizados y tiempos de ocupación de las 4 bahías, para evaluar el rendimiento general del taller. |
| Criterio de aceptación 1 | Dado que el gerente ingresa al módulo de reportes, cuando selecciona el intervalo de fechas mensual, entonces el sistema genera métricas consolidadas de ingresos y servicios completados. |
| Criterio de aceptación 2 | Dado que se consultan los tiempos operativos, cuando el sistema procesa las órdenes, entonces muestra gráficos de ocupación de las 4 bahías para medir la eficiencia del taller. |
| Reglas de negocio | Sin regla de negocio específica; ver RF-11. |
| Wireframe | Pendiente |
| Casos de prueba | Pendiente |
HU-30: Cumplimiento de Privacidad y Uso de Datos Ficticios
| Campo | Contenido |
| --- | --- |
| ID e issue | HU-30 / #[30] |
| Historia | Como cliente del taller, quiero conocer el aviso de privacidad antes de proporcionar mis datos, para saber para qué se usarán conforme a la LFPDPPP. |
| Criterio de aceptación 1 | Dado que la recepcionista registra a un cliente nuevo, cuando captura sus datos personales, entonces el sistema muestra el aviso de privacidad simplificado (4.8) antes de guardar el registro. |
| Criterio de aceptación 2 | Dado que el cliente abre su enlace seguro por primera vez, cuando carga la página, entonces el sistema muestra el enlace al aviso de privacidad integral y cómo ejercer sus derechos ARCO. |
| Reglas de negocio | Sin regla de negocio específica; ver 4.8 y RNF-05. |
| Wireframe | Pendiente |
| Casos de prueba | CPA-31 |
Pendiente
Descripción: las actividades del cliente y del personal en columnas (Agendar cita, Recibir vehículo, Asignar y diagnosticar, Cotizar y autorizar, Reparar, Cobrar y entregar, Supervisar) y debajo las historias HU-01 a HU-30 ordenadas por prioridad; una línea horizontal marca el corte del release v0.1.0 (historias Must y Should con release v0.1.0 de la tabla anterior) y lo que pasa a la Fase 2 (HU-05, HU-11, HU-19, HU-24, HU-29).
Archivo fuente: docs/04-requisitos/story-map.drawio
Figura 4.1. Story map con el corte del release v0.1.0. Fuente: docs/04-requisitos/story-map.drawio
## 4.6 Requisitos no funcionales
| ID | Característica ISO/IEC 25010:2023 | Requisito | Métrica y umbral | Cómo se verificará |
| --- | --- | --- | --- | --- |
| RNF-01 | Flexibilidad (instalabilidad y adaptabilidad) | El portal del cliente deberá ser una PWA responsiva que funcione en navegadores móviles iOS y Android sin instalar software ni conceder permisos especiales. | Funciona sin errores bloqueantes en las 2 últimas versiones de Safari (iOS) y Chrome (Android); 0 permisos solicitados al cliente; sin desplazamiento horizontal en anchos de 360 a 430 px. | Pruebas manuales en 2 móviles reales (iOS y Android) con una lista de verificación de las pantallas del cliente y revisión con las herramientas de desarrollo del navegador. |
| RNF-02 | Capacidad de interacción | La interfaz de la tableta del jefe de Mecánicos deberá tener botones grandes, alto contraste y controles táctiles adaptados al uso con manos sucias y en ambiente ruidoso. | Botones de al menos 48 × 48 px con separación mínima de 8 px; contraste de texto de al menos 7:1; al menos 95 % de aciertos en 20 toques con guantes de trabajo. | Auditoría con Lighthouse o axe DevTools (gratuitos), medición del contraste con un verificador y prueba en la tableta real con guantes. |
| RNF-03 | Capacidad de interacción | La interfaz de la tableta deberá ofrecer flujos de pocos pasos para las operaciones frecuentes del taller. | Asignar bahía, actualizar el estado de una orden y sellar un trabajo en máximo 4 toques y 30 s cada una. | Prueba de usabilidad cronometrada con al menos 3 usuarios (o compañeros que simulen el rol), repitiendo cada operación 3 veces. |
| RNF-04 | Seguridad (no repudio e integridad) | Toda autorización de presupuesto o de sobrecosto mayor al 10 % deberá registrar marca de tiempo y metadatos inalterables, incluida la dirección IP, para evitar disputas con el cliente. | % de las autorizaciones guardan fecha y hora UTC, IP, identificador de orden y huella SHA-256 del documento; 100 % de los intentos de alterar un registro se detectan al verificar la huella. | Prueba con 20 autorizaciones, revisión de los registros guardados e intento de modificar directamente la base de datos para confirmar que la verificación lo detecta. |
| RNF-05 | Seguridad (confidencialidad y cumplimiento legal) | El manejo de datos personales deberá apegarse a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares y usar solo datos ficticios en las pruebas. | % de las conexiones con HTTPS (TLS 1.2 o superior); datos personales sensibles cifrados en reposo; aviso de privacidad visible en el 100 % de los formularios que capturan datos; 0 registros reales en el ambiente de pruebas. | Análisis con testssl.sh o SSL Labs, lista de verificación de la ley revisada por el equipo y revisión de los datos de prueba antes de cada entrega. |
| RNF-06 | Eficiencia de desempeño | El registro de recepción se deberá guardar de forma local con rapidez, aun sin conexión. | Guardar un registro con 5 fotografías en máximo 2 s (percentil 95) en la tableta o laptop del taller. | repeticiones cronometradas con la herramienta de rendimiento del navegador, calculando el percentil 95. |
| RNF-07 | Mantenibilidad (modificabilidad) | El desarrollo deberá usar únicamente herramientas de código abierto, frameworks de uso libre (como FastAPI y Python) y planes educativos. | % de las dependencias con licencia de código abierto o plan educativo vigente; costo de licenciamiento de $0 en esta fase. | Inventario de dependencias con herramientas de revisión de licencias (por ejemplo, pip-licenses) y registro de los planes educativos usados. |
| RNF-08 | Fiabilidad (tolerancia a fallos) | El personal interno deberá poder operar sin internet o sin energía eléctrica, con equipos en batería, bajo una arquitectura local con sincronización diferida. | Las 7 operaciones definidas (registro de entrada, checklist, fotografías, diagnósticos, asignación de bahías, consulta de proveedores y autorizaciones gerenciales) funcionan al 100 % durante al menos 4 h sin conexión; 0 datos perdidos. | Casos de prueba de las 7 operaciones con la red desconectada y un equipo con batería, comparando los registros al terminar. |
| RNF-09 | Fiabilidad (recuperabilidad) | Al restablecerse la conexión, el sistema deberá sincronizar automáticamente datos, archivos multimedia y registros de auditoría con la base de datos central, sin duplicados. | % de los registros sincronizados, 0 duplicados y 0 pérdidas; 200 registros con 50 fotografías en máximo 5 min. | Crear 200 registros sin conexión, reconectar y comparar conteos y huellas con la base central; repetir 3 veces e interrumpir la conexión a mitad de una sincronización. |
| RNF-10 | Fiabilidad (tolerancia a fallos del cliente) | Ante una falla de conectividad durante la consulta de estatus o la autorización 2FA, la interfaz del cliente deberá informar el estado y reintentar automáticamente. | Mensaje de estado en máximo 3 s; reintento automático cada 30 s o menos hasta completar; 0 autorizaciones duplicadas o perdidas. | Cortar el servidor durante la consulta y durante el envío del código, cronometrar el mensaje y revisar la base de datos tras restablecer el servicio. |
## 4.7 Reglas de negocio y requisitos de dominio
| ID | Regla de negocio | Fuente (anteproyecto / entrevista con fecha) | Requisitos que afecta |
| --- | --- | --- | --- |
| RN-01 | Expiración y vigencia de enlaces: El enlace web de seguimiento permanecerá activo durante la estancia del vehículo en el taller. Expirará automáticamente al entregar y saldar la unidad. Si el cliente requiere ver su historial posteriormente, deberá solicitar la generación de un nuevo enlace. La vigencia del enlace es independiente de la vigencia de la cotización (RN-11). | Entrevista con el cliente (19/10/2026) | RF-02.1, RF-02.2 |
| RN-02 | Doble verificación en autorizaciones: Toda aprobación remota o presencial de cotización exigirá una doble verificación (código 2FA de 6 dígitos, de un solo uso y vigente 5 minutos, enviado al correo electrónico registrado del cliente) para evitar reclamos por trabajos no autorizados. | Entrevista con el cliente (19/10/2026) | RF-06, RNF-04 |
| RN-03 | Selección granular de rubros: El cliente puede aprobar o rechazar de manera independiente los conceptos opcionales desglosados en el presupuesto (mano de obra o refacciones), ejecutando únicamente lo autorizado explícitamente. | Entrevista con el cliente (19/10/2026) | RF-06 |
| RN-04 | Re-cotización obligatoria por sobrecostos (>10%): Cualquier trabajo o repuesto imprevisto durante la reparación que incremente el costo inicial más de un 10% detendrá el avance hasta contar con una nueva autorización validada por el cliente. | Anteproyecto y propuesta técnica | RF-07, RNF-04 |
| RN-05 | Capacidad física del taller: La atención simultánea está limitada estrictamente a 4 bahías físicas (1 vehículo por bahía) y un área de estacionamiento de recepción/espera con capacidad máxima para 5 vehículos. | Anteproyecto y entrevista con el cliente | RF-05, RF-09 |
| RN-06 | Reubicación por espera de refacciones: Si un vehículo requiere refacciones externas con demora de entrega de varios días, se liberará la bahía de trabajo reubicando la unidad en el estacionamiento hasta el arribo de las piezas. | Entrevista con el cliente (19/10/2026) | RF-05, RF-08.2 |
| RN-07 | Clasificación de vehículos autorizados: El sistema operará exclusivamente con vehículos automotrices ligeros (automóviles particulares, motocicletas y camionetas hasta de 3 toneladas). Se excluyen bicicletas, tráilers y maquinaria pesada. | Entrevista con el cliente (19/10/2026) | RF-03.1 |
| RN-08 | Confirmación manual de citas web: Las solicitudes de cita agendadas desde el portal público ingresarán en estado "Pendiente" y no reservarán espacio en la agenda hasta que la recepcionista las confirme manualmente. | Entrevista con el cliente (19/10/2026) | RF-09 |
| RN-09 | Asignación y colaboración de mecánicos: Cada orden mantendrá un mecánico principal responsable. Otros mecánicos podrán colaborar en el trabajo técnico sin alterar la titularidad de la orden, salvo reasignación formal. | Entrevista con el cliente (19/10/2026) | RF-05 |
| RN-10 | Restricción de entrega y excepción a flotillas: Queda prohibida la entrega física del vehículo con saldo pendiente. Como única excepción, el Gerente podrá autorizar la entrega a crédito para vehículos pertenecientes a flotillas empresariales registradas. | Anteproyecto y entrevista con el cliente | RF-10 |
| RN-11 | Vigencia de cotizaciones: Toda cotización tiene vigencia de 5 días naturales desde su emisión. Una cotización vencida no puede autorizarse; el taller debe emitir una nueva versión. | Anteproyecto | RF-06 |
| RN-12 | Evidencia fotográfica de recepción: Al recibir un vehículo se exigen el checklist completo y al menos 4 fotografías (frente, trasera, costado izquierdo y costado derecho); sin ellas la orden no puede pasar a diagnóstico. | Anteproyecto; el mínimo de 4 fotografías debe validarse con el cliente | RF-04 |
| RN-13 | Garantía de mano de obra: Los trabajos tienen garantía de 30 días naturales sobre la mano de obra, contados desde la entrega del vehículo. | RF-03.2; confirmar la fuente con el cliente | RF-03.2 |
| RN-14 | Medidor de combustible descompuesto: Si el indicador de combustible del tablero no funciona, el nivel no se deja en blanco ni se adivina: se registra como «No verificable», junto con el nivel que declara el cliente, el método de estimación usado (4.7.1) y la aceptación del cliente. El taller no responde por diferencias de combustible en una recepción marcada como «No verificable», salvo lo que él mismo haya medido. | Propuesta del equipo; validar con el cliente | RF-04, HU-01 |
| RN-15 | Operación de contingencia en papel: Si la falta de luz o de internet dura más que la autonomía de los equipos (RNF-08), la operación continúa en la Bitácora de Contingencia impresa (4.7.1) con folios provisionales. Todo lo registrado en papel se captura en el sistema a más tardar 24 horas después de restablecerse el servicio y conserva la hoja física escaneada como evidencia. | Propuesta del equipo; amplía HU-25; validar con el cliente | RNF-08, RNF-09, RF-04, RF-06, RF-10 |
### 4.7.1 Procedimientos de contingencia
Estos procedimientos detallan RN-14 y RN-15. Son operativos: indican qué hace el personal cuando falla el vehículo del cliente o la infraestructura del taller, y qué tendrá que soportar el sistema para que esos casos queden registrados.
A. Vehículo con gasolina pero con el medidor descompuesto (RN-14).
El nivel de combustible al ingreso protege a ambas partes ante reclamos («dejé medio tanque y me lo entregaron en reserva»). Cuando el indicador del tablero no funciona, la recepcionista aplica, en este orden, el primer método que esté disponible y anota cuál usó:
Lectura por OBD-II. Muchas veces solo falla la aguja o el tablero, pero el sensor (flotador) del tanque sigue funcionando. Con el escáner OBD-II del taller se lee el parámetro «Fuel Tank Level Input» (PID 0x2F), que da el porcentaje del tanque, y se convierte al selector de 5 niveles (0–12 % Reserva, 13–37 % 1/4, 38–62 % 1/2, 63–87 % 3/4, 88–100 % Lleno). Se fotografía la pantalla del escáner.
Computadora de viaje. Si el vehículo muestra la autonomía restante (km), se fotografía y se registra como referencia, aclarando que es una estimación del propio vehículo.
Medición física, solo si el trabajo lo requiere. Si la reparación implica bajar o vaciar el tanque (bomba de gasolina, sensor de nivel, fugas), el combustible se extrae con la bomba de trasvase a bidones graduados aprobados para combustible y se registran los litros medidos, con fotografía del bidón. Al terminar, ese mismo volumen se regresa al tanque. No se abre el sistema de combustible solo para medir: es un riesgo de incendio y no forma parte del servicio autorizado.
Declaración del cliente. Si nada de lo anterior es posible, se registra el nivel que dice el cliente con la leyenda «Declarado por el cliente, no verificable».
En todos los casos se fotografía el tablero encendido (evidencia de que el indicador no funciona), se agrega al checklist el hallazgo «Indicador de combustible inoperante» y se le ofrece al cliente diagnosticarlo como servicio adicional. El cliente acepta lo registrado con su firma en la recepción. Al entregar, el nivel se vuelve a medir con el mismo método para que la comparación sea justa. La conversión del porcentaje OBD-II a los 5 niveles es una de las decisiones candidatas a modelarse en DMN (7.9).
Impacto en el sistema: el selector de combustible del wireframe W-01 gana la opción «No verificable», que obliga a capturar el método de estimación (OBD-II, computadora de viaje, medición en litros o declaración del cliente), el valor obtenido y una fotografía del tablero. Pendienteagregar los campos metodo_combustible y litros_medidos a RecepcionVehicular (6.2) y su caso de prueba en la sección 5.
B. Cortes prolongados de luz o de internet (RN-15).
La operación sin conexión de la PWA (HU-25, RNF-08) cubre los cortes cortos. Para los largos se definen tres niveles:
| Nivel | Situación | Cómo se opera |
| --- | --- | --- |
| . Sin internet | Hay luz, pero no hay conexión. | La PWA trabaja con IndexedDB y sincroniza al volver la conexión (RNF-09). El cliente no recibe enlace ni puede autorizar en línea; se le avisa por teléfono. |
| 2. Sin luz | Los equipos funcionan con batería. | Igual que el nivel 1. Se apagan los equipos que no se usen y se reservan las baterías para recepción y diagnóstico. |
| 3. Contingencia en papel | El corte supera 4 horas o la batería de los equipos baja del 20 %. | El Gerente declara la contingencia y anota la hora de inicio en la Bitácora. Todo se registra en papel, como se describe abajo. |
La Bitácora de Contingencia es una libreta o carpeta con formatos impresos y numerados de antemano, que se guarda en recepción. Contiene:
Hoja de recepción: folio provisional C-AAAAMMDD-NN (consecutivo del día, escrito a mano), datos del cliente y del vehículo, kilometraje, nivel de combustible (con la opción «No verificable» de la parte A), checklist de carrocería e interiores y firma del cliente. Las 4 fotografías obligatorias (RN-12) se toman con el celular del taller y se nombran con el folio provisional.
Hoja de diagnóstico y cotización, con el desglose de mano de obra y refacciones.
Hoja de autorización: como no es posible enviar el código 2FA por correo (RN-02), la única autorización válida en contingencia es la firma autógrafa del cliente en presencia del personal, con fecha y hora. No se aceptan autorizaciones por teléfono.
Recibo provisional numerado para los pagos (solo efectivo, porque la terminal bancaria tampoco funciona). Sigue vigente RN-10: no se entrega un vehículo con saldo pendiente.
Registro de movimientos: cambios de estado y de bahía, con hora y nombre de quien los hizo.
Al restablecerse el servicio, el Gerente anota la hora de fin en la Bitácora. En las 24 horas siguientes, la recepcionista captura cada hoja en el sistema: la orden recibe su folio definitivo OS-AAAA-NNNN y conserva el folio provisional como referencia, se adjuntan las fotografías y la hoja escaneada, y las autorizaciones quedan registradas con medio «Firma en papel». El Gerente revisa que no falte ningún folio provisional del consecutivo y firma la Bitácora como conciliada. Las hojas físicas se resguardan con el mismo cuidado que los datos personales del sistema (4.8).
Pendienteagregar al modelo el medio de autorización «Firma en papel» y el campo folio_provisional; diseñar e imprimir los formatos de la Bitácora; validar con el cliente el umbral de 4 horas y el plazo de 24 horas.
## 4.8 Requisitos de protección de datos personales
En cumplimiento con la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP - DOF):
Datos Personales Recabados
El sistema capturará y procesará los siguientes datos de clientes particulares y representantes de flotillas:
Datos de identificación y contacto: Nombre completo, número telefónico celular (WhatsApp/SMS) y correo electrónico.
Datos del vehículo y de la propiedad: Placas, marca, modelo, año, número de serie (VIN - opcional), kilometraje, nivel de combustible, fotografías del estado físico de la unidad, historial de servicios e importes de facturación.
Finalidad del Tratamiento
Finalidades primarias: Identificación del cliente, vinculación del vehículo a la orden de servicio, generación y envío de enlaces temporales de seguimiento, envío de códigos 2FA para validación de presupuestos, cobro, emisión de comprobantes de pago y aplicación de garantías de mano de obra (30 días).
Finalidades secundarias: Recordatorios de mantenimiento preventivo y consulta de historial a solicitud del cliente.
Medidas de Seguridad y Control de Accesos
Control de Acceso Basado en Roles (RBAC): La información personal del cliente solo estará accesible para los roles de Recepcionista y Gerente. Los Mecánicos y Encargados de Almacén únicamente visualizarán datos técnicos del vehículo y requerimientos de refacciones.
Acceso mediante Tokens Temporales: Los clientes accederán a sus cotizaciones y estatus vía tokens dinámicos sin necesidad de almacenar contraseñas de usuarios externos en la base de datos. Protección de Datos en Pruebas: Se garantiza el uso exclusivo de datos sintéticos o ficticios (mock data) durante todas las fases de desarrollo, pruebas y demostraciones académicas, sin almacenar registros reales en los entornos de staging o prueba.
Seguridad en Tránsito: Las comunicaciones entre navegadores móviles, tabletas y servidores se realizarán mediante protocolos cifrados HTTPS (TLS 1.2 o superior).
Borrador del Aviso de Privacidad Simplificado
AVISO DE PRIVACIDAD SIMPLIFICADO
Servicio Automotriz Hermanos Ruiz, S.A. de C.V., con domicilio en las instalaciones operativas del taller, es responsable del tratamiento de los datos personales (contacto, identificación y datos de su vehículo) proporcionados en la recepción.
Sus datos serán utilizados exclusivamente para la apertura de órdenes de servicio, seguimiento en vivo, envío de cotizaciones para su autorización remota o presencial mediante doble verificación (2FA), cobro, entrega y aplicación de garantías. Sus datos no serán transferidos ni compartidos con terceros sin su consentimiento explícito. Para consultar el Aviso de Privacidad Integral o ejercer sus derechos ARCO (Acceso, Rectificación, Cancelación y Oposición), puede acudir a la recepción de nuestro taller o solicitarlo a través de nuestro portal web de atención a clientes.
## 4.9 Casos de uso
Pendiente
Descripción: actores Recepcionista y Jefe de Mecánicos; casos CU-01 Confirmación de cita web, CU-02 Recepción del vehículo y apertura de orden, CU-03 Firma de contrato presencial (2FA), CU-05 Diagnóstico, cotización técnica y asignación de trabajo, CU-07 Finalización de trabajo y sellado de historial, CU-04 Cobro y entrega del vehículo; actor secundario Servicio de correo; «include» de Autenticarse.
Archivo fuente: docs/04-requisitos/casos-uso/taller.puml
Figura 4.2. Diagrama de casos de uso: recepción, taller y cotización. Fuente: docs/04-requisitos/casos-uso/taller.puml
Pendiente
Descripción: actor Cliente; casos CU-09 Solicitud de cita desde la web, CU-10 Consulta del estado del vehículo en vivo, CU-11 Aprobación remota de cotización (2FA), con «extend» Rechazar cotización y Seleccionar opcionales; actor secundario Servicio de correo.
Archivo fuente: docs/04-requisitos/casos-uso/portal-cliente.puml
Figura 4.3. Diagrama de casos de uso: portal del cliente. Fuente: docs/04-requisitos/casos-uso/portal-cliente.puml
Pendiente
Descripción: actores Gerente y Encargado de Almacén; casos CU-12 Monitoreo global del taller y KPIs, CU-13 Autorización de entrega a crédito (flotillas), CU-06 Requisición de refacciones, CU-08 Atender solicitud de refacciones y registrar compra; Gerente especializa a Usuario del personal.
Archivo fuente: docs/04-requisitos/casos-uso/gerencia-almacen.puml
Figura 4.4. Diagrama de casos de uso: gerencia y almacén. Fuente: docs/04-requisitos/casos-uso/gerencia-almacen.puml
CU-01 — Confirmación de cita web
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-01 Confirmación de cita web |
| Actor principal | Recepcionista |
| Actores secundarios | Cliente; servicio de correo electrónico. |
| Descripción breve | Permite revisar solicitudes de citas realizadas desde el sitio web, verificar la disponibilidad del taller y confirmar fecha, hora y bahía preliminar. El sistema actualiza el estado y notifica al cliente. |
| Precondiciones | . El cliente solicitó previamente una cita mediante el sitio web. 2. La solicitud está registrada y pendiente de revisión. 3. La recepcionista dispone de credenciales válidas. |
| Flujo principal | . La recepcionista inicia sesión desde la computadora de mostrador. 2. El sistema valida las credenciales y muestra el menú principal. 3. La recepcionista abre el módulo de Gestión de Citas. 4. El sistema muestra las solicitudes pendientes. 5. La recepcionista selecciona una solicitud y revisa los datos del cliente. 6. El sistema muestra la agenda y la disponibilidad de horarios y bahías. 7. La recepcionista verifica la disponibilidad y selecciona fecha, hora y bahía preliminar. 8. La recepcionista confirma la programación. 9. El sistema actualiza la cita a «Confirmada» y guarda la programación. 10. El sistema envía una notificación al cliente por correo electrónico. 11. El sistema informa a la recepcionista que la cita fue confirmada. |
| Flujos alternos | A1 (paso 7): Horario o fecha sin disponibilidad. El sistema muestra que no hay espacio y permite seleccionar una alternativa; recepción propone la nueva fecha u hora al cliente y continúa con la confirmación. A2 (paso 4): No hay solicitudes pendientes. El sistema informa que la bandeja está vacía y la recepcionista puede salir del módulo. |
| Flujos de excepción | E1 (paso 1): Credenciales incorrectas o cuenta bloqueada. El sistema rechaza el acceso; después de tres intentos fallidos consecutivos bloquea temporalmente la cuenta durante 15 minutos. E2 (paso 9): Error al guardar. El sistema informa que no fue posible actualizar la cita y conserva el estado anterior. E3 (paso 10): Fallo de correo. La cita permanece confirmada y el envío queda para seguimiento o reintento. |
| Postcondiciones | La cita queda registrada con estado «Confirmada» y con fecha y hora asignadas. El sistema conserva el resultado del envío de la notificación. |
| Reglas de negocio | Reglas de 4.7: RN-08 (Confirmación manual de citas web), RN-05 (Capacidad física del taller). Validaciones del caso de uso: • Solo se confirma una solicitud registrada. • La programación debe respetar la disponibilidad de horarios y bahías. • La cita confirmada debe contar con fecha y hora. • La notificación se envía al correo registrado. |
| Requisitos relacionados | RF-09 · HU-04 |
CU-02 — Recepción del vehículo y apertura de orden
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-02 Recepción del vehículo y apertura de orden |
| Actor principal | Recepcionista |
| Actores secundarios | Cliente. |
| Descripción breve | Registra la llegada del vehículo, verifica o captura los datos del cliente y del automóvil, documenta sus condiciones iniciales y abre una orden de servicio para dar seguimiento al trabajo. |
| Precondiciones | . El cliente se presenta físicamente en el taller con su vehículo. 2. La recepcionista tiene acceso autorizado al sistema. 3. El sistema permite registrar clientes, vehículos y órdenes. |
| Flujo principal | . La recepcionista inicia sesión o continúa con una sesión activa. 2. Accede al módulo de Registro de Cliente y Vehículo. 3. Busca al cliente por los datos disponibles. 4. El sistema muestra al cliente y sus vehículos registrados, si existen. 5. La recepcionista verifica o registra los datos del cliente y del vehículo: placas, marca, modelo y VIN. 6. Accede al módulo de Check-in y Registro de Entrada. 7. El sistema solicita los datos iniciales del vehículo. 8. La recepcionista registra kilometraje y nivel de combustible. 9. Completa la lista de inspección inicial, incluyendo herramientas y llanta de refacción, entre otros elementos definidos por el taller. 10. Toma o carga fotografías de la carrocería para documentar daños previos. 11. Revisa los datos y selecciona «Abrir Orden de Servicio». 12. El sistema valida los datos obligatorios y registra la orden con estado «Abierta». 13. El sistema genera un enlace seguro asociado a la orden para el cliente. 14. El sistema confirma la apertura de la orden. |
| Flujos alternos | A1 (paso 3): Cliente no registrado. La recepcionista captura sus datos y continúa con el registro del vehículo. A2 (paso 5): Vehículo no registrado. La recepcionista captura sus datos y lo vincula con el cliente. A3 (paso 10): No se observan daños visibles. La recepcionista registra el resultado de la inspección y continúa. |
| Flujos de excepción | E1 (paso 5): Datos obligatorios incompletos. El sistema identifica los campos faltantes y no permite guardar hasta completarlos. E2 (paso 5): Vehículo con orden previa abierta. Si las placas corresponden a una orden activa, el sistema muestra el folio y dirige a la orden existente para actualizarla o cerrarla antes de abrir otra. E3 (paso 10): Fotografía inválida o mayor a 10 MB. El sistema muestra un error de formato o tamaño y solicita seleccionar una imagen compatible o comprimida. E4 (paso 12): Error al abrir la orden. El sistema informa que la operación no se completó y no debe mostrar una orden como abierta si no fue guardada. |
| Postcondiciones | Quedan registrados el check-in y la orden de servicio en estado «Abierta»; el vehículo se asocia al cliente y se genera el enlace seguro correspondiente. |
| Reglas de negocio | Reglas de 4.7: RN-12 (Evidencia fotográfica de recepción), RN-07 (Clasificación de vehículos autorizados), RN-01 (Expiración y vigencia de enlaces). Validaciones del caso de uso: • Cada vehículo debe estar asociado con un cliente. • Se registra kilometraje y nivel de combustible al ingreso. • La inspección inicial documenta el estado del vehículo. • La orden requiere los datos obligatorios completos. • La orden tiene folio único y estado inicial «Abierta». • El enlace seguro debe corresponder a la orden correcta. |
| Requisitos relacionados | RF-02.1, RF-03.1, RF-04 · HU-01, HU-05, HU-06 |
CU-03 — Firma de contrato presencial (2FA)
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-03 Firma de contrato presencial (2FA) |
| Actor principal | Recepcionista |
| Actores secundarios | Cliente; servicio de correo electrónico. |
| Descripción breve | Formaliza en el mostrador la autorización de una cotización técnica mediante un código de un solo uso enviado al correo registrado del cliente. |
| Precondiciones | . El jefe de mecánicos ya generó el diagnóstico y la cotización técnica. 2. La cotización está asociada a una orden y disponible para revisión. 3. El cliente decide autorizar de forma presencial. 4. El cliente tiene un correo registrado y accesible. 5. La recepcionista tiene acceso al sistema. |
| Flujo principal | . El clnte comunica que desea autorizar presencialmente la cotización. 2. La recepcionista abre el módulo de Firma de Contrato Presencial. 3. El sistema muestra las órdenes y cotizaciones pendientes de autorización. 4. La recepcionista selecciona la orden correspondiente. 5. El sistema muestra el desglose de la cotización. 6. El cliente revisa el alcance y el importe cotizado. 7. La recepcionista selecciona «Enviar Código 2FA». 8. El sistema genera un código de verificación y lo envía al correo registrado. 9. El cliente recibe el código y se lo proporciona a la recepcionista. 10. La recepcionista introduce los seis dígitos. 11. La recepcionista selecciona «Validar y Firmar». 12. El sistema comprueba que el código sea correcto, vigente y no utilizado. 13. El sistema registra la autorización y cambia la orden a «Autorizada». 14. El sistema muestra la confirmación de la operación. |
| Flujos alternos | A1 (paso 6): El cliente solicita aclaraciones. La recepcionista aclara la información disponible o consulta al jefe de mecánicos; después el cliente puede continuar o rechazar la cotización. A2 (paso 9): El cliente no recibe el código. Se verifica el correo y el estado del envío; si está habilitado, se reenvía el código. A3 (paso 10): Si el sistema lo permite, el cliente introduce personalmente el código. |
| Flujos de excepción | E1 (paso 8): Fallo de envío. El sistema informa que no pudo enviar el código y no permite autorizar hasta completar la verificación. E2 (paso 12): Código incorrecto o expirado tras cinco minutos. El sistema lo rechaza y permite introducir un código vigente o solicitar un reenvío. E3 (paso 12): Límite de intentos excedido. El sistema bloquea temporalmente la validación o exige iniciar nuevamente el proceso. E4 (paso 13): Error al registrar la autorización. La orden conserva el estado anterior hasta que se registre correctamente. E5: El cliente rechaza la cotización. La recepcionista registra el rechazo; la orden queda «Cancelada/Rechazada» y se coordina el cobro de revisión y la entrega del vehículo sin reparar, si aplica. |
| Postcondiciones | Si la validación tiene éxito, la autorización queda registrada y la orden cambia a «Autorizada». Si el cliente rechaza la cotización, se registra el rechazo y no continúa la reparación cotizada. |
| Reglas de negocio | Reglas de 4.7: RN-02 (Doble verificación en autorizaciones), RN-03 (Selección granular de rubros), RN-11 (Vigencia de cotizaciones). Validaciones del caso de uso: • La cotización debe haberse generado y estar asociada a la orden. • El cliente debe revisar la cotización antes de autorizarla. • El código es de un solo uso y tiene vigencia definida de cinco minutos, según la especificación recibida. • Se rechazan códigos incorrectos, vencidos o ya utilizados. • La orden solo cambia a «Autorizada» después de validar y registrar la aceptación. |
| Requisitos relacionados | RF-06 · HU-12, HU-14 |
CU-04 — Cobro y entrega del vehículo
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-04 Cobro y entrega del vehículo |
| Actor principal | Recepcionista |
| Actores secundarios | Cliente; gerente (cuando se requiera autorización de crédito); sistema de registro de pagos. |
| Descripción breve | Registra el pago de la orden, emite el comprobante, entrega las llaves al cliente y cierra la orden de servicio cuando se cumplen las condiciones de salida. |
| Precondiciones | . El jefe de mecánicos marcó el trabajo como «Terminado» y el vehículo está listo para entrega. 2. Existe una orden de servicio registrada. 3. La recepcionista tiene permiso para realizar el cobro y registrar la entrega. |
| Flujo principal | . El cliente acude al taller a recoger su vehículo. 2. La recepcionista abre el módulo de Cobro y Entrega. 3. El sistema muestra el saldo pendiente de la orden. 4. La recepcionista verifica el importe, registra el pago y emite el comprobante. 5. La recepcionista entrega las llaves al cliente. 6. La recepcionista selecciona «Registrar Entrega». 7. El sistema guarda la orden en el Historial de Servicio del vehículo y cambia el estado a «Cerrada». 8. El sistema confirma el cierre de la orden. |
| Flujos alternos | A1: Entrega a crédito para flotilla empresarial. Si el vehículo pertenece a una flotilla y queda saldo pendiente, la recepcionista solicita autorización al gerente. Si el gerente autoriza, se continúa con el registro de entrega sin pago inmediato de contado (véase CU-13). A2: El cliente paga el saldo pendiente y se reanuda el proceso de cobro y entrega. |
| Flujos de excepción | E1: Saldo pendiente sin autorización de crédito. El sistema bloquea la entrega y muestra que se requiere liquidación completa o autorización expresa de Gerencia. E2: Sesión expirada por más de 30 minutos de inactividad. El sistema redirige al inicio de sesión y conserva el borrador del formulario de cobro; tras autenticarse, la recepcionista retoma el proceso. |
| Postcondiciones | La orden queda «Cerrada», el pago queda registrado, se emite un comprobante y la orden se conserva en el historial de servicio del vehículo. |
| Reglas de negocio | Reglas de 4.7: RN-10 (Restricción de entrega y excepción a flotillas), RN-13 (Garantía de mano de obra), RN-01 (Expiración y vigencia de enlaces). Validaciones del caso de uso: • No se entrega un vehículo con saldo pendiente salvo autorización expresa de Gerencia para crédito de flotilla. • El pago debe registrarse en el sistema y producir un comprobante. • La orden se cierra después de registrar la entrega. • El cierre debe quedar en el historial de servicio del vehículo. |
| Requisitos relacionados | RF-02.2, RF-03.2, RF-10 · HU-21, HU-23 |
CU-05 — Diagnóstico, cotización técnica y asignación de trabajo
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-05 Diagnóstico, cotización técnica y asignación de trabajo |
| Actor principal | Jefe de Mecánicos (líder técnico) |
| Actores secundarios | Recepcionista; mecánico asignado; sistema de agenda de bahías. |
| Descripción breve | Permite inspeccionar técnicamente un vehículo con orden abierta, elaborar el diagnóstico y la cotización de mano de obra y refacciones, y asignar una bahía y un mecánico. |
| Precondiciones | . Existe una orden de servicio en estado «Abierta». 2. El jefe de mecánicos tiene acceso autorizado desde la tableta del taller. 3. Hay información suficiente para identificar la orden y el vehículo. |
| Flujo principal | . El jefe de mecánicos inicia sesión en la tableta del taller. 2. Revisa las órdenes abiertas y localiza el vehículo en el área de recepción. 3. Inspecciona físicamente el automóvil. 4. Abre el módulo de Diagnóstico y Cotización Técnica. 5. Registra el diagnóstico y desglosa la mano de obra estimada y las refacciones necesarias. 6. Consulta el Tablero de Bahías y Mecánicos. 7. Asigna la orden a una bahía disponible y a un mecánico de su equipo. 8. Selecciona «Guardar Diagnóstico». 9. El sistema guarda el diagnóstico y cambia la orden a «Diagnosticada». 10. El sistema deja disponible la cotización para que se gestione la autorización del cliente. |
| Flujos alternos | A1 (paso 7): Las cuatro bahías están ocupadas. El sistema muestra «Capacidad máxima alcanzada (4/4 bahías ocupadas)» y coloca la orden en la lista de espera; al liberarse una bahía, el jefe retoma la asignación. A2: La orden se diagnostica pero queda en espera de asignación hasta que exista capacidad disponible. |
| Flujos de excepción | E1: Credenciales incorrectas. El sistema rechaza el acceso y permite volver a intentar. E2: Pérdida de Wi‑Fi o sesión pausada al guardar. El sistema informa que no hay conexión o que la sesión se pausó, conserva una copia local si está disponible y solicita volver a iniciar sesión al restablecer la red. E3: Durante la reparación se detecta una falla adicional cuyo costo incrementa más del 10 % respecto de lo autorizado. El sistema detiene el avance, cambia la orden a «Pendiente de Re-cotización» y deshabilita nuevas requisiciones hasta obtener una nueva autorización mediante 2FA. |
| Postcondiciones | El diagnóstico y la cotización quedan guardados; la orden cambia a «Diagnosticada». La asignación queda establecida o la orden queda en lista de espera si todas las bahías están ocupadas. |
| Reglas de negocio | Reglas de 4.7: RN-05 (Capacidad física del taller), RN-09 (Asignación y colaboración de mecánicos), RN-04 (Re-cotización obligatoria por sobrecostos), RN-11 (Vigencia de cotizaciones). Validaciones del caso de uso: • El diagnóstico se registra sobre una orden existente en estado «Abierta». • La asignación física requiere una bahía disponible y un mecánico asignado. • El taller dispone de cuatro bahías; si todas están ocupadas, se utiliza lista de espera. • Un incremento superior al 10 % del costo autorizado requiere re-cotización y nueva autorización del cliente antes de solicitar refacciones adicionales. |
| Requisitos relacionados | RF-05, RF-06, RF-07 · HU-07, HU-08, HU-09, HU-12, HU-16 |
CU-06 — Requisición de refacciones
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-06 Requisición de refacciones |
| Actor principal | Jefe de Mecánicos (líder técnico) |
| Actores secundarios | Encargado de almacén; cliente (cuando se requiere nueva autorización). |
| Descripción breve | Registra y envía al almacén la solicitud de refacciones necesarias para ejecutar una reparación autorizada. |
| Precondiciones | . La orden está autorizada por el cliente. 2. La reparación se encuentra en proceso. 3. El jefe de mecánicos tiene acceso a la tableta y a la orden activa. |
| Flujo principal | . El jefe de mecánicos inicia sesión y abre el módulo de Requisición de Refacciones en la tableta. 2. Selecciona la orden de servicio activa. 3. Ingresa las refacciones requeridas para realizar el trabajo autorizado. 4. Revisa la lista de piezas solicitadas. 5. Selecciona «Enviar Solicitud a Almacén». 6. El sistema registra la requisición y notifica al encargado de almacén. 7. El encargado de almacén puede consultar la solicitud pendiente para atenderla. |
| Flujos alternos | A1: Si las piezas solicitadas corresponden a una re-cotización previamente autorizada por el cliente, el jefe registra la requisición adicional y continúa el flujo normal. |
| Flujos de excepción | E1: Se detecta durante la reparación una falla oculta que incrementa el costo en más del 10 % del importe autorizado. El sistema detiene la orden, la cambia a «Pendiente de Re-cotización» y deshabilita la solicitud de nuevas refacciones. El jefe prepara la cotización complementaria; tras una nueva autorización 2FA por Recepción o por la Web, puede volver a requisar. E2: Pérdida de conexión o sesión pausada al guardar. El sistema muestra el aviso correspondiente y, si está disponible, conserva una copia local para reintentar cuando se restablezca la conexión. |
| Postcondiciones | La requisición queda registrada y disponible para el encargado de almacén, que recibe una notificación. Si se requiere re-cotización, las nuevas piezas quedan bloqueadas hasta obtener autorización. |
| Reglas de negocio | Reglas de 4.7: RN-04 (Re-cotización obligatoria por sobrecostos), RN-06 (Reubicación por espera de refacciones). Validaciones del caso de uso: • La requisición ordinaria corresponde a una orden autorizada y en proceso de reparación. • Las piezas adicionales asociadas a un aumento superior al 10 % requieren re-cotización y autorización 2FA. • La solicitud enviada debe quedar asociada a la orden de servicio. |
| Requisitos relacionados | RF-08.1 · HU-10 |
CU-07 — Finalización de trabajo y sellado de historial
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-07 Finalización de trabajo y sellado de historial |
| Actor principal | Jefe de Mecánicos (líder técnico) |
| Actores secundarios | Mecánico asignado; cliente; servicio de notificaciones. |
| Descripción breve | Registra las notas técnicas finales, verifica que las tareas autorizadas estén completadas y finaliza el trabajo para habilitar la entrega del vehículo. |
| Precondiciones | . El mecánico asignado terminó físicamente las reparaciones. 2. La orden está en reparación y cuenta con diagnóstico y autorización del cliente. 3. El jefe de mecánicos tiene acceso al sistema desde la tableta. |
| Flujo principal | . El jefe de mecánicos inicia sesión en la tableta y supervisa el vehículo. 2. Abre el módulo de Cierre Técnico y Sellado de Historial. 3. Redacta las notas técnicas finales del trabajo realizado y verifica su correspondencia con lo autorizado por el cliente. 4. Marca las tareas realizadas como completadas. 5. Selecciona «Finalizar Trabajo». 6. El sistema valida el cierre técnico. 7. El sistema cambia el estado de la orden a «Lista para Entrega». 8. El sistema envía una notificación automática al cliente. |
| Flujos alternos | A1: Si faltan tareas por marcar, el jefe revisa el estado de las reparaciones, completa las tareas correspondientes y vuelve a intentar finalizar el trabajo. |
| Flujos de excepción | E1: El jefe intenta cerrar la orden con tareas autorizadas pendientes. El sistema muestra «Existen tareas autorizadas pendientes por marcar como concluidas» y no finaliza la orden. E2: La sesión se pausa o se pierde la conexión Wi‑Fi antes de guardar. El sistema informa el problema y permite reanudar el proceso tras recuperar conexión y autenticarse. |
| Postcondiciones | Las notas técnicas y las tareas completadas quedan registradas; la orden cambia a «Lista para Entrega» y se envía la notificación al cliente. |
| Reglas de negocio | Reglas de 4.7: RN-03 (Selección granular de rubros), RN-13 (Garantía de mano de obra). Validaciones del caso de uso: • Solo se finaliza técnicamente una reparación concluida. • Las tareas completadas deben corresponder con lo autorizado por el cliente. • No se cambia la orden a «Lista para Entrega» si quedan tareas autorizadas pendientes. • La finalización genera una notificación al cliente. |
| Requisitos relacionados | RF-03.2, RF-05 · HU-20 |
CU-08 — Atender solicitud de refacciones y registrar compra
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-08 Atender solicitud de refacciones y registrar compra |
| Actor principal | Encargado de Almacén |
| Actores secundarios | Jefe de Mecánicos; proveedor local; sistema de inventario. |
| Descripción breve | Atiende una solicitud de refacciones, contacta a un proveedor, registra la compra y el ticket, y actualiza la disponibilidad de las piezas para que continúe la reparación. |
| Precondiciones | . El jefe de mecánicos envió una solicitud de refacciones asociada a una orden. 2. El encargado de almacén tiene acceso a la computadora y al sistema. |
| Flujo principal | . El encargado de almacén inicia sesión en la computadora de almacén. 2. Abre Solicitudes Pendientes y selecciona el pedido recibido. 3. Consulta el Directorio de Proveedores Locales y localiza un proveedor. 4. Realiza la compra o pedido por teléfono o correo con el proveedor seleccionado. 5. Abre el módulo de Registro de Compra y Ticket. 6. Captura los costos de las piezas, el proveedor y la fecha de recepción. 7. Selecciona «Confirmar Compra y Generar Ticket». 8. El sistema genera el historial de compra, descuenta del inventario si aplica y marca la refacción como «Recibida». 9. El sistema deja la solicitud registrada para que el taller continúe la reparación. |
| Flujos alternos | A1: Si existe stock local disponible, el encargado puede registrar el surtido de las piezas correspondientes sin efectuar una nueva compra, actualizando el inventario y la solicitud según corresponda. |
| Flujos de excepción | E1: No hay existencia en almacén y ningún proveedor local tiene la pieza para entrega inmediata. El encargado selecciona «Sin disponibilidad de proveedor»; el sistema cambia la orden a «Detenida por Refacción» y avisa al jefe de mecánicos y al portal del cliente. Cuando se confirma la llegada de la pieza, el encargado registra el pedido y marca las piezas como recibidas. E2: Credenciales incorrectas o tres intentos fallidos. El sistema rechaza el acceso y bloquea temporalmente la cuenta conforme a la política descrita. E3: Cuenta abierta en otro dispositivo o sesión expirada. El sistema cierra la sesión anterior o informa que la sesión expiró. |
| Postcondiciones | La compra queda en el historial, el ticket se genera, el inventario se actualiza si aplica y las refacciones quedan marcadas como «Recibida»; si no hay disponibilidad, la orden queda «Detenida por Refacción». |
| Reglas de negocio | Reglas de 4.7: RN-06 (Reubicación por espera de refacciones). Validaciones del caso de uso: • Toda compra debe asociarse a la solicitud y a su orden de servicio. • Se registra el proveedor, los costos y la fecha de recepción. • El inventario solo se descuenta o actualiza según aplique al movimiento registrado. • La falta de pieza disponible debe comunicarse al taller y al portal del cliente. |
| Requisitos relacionados | RF-08.2, RF-08.3 · HU-17, HU-18 |
CU-09 — Solicitud de cita desde la web
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-09 Solicitud de cita desde la web |
| Actor principal | Cliente |
| Actores secundarios | Sistema web; recepcionista (revisa posteriormente la solicitud). |
| Descripción breve | Permite que el cliente solicite una cita en el sitio web público sin crear una cuenta ni iniciar sesión, proporcionando sus datos, los de su vehículo y el horario deseado. |
| Precondiciones | . El cliente puede acceder a la página web pública del taller. 2. El servicio web de solicitud de citas está disponible. |
| Flujo principal | . El cliente abre la pantalla de Solicitud de Cita desde el sitio web, sin registrarse ni introducir contraseña. 2. Llena sus datos personales y la información de su automóvil. 3. Selecciona la fecha y hora deseadas. 4. Revisa la información y selecciona «Solicitar Cita». 5. El sistema registra la solicitud como pendiente de revisión. 6. El sistema muestra un mensaje que indica que Recepción revisará la petición. |
| Flujos alternos | A1: Si la fecha u hora solicitada no tiene espacio disponible, Recepción revisa la solicitud y puede proponer al cliente un día u horario alternativo antes de confirmar la cita. |
| Flujos de excepción | E1: No se puede enviar o registrar la solicitud. El material proporcionado no especifica el mensaje ni el procedimiento concreto de recuperación; la solicitud no debe considerarse recibida hasta que el sistema confirme el registro. |
| Postcondiciones | La solicitud queda registrada para revisión de Recepción y el cliente recibe confirmación en pantalla de que su petición fue enviada. |
| Reglas de negocio | Reglas de 4.7: RN-08 (Confirmación manual de citas web). Validaciones del caso de uso: • El cliente puede solicitar la cita sin usuario ni contraseña. • La solicitud requiere datos del cliente, información del vehículo y fecha/hora deseadas. • Enviar una solicitud no equivale a confirmar la cita; Recepción debe revisarla. |
| Requisitos relacionados | RF-09 · HU-03 |
CU-10 — Consulta del estado del vehículo en vivo
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-10 Consulta del estado del vehículo en vivo |
| Actor principal | Cliente |
| Actores secundarios | Sistema web; servicio de generación y validación de enlaces seguros. |
| Descripción breve | Permite consultar el avance del automóvil desde un teléfono mediante un enlace seguro asociado a la orden, sin requerir usuario, contraseña ni descarga de una aplicación. |
| Precondiciones | . El vehículo fue recibido en el taller y cuenta con una orden de servicio. 2. El cliente recibió por correo o SMS el enlace seguro correspondiente. |
| Flujo principal | . El cliente abre desde su teléfono el enlace seguro recibido. 2. El sistema valida automáticamente el token incluido en el enlace. 3. El sistema muestra la pantalla de Seguimiento en Vivo. 4. El cliente visualiza la barra de progreso y el estado actual del vehículo. 5. El sistema presenta el avance disponible, que puede incluir Recepción, Diagnóstico, En Reparación y Listo. |
| Flujos alternos | A1: El cliente vuelve a abrir el mismo enlace vigente para consultar el estado actualizado de la orden. |
| Flujos de excepción | E1: El enlace ha expirado o el token fue alterado. El sistema bloquea el acceso y muestra: «Su enlace de acceso ha expirado o es inválido. Por favor, solicite un nuevo enlace de seguimiento a la recepción del taller». |
| Postcondiciones | El cliente visualiza el estado asociado a la orden si el token es válido. No se modifican los datos ni el estado de la orden mediante esta consulta. |
| Reglas de negocio | Reglas de 4.7: RN-01 (Expiración y vigencia de enlaces). Validaciones del caso de uso: • El acceso del cliente se realiza mediante un token seguro, sin usuario ni contraseña. • Un enlace expirado o alterado no debe permitir consultar la información. • La información mostrada corresponde a la orden asociada al enlace. |
| Requisitos relacionados | RF-02.1 · HU-28 |
CU-11 — Aprobación remota de cotización (2FA)
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-11 Aprobación remota de cotización (2FA) |
| Actor principal | Cliente |
| Actores secundarios | Recepcionista; servicio de correo electrónico; sistema web. |
| Descripción breve | Permite que el cliente revise y autorice a distancia la cotización técnica mediante un enlace seguro y un código 2FA de seis dígitos enviado por correo electrónico. |
| Precondiciones | . El vehículo ya fue diagnosticado. 2. La cotización fue enviada al cliente mediante un enlace seguro. 3. El enlace está vigente y asociado a la orden correcta. 4. El cliente puede acceder al correo registrado. |
| Flujo principal | . El cliente abre el enlace dinámico desde su teléfono. 2. El sistema valida el enlace y muestra el desglose de mano de obra y refacciones. 3. El cliente revisa los conceptos y el importe cotizado. 4. Presiona «Solicitar Código 2FA para Autorizar». 5. El sistema envía por correo un código de verificación de seis dígitos. 6. El cliente introduce el código en la página web. 7. Presiona «Aceptar y Autorizar». 8. El sistema valida el código y registra el monto, la fecha y la hora de la autorización. 9. El sistema cambia la orden a «Autorizada» y muestra el resultado. |
| Flujos alternos | A1 (paso 3): El cliente no está de acuerdo con el costo y selecciona «Rechazar Cotización». El sistema solicita confirmar el rechazo; tras la confirmación cambia la orden a «Cancelada/Rechazada», notifica a Recepción para coordinar la entrega del vehículo sin reparar y finaliza la sesión web. |
| Flujos de excepción | E1: Enlace expirado o token alterado. El sistema bloquea el acceso e indica al cliente que solicite un nuevo enlace a Recepción. E2 (paso 8): Código 2FA incorrecto o expirado después de cinco minutos. El sistema rechaza la autorización e indica que debe solicitarse un código nuevo. E3: El código no llega al correo. El material indica que el cliente debe solicitar un nuevo código; el flujo no concluye hasta que la verificación sea satisfactoria. |
| Postcondiciones | Si la autorización es válida, queda registrada la cotización aprobada y la orden pasa a «Autorizada». Si el cliente la rechaza, la orden queda «Cancelada/Rechazada» y Recepción recibe aviso para coordinar la entrega sin reparar. |
| Reglas de negocio | Reglas de 4.7: RN-02 (Doble verificación en autorizaciones), RN-03 (Selección granular de rubros), RN-11 (Vigencia de cotizaciones). Validaciones del caso de uso: • La cotización debe estar asociada a una orden diagnosticada. • El enlace seguro debe ser vigente y válido. • El código 2FA es de seis dígitos y su vigencia indicada es de cinco minutos. • La orden solo se autoriza después de validar el código y registrar el consentimiento del cliente. • El rechazo confirmado debe notificarse a Recepción. |
| Requisitos relacionados | RF-02.1, RF-06 · HU-02, HU-13, HU-14, HU-15 |
CU-12 — Monitoreo global del taller y KPIs
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-12 Monitoreo global del taller y KPIs |
| Actor principal | Gerente (dueño) |
| Actores secundarios | Sistema de gestión del taller. |
| Descripción breve | Proporciona al gerente un tablero general para visualizar indicadores operativos y financieros del taller, incluyendo ocupación de bahías, órdenes abiertas, tiempos promedio e ingresos acumulados. |
| Precondiciones | . El gerente requiere revisar la operación general. 2. Cuenta con perfil gerencial y credenciales válidas. 3. Existen datos operativos registrados en el sistema. |
| Flujo principal | . El gerente inicia sesión en su computadora o teléfono con el perfil gerencial. 2. El sistema valida las credenciales y abre el Dashboard General de Control. 3. El gerente consulta la ocupación de las cuatro bahías. 4. El gerente visualiza las órdenes abiertas. 5. El gerente consulta los tiempos promedio de estancia. 6. El gerente visualiza los ingresos acumulados y los indicadores disponibles en tiempo real. |
| Flujos alternos | A1: El gerente consulta el tablero desde otro dispositivo autorizado y revisa los mismos indicadores según los permisos de su perfil. |
| Flujos de excepción | E1: Credenciales incorrectas u olvido de contraseña. El sistema muestra un error y permite iniciar el flujo de recuperación por correo y verificación de seguridad. E2: Cambio de red o inactividad. Para proteger la información operativa y financiera, el sistema requiere reautenticación mediante huella o contraseña, de acuerdo con el flujo descrito en el material. |
| Postcondiciones | El gerente visualiza los indicadores disponibles del taller. La consulta no modifica las órdenes ni los datos operativos. |
| Reglas de negocio | Sin regla de 4.7 específica. Validaciones del caso de uso: • Solo un perfil gerencial autorizado puede consultar el Dashboard General de Control. • Los indicadores mostrados deben basarse en los datos registrados en el sistema. • Tras inactividad o cambio de red, el sistema puede exigir reautenticación para proteger la información. |
| Requisitos relacionados | RF-11 · HU-29 |
CU-13 — Autorización de entrega a crédito (flotillas)
| Campo | Contenido |
| --- | --- |
| ID y nombre | CU-13 Autorización de entrega a crédito (flotillas) |
| Actor principal | Gerente (dueño) |
| Actores secundarios | Recepcionista; cliente empresarial/flotilla; sistema de control de crédito. |
| Descripción breve | Permite decidir si se libera a crédito un vehículo de una flotilla empresarial que terminó su reparación pero conserva saldo pendiente, con revisión de la línea de crédito de la empresa. |
| Precondiciones | . El vehículo de una flotilla empresarial terminó su reparación. 2. La orden conserva saldo pendiente. 3. Recepción solicitó autorización de crédito para liberar el vehículo. 4. El gerente tiene un perfil autorizado para aprobar excepciones. |
| Flujo principal | . La recepcionista solicita al gerente autorización de entrega a crédito. 2. El gerente inicia sesión y abre Aprobación de Créditos y Excepciones. 3. Selecciona la orden correspondiente a la flotilla empresarial. 4. El sistema muestra la información de la orden y la línea de crédito aprobada. 5. El gerente revisa la información de crédito y decide autorizar la entrega. 6. El gerente selecciona «Autorizar Entrega a Crédito». 7. El sistema registra la autorización y habilita a Recepción para entregar el vehículo sin pago inmediato de contado. |
| Flujos alternos | A1: La flotilla excede su límite autorizado o presenta facturas vencidas. El sistema muestra una alerta con el saldo vencido y pregunta si el gerente desea forzar la autorización bajo su responsabilidad. • Si acepta, el sistema registra la excepción gerencial y habilita la entrega. • Si rechaza, la entrega continúa bloqueada y se exige liquidar el saldo pendiente. |
| Flujos de excepción | E1: Credenciales gerenciales incorrectas o cuenta inaccesible. El gerente debe corregir los datos o recuperar la contraseña por correo antes de continuar. E2: El sistema detecta que la empresa excedió el límite de crédito. Si no existe autorización expresa del gerente, la entrega permanece bloqueada. |
| Postcondiciones | Si se autoriza, queda registrada la excepción de crédito y Recepción puede continuar con la entrega. Si se deniega, el vehículo no se libera hasta liquidar el saldo o conseguir autorización válida. |
| Reglas de negocio | Reglas de 4.7: RN-10 (Restricción de entrega y excepción a flotillas). Validaciones del caso de uso: • Esta excepción aplica a vehículos de flotillas empresariales. • Se debe revisar la línea de crédito antes de autorizar. • El gerente puede forzar una autorización con límite excedido bajo su responsabilidad, según el flujo definido. • Si el gerente rechaza la excepción, la entrega permanece bloqueada y se exige pago del saldo. |
| Requisitos relacionados | RF-10 · HU-22 |
### 4.9.1 Flujos transversales de autenticación y sesión
Estos flujos se presentan como apoyo transversal de seguridad, no como casos de uso de negocio adicionales a los 13 anteriores. Los comportamientos se transcriben y ordenan a partir del material entregado.
FT-01 — Autenticación y sesión de Recepcionista
| Campo | Contenido |
| --- | --- |
| Actor / flujo | Actor: Recepcionista Precondición: la recepcionista intenta acceder desde la computadora de mostrador. Flujo normal: ingresa usuario/correo y contraseña; el sistema valida los datos y muestra la pantalla principal de Recepción. Excepciones: (1) Credenciales incorrectas: muestra «Usuario o contraseña incorrectos. Intentos restantes: 2». (2) Tres intentos fallidos consecutivos: bloquea la cuenta por 15 minutos y muestra aviso de bloqueo. (3) Recuperación: solicita correo corporativo; si no existe muestra «Correo no registrado»; si existe, envía enlace/token válido por 15 minutos; la recepcionista restablece la contraseña y vuelve al login. (4) Más de 30 minutos de inactividad: expira la sesión, guarda el borrador del formulario actual, redirige al login y muestra aviso de sesión expirada. |
FT-02 — Autenticación y sesión del Jefe de Mecánicos
| Campo | Contenido |
| --- | --- |
| Actor / flujo | Actor: Jefe de Mecánicos Precondición: el jefe intenta acceder desde la tableta del taller. Flujo normal: introduce usuario y contraseña y accede al tablero del taller. Excepciones: (1) Error de captura o credenciales: se rechaza el acceso y se permite reintentar. (2) Recuperación: ingresa el correo, recibe un token de restablecimiento, crea una nueva contraseña y vuelve al login. (3) Pérdida de Wi‑Fi o cierre por inactividad durante el guardado: muestra «Sin conexión / Sesión pausada. Se guardó una copia local. Vuelva a iniciar sesión al restablecer la red». |
FT-03 — Autenticación y sesión del Encargado de Almacén
| Campo | Contenido |
| --- | --- |
| Actor / flujo | Actor: Encargado de Almacén Precondición: el almacenista intenta acceder a la terminal de inventarios. Flujo normal: introduce credenciales y accede a la pantalla de solicitudes. Excepciones: (1) Tres contraseñas fallidas: bloqueo temporal y notificación al gerente/sistema. (2) Recuperación por correo corporativo y restablecimiento de contraseña. (3) Inicio en dos computadoras o expiración de sesión por inactividad: el sistema cierra la sesión anterior y muestra «Se ha iniciado sesión en otro dispositivo o la sesión ha expirado». |
FT-04 — Acceso del Cliente mediante enlace seguro y token
| Campo | Contenido |
| --- | --- |
| Actor / flujo | Actor: Cliente Precondición: el cliente intenta consultar el estado del vehículo o autorizar una cotización desde el celular. No requiere usuario ni contraseña: la validación se realiza con el token del enlace único. Excepción: enlace expirado (el enlace expira al entregar y saldar el vehículo, RN-01) o token alterado. El sistema bloquea el acceso e indica: «Su enlace de acceso ha expirado o es inválido. Por favor, solicite un nuevo enlace de seguimiento a la recepción del taller». Cotización vencida: si pasaron los 5 días naturales de vigencia (RN-11), el enlace sigue activo, pero la cotización se muestra como «Vencida» y no puede autorizarse; el cliente pide una nueva versión a Recepción. Excepción 2FA: código incorrecto o expirado después de cinco minutos. El sistema rechaza la autorización y solicita un nuevo código. El cliente también puede rechazar expresamente la cotización; tras confirmar, el sistema cambia la orden a «Cancelada/Rechazada», notifica a Recepción y finaliza la sesión web. |
FT-05 — Autenticación y sesión del Gerente
| Campo | Contenido |
| --- | --- |
| Actor / flujo | Actor: Gerente (dueño) Precondición: el gerente intenta ingresar al dashboard desde su laptop o celular. Flujo normal: inicia sesión con sus credenciales y accede al Dashboard General. Excepciones: (1) Credenciales olvidadas o incorrectas: puede recuperar la cuenta mediante correo personal/gerencial, completar la verificación de seguridad, cambiar la contraseña y volver a iniciar sesión. (2) Cambio de red Wi‑Fi o inactividad: el sistema exige reautenticación mediante huella o contraseña para proteger métricas financieras y operativas. |
## 4.10 Prototipos de baja fidelidad
Un wireframe por pantalla del flujo núcleo, con la historia y el caso de uso que representa.
Pendiente
Descripción: búsqueda por teléfono o placas, datos del vehículo, kilometraje, selector de combustible de 5 niveles, checklist de carrocería e interiores, 4 casillas de fotografía obligatoria (frente, trasera, izquierda, derecha) con indicador de completas, botón «Abrir orden» y aviso rojo «Sin bahías disponibles».
Archivo fuente: docs/04-requisitos/wireframes/w01-recepcion.png
Figura 4.5. Wireframe W-01: recepción del vehículo (HU-01, HU-06, HU-07; CU-02). Fuente: docs/04-requisitos/wireframes/w01-recepcion.png
Pendiente
Descripción: las 4 bahías como tarjetas grandes (libre/ocupada, folio, placas), selector de mecánico responsable y colaboradores, campo de diagnóstico con dictado y botón «Guardar diagnóstico» de al menos 48 x 48 px (RNF-02).
Archivo fuente: docs/04-requisitos/wireframes/w02-tableta-taller.png
Figura 4.6. Wireframe W-02: tableta del jefe de mecánicos (HU-08, HU-09, HU-11; CU-05). Fuente: docs/04-requisitos/wireframes/w02-tableta-taller.png
Pendiente
Descripción: tabla de conceptos (concepto, tipo, cantidad, precio, opcional), total, fecha de vencimiento a 5 días y botón «Enviar al cliente»; en una re-cotización, el porcentaje de incremento y el aviso de que requiere nueva autorización si supera 10 %.
Archivo fuente: docs/04-requisitos/wireframes/w03-cotizacion.png
Figura 4.7. Wireframe W-03: generación de cotización (HU-12, HU-16; CU-05). Fuente: docs/04-requisitos/wireframes/w03-cotizacion.png
Pendiente
Descripción: estado del vehículo con línea de tiempo, cotización desglosada con interruptores para los opcionales, total actualizado, botones «Autorizar» y «Rechazar», y pantalla de captura del código de 6 dígitos con cuenta regresiva de 5 minutos. Ancho de 360 px (RNF-01).
Archivo fuente: docs/04-requisitos/wireframes/w04-portal-cliente.png
Figura 4.8. Wireframe W-04: portal del cliente en celular (HU-02, HU-13 a HU-15, HU-28; CU-10, CU-11). Fuente: docs/04-requisitos/wireframes/w04-portal-cliente.png
Pendiente
Descripción: formulario público de solicitud con casilla de aviso de privacidad; vista de la recepcionista por día y bahía con las citas pendientes resaltadas y botón «Confirmar en bahía n».
Archivo fuente: docs/04-requisitos/wireframes/w05-agenda.png
Figura 4.9. Wireframe W-05: agenda de citas (HU-03, HU-04; CU-01, CU-09). Fuente: docs/04-requisitos/wireframes/w05-agenda.png
Pendiente
Descripción: lista de órdenes abiertas (folio, estado, bahía, responsable, días de estancia), detalle con saldo pendiente, registro de pago, botón «Entregar» deshabilitado con saldo y botón del gerente «Autorizar crédito» solo para flotillas.
Archivo fuente: docs/04-requisitos/wireframes/w06-ordenes-entrega.png
Figura 4.10. Wireframe W-06: órdenes abiertas, cobro y entrega (HU-20 a HU-23; CU-04, CU-13). Fuente: docs/04-requisitos/wireframes/w06-ordenes-entrega.png
## 4.11 Validación de requisitos con el cliente
La sesión registrada con el cliente es la entrevista del 19/10/2026. La validación formal se realiza en la Review 1 con un recorrido del SRS y de los wireframes 4.5 a 4.10, en la que se confirman el mínimo de 4 fotografías (RN-12) y la fuente de la garantía de 30 días (RN-13).
| Fecha | Técnica (recorrido, prototipo, revisión) | Hallazgos | Cambios acordados |
| --- | --- | --- | --- |
| /10/2026 | Entrevista con el cliente (levantamiento de requisitos) | Disputas por cobros no autorizados, reclamos por daños sin evidencia, llamadas para preguntar por el avance y poca visibilidad de las 4 bahías. | Base del SRS v0.1 (secciones 4.1–4.7). |
# 5. Plan de pruebas y trazabilidad
## 5.1 Plan de pruebas
Estructura adaptada de ISO/IEC/IEEE 29119-3:2021. Responsable: QA Lead.
| Apartado | Contenido |
| --- | --- |
| Alcance | Se prueba en la Fase 1: el flujo núcleo del release v0.1.0 — recepción con checklist y fotografías, asignación de bahía y mecánico, diagnóstico, cotización con vigencia, autorización con código 2FA (remota y presencial), re-cotización por sobrecosto, pago, entrega, crédito a flotillas, citas en línea, lista de órdenes abiertas, panel del gerente y control de acceso por rol. No se prueba en la Fase 1: almacén y compras (RF-08.x), operación sin conexión y sincronización (RNF-08, RNF-09; dependen de la PWA), reportes mensuales (HU-29) y envío real de correo o SMS (R-05). |
| Niveles de prueba | Unitarias y de integración: pruebas automatizadas con pytest sobre la API completa (servicio + base de datos), en backend/tests/. Sistema: recorrido del flujo núcleo en el ambiente de pruebas (desde el Sprint 4). Aceptación: los casos CPA de 5.2, ejecutados con el Product Owner y validados con el cliente en las Reviews. |
| Enfoque | Automatizado primero: cada regla de negocio (RN) y cada requisito de acceso tiene al menos una prueba automatizada; se incluyen valores límite (5 vs. 6 días, 10 % vs. 10.06 %, 5 min vs. 5 min 1 s). Manual para usabilidad y dispositivos (RNF-01 a RNF-03). Herramientas: pytest, httpx/TestClient, GitHub Actions; Lighthouse/axe para accesibilidad (Sprint 5). |
| Entornos | Local: SQLite en memoria, reloj controlable para probar vigencias. CI: GitHub Actions ejecuta las pruebas, carga db/schema.sql en PostgreSQL 16 y compila este documento. Staging: hospedaje y URL según ADR-004 (Sprint 4). Siempre datos ficticios (RNF-05). |
| Criterios de entrada | La historia cumple la DoR; existe su caso CPA en 5.2; el código está en un Pull Request hacia main. |
| Criterios de salida | 100 % de las pruebas automatizadas pasan en CI; 0 defectos S1/S2 abiertos; todos los requisitos Must tienen al menos un caso que pasa (matriz 5.3); el PO aceptó las historias. |
| Roles | QA Lead: diseña los casos, mantiene la matriz y la CI. Developers: escriben pruebas junto con el código. PO: ejecuta las pruebas de aceptación. Equipo A: QA cruzado. Cliente: valida en las Reviews. |
| Riesgos de las pruebas | Las pruebas con SQLite podrían ocultar diferencias con PostgreSQL (mitigación: la CI carga el esquema real; pendiente agregar pruebas de integración contra PostgreSQL). El envío de códigos se simula con una bandeja en memoria. Sin dispositivos reales todavía para RNF-01/02. |
| Calendario | S2: casos CPA del flujo núcleo y CI. S3: pruebas de citas y panel. S4: pruebas en staging y de rendimiento (RNF-06). S5: usabilidad, accesibilidad y SUS. S6: ejecución final, QA cruzado y reporte (sección 10). |
## 5.2 Casos de prueba de aceptación
Cada caso está automatizado en backend/tests/ con el prefijo de su ID (por ejemplo, test_cpa14_codigo_expira_a_los_cinco_minutos). Resultado de la ejecución del 29/10/2026: 35 de 35 pasan. Los datos son ficticios.
| ID | HU / CU (regla) | Precondiciones | Pasos | Resultado esperado | Res. |
| --- | --- | --- | --- | --- | --- |
| CPA-01 | HU-01, CU-02 | Sesión de Recepcionista; vehículo registrado | 1. Registrar recepción con kilometraje, combustible y checklist. | Se crea la orden con folio OS-AAAA-NNNN en estado Abierta y su primer registro en el historial. | Pasa |
| CPA-02 | HU-01, HU-09 (RN-12) | Orden con 3 fotografías | 1. Asignar bahía. 2. Registrar diagnóstico. 3. Subir la 4.ª foto y repetir. | Sin las 4 fotos se rechaza (RN-12); con ellas la orden pasa a Diagnosticada. | Pasa |
| CPA-03 | HU-01 (RN-12) | Orden con checklist incompleto | 1. Intentar diagnóstico. 2. Completar checklist. 3. Repetir. | Primero se rechaza; tras completar el checklist se acepta. | Pasa |
| CPA-04 | HU-01 | Orden abierta con foto Frente | 1. Subir otra foto Frente. 2. Subir un archivo que no es imagen. | Foto repetida rechazada (409); archivo no imagen rechazado (415). | Pasa |
| CPA-05 | HU-07 (RN-05) | Las 4 bahías ocupadas | 1. Registrar una nueva recepción. | La orden queda EnEsperaDeBahia y la respuesta trae la alerta «sin bahías». | Pasa |
| CPA-06 | HU-07 (RN-05) | 4 bahías ocupadas y 5 vehículos en espera | 1. Registrar otra recepción. | Se rechaza: estacionamiento lleno. | Pasa |
| CPA-07 | HU-08 (RN-05) | Bahía 2 ocupada | 1. Asignar la bahía 2 a otra orden. 2. Cancelar la primera orden. 3. Repetir. | Primero se rechaza; al cancelar se libera y la asignación procede. | Pasa |
| CPA-08 | HU-08 (RN-09) | Orden abierta | 1. Asignar como responsable a una recepcionista. | Se rechaza: el responsable debe ser mecánico activo. | Pasa |
| CPA-09 | CU-02 | Vehículo con orden abierta | 1. Abrir otra orden para el mismo vehículo. | Se rechaza. | Pasa |
| CPA-10 | HU-12, HU-02 | Orden Diagnosticada | 1. Generar cotización con mano de obra, refacción y un concepto opcional. | Total $1,750.00; vence a los 5 días; el cliente recibe su enlace seguro. | Pasa |
| CPA-11 | HU-14 (RN-11) | Cotización emitida el día 0 | 1. Día 5: pedir código. 2. Día 6: confirmar. | Día 5 vigente; día 6 se rechaza por vencida. | Pasa |
| CPA-12 | HU-13 (RN-03) | Cotización pendiente | 1. Deseleccionar el concepto opcional. 2. Deseleccionar uno obligatorio. | Total baja a $1,500.00; el obligatorio no se puede quitar. | Pasa |
| CPA-13 | HU-14, CU-11 (RN-02, RNF-04) | Cotización pendiente | 1. El cliente pide código desde su enlace. 2. Lo confirma. | Autorización Confirmada con IP, token y huella SHA-256 válida; orden Autorizada; el cambio no tiene usuario interno. | Pasa |
| CPA-14 | HU-14 (RN-02) | Código emitido | 1. Esperar 5 min 1 s. 2. Confirmar. | Se rechaza: código expirado. | Pasa |
| CPA-15 | HU-14 (RN-02) | Código emitido | 1. Confirmar con código incorrecto. 2. Con el correcto. 3. Repetir el correcto. | Incorrecto rechazado; correcto aceptado; segundo uso rechazado. | Pasa |
| CPA-16 | CU-03 | Cotización pendiente; cliente en mostrador | 1. Recepcionista pide el código. 2. Captura el que dicta el cliente. | Autorización Presencial confirmada. | Pasa |
| CPA-17 | HU-15 | Cotización inicial pendiente | 1. El cliente rechaza desde su enlace. | Cotización Rechazada y orden Cancelada. | Pasa |
| CPA-18 | HU-16 (RN-04) | Orden Autorizada por $1,750.00 | 1. Re-cotizar a $1,926.00 (+10.06 %). 2. Terminar trabajo. 3. Autorizar y repetir. | Queda Pendiente y bloquea el avance; tras autorizar se termina. | Pasa |
| CPA-19 | HU-16 (RN-04) | Orden Autorizada por $1,750.00 | 1. Re-cotizar a $1,925.00 (+10 % exacto). | Se autoriza sin detener el trabajo; total autorizado $1,925.00. | Pasa |
| CPA-20 | RNF-04 | Autorización confirmada | 1. Modificar el monto directamente en la base. 2. Verificar la huella. | La verificación detecta la alteración. | Pasa |
| CPA-21 | HU-21 (RN-10) | Orden lista; pago parcial | 1. Registrar la entrega. | Se rechaza por saldo pendiente. | Pasa |
| CPA-22 | HU-23, CU-04 (RN-01, RN-13) | Orden lista | 1. Pagar el total. 2. Entregar. 3. Abrir el enlace del cliente. | Orden Cerrada, garantía de 30 días, bahía libre, enlace expirado. | Pasa |
| CPA-23 | HU-23 | Orden lista | 1. Pagar un centavo más que el saldo. | Se rechaza. | Pasa |
| CPA-24 | HU-22, CU-13 (RN-10) | Orden lista de un cliente particular | 1. Recepcionista autoriza crédito. 2. Gerente lo intenta. | Recepcionista: 403. Gerente: rechazado porque no es flotilla. | Pasa |
| CPA-25 | HU-22, CU-13 (RN-10) | Orden lista de flotilla con crédito | 1. Gerente autoriza crédito. 2. Entregar con saldo. | Entrega permitida; el enlace sigue activo mientras haya saldo. | Pasa |
| CPA-26 | RF-01 | Sin sesión | 1. Consultar órdenes sin token y con token falso. | 401 en ambos casos. | Pasa |
| CPA-27 | RF-01 | Usuarios registrados | 1. Entrar con contraseña incorrecta. 2. Entrar como mecánico de bahía. | 401 en ambos casos. | Pasa |
| CPA-28 | RF-01, HU-27 | Sesiones de cada rol | 1. Recepcionista asigna bahía. 2. Jefe cancela orden. 3. Recepcionista abre el panel. 4. Almacén lista órdenes. 5. Recepcionista crea un gerente. | 403 en todos los casos. | Pasa |
| CPA-29 | HU-27 | Sesión de Gerente | 1. Dar de alta a una recepcionista. 2. Iniciar sesión con ella. | Alta correcta (correo normalizado) y sesión con rol Recepcionista. | Pasa |
| CPA-30 | RF-02.1, CU-10 (OWASP A01) | Cliente con enlace | 1. Abrir su enlace. 2. Alterar un carácter. 3. Usar un folio como enlace. | Solo su orden es visible; 2 y 3 dan 404. | Pasa |
| CPA-31 | HU-03, HU-30 (RN-08) | Público | 1. Solicitar cita sin aceptar el aviso. 2. Aceptándolo. | Sin aviso se rechaza; con aviso queda Pendiente y sin bahía. | Pasa |
| CPA-32 | HU-04, CU-01 | Dos citas pendientes a la misma hora | 1. Confirmar ambas en la bahía 3. 2. La segunda en la bahía 4. | La segunda en bahía 3 se rechaza; en bahía 4 se confirma. | Pasa |
| CPA-33 | CU-02 (RN-08) | Cita pendiente | 1. Abrir orden desde la cita. 2. Confirmarla y repetir. | Primero se rechaza; confirmada sí abre la orden. | Pasa |
| CPA-34 | HU-03 | Placas registradas a otro cliente | 1. Solicitar cita con esas placas y otro contacto. | Se rechaza. | Pasa |
| CPA-35 | RF-11, flujo núcleo | Una orden diagnosticada y una cancelada | 1. Consultar órdenes abiertas. 2. Consultar el panel. | Solo aparece la diagnosticada, con bahía y responsable; panel con 1 bahía ocupada. | Pasa |
## 5.3 Matriz de trazabilidad
Los módulos se refieren a backend/app/servicios/ (lógica) y backend/app/rutas/ (API). Resultado de la ejecución automatizada del 29/10/2026.
| Requisito | Historias | Caso de uso | Casos de prueba | Componente / módulo | Resultado |
| --- | --- | --- | --- | --- | --- |
| RF-01 (Must) | HU-27 | — | CPA-26 a CPA-29 | seguridad.py, rutas/personal.py | Pasa |
| RF-02.1 (Must) | HU-02, HU-28 | CU-10, CU-11 | CPA-10, CPA-13, CPA-30 | rutas/portal.py, servicios/cotizaciones.py | Pasa (API; falta PWA) |
| RF-02.2 (Should) | HU-02, HU-23 | CU-04 | CPA-22, CPA-25 | servicios/cobro.py | Pasa |
| RF-02.3 (Could) | HU-02 | — | — | — | Fase 2 |
| RF-03.1 (Must) | HU-05, HU-06 | CU-02 | CPA-05, CPA-34 | rutas/personal.py | Pasa |
| RF-03.2 (Should) | HU-23, HU-24 | CU-07 | CPA-22 | servicios/cobro.py (garantía) | Pasa (parcial) |
| RF-04 (Must) | HU-01, HU-25, HU-26 | CU-02 | CPA-01 a CPA-04 | servicios/ordenes.py | Pasa (sin modo offline) |
| RF-05 (Must) | HU-07, HU-08, HU-09, HU-11 | CU-05 | CPA-05 a CPA-09, CPA-35 | servicios/ordenes.py | Pasa |
| RF-06 (Must) | HU-02, HU-12 a HU-15 | CU-03, CU-05, CU-11 | CPA-10 a CPA-17 | servicios/cotizaciones.py | Pasa |
| RF-07 (Must) | HU-16 | CU-07 | CPA-18, CPA-19 | servicios/cotizaciones.py, cobro.py | Pasa |
| RF-08.1 (Should) | HU-10, HU-19 | CU-06 | Pendiente | — | No iniciado |
| RF-08.2 (Should) | HU-17, HU-18 | CU-08 | Pendiente | — | No iniciado |
| RF-08.3 (Could) | HU-18 | CU-08 | — | — | No iniciado |
| RF-09 (Should) | HU-03, HU-04, HU-06 | CU-01, CU-09 | CPA-31 a CPA-34 | servicios/citas.py | Pasa |
| RF-10 (Must) | HU-21, HU-22, HU-23 | CU-04, CU-13 | CPA-21 a CPA-25 | servicios/cobro.py | Pasa |
| RF-11 (Should) | HU-29 | CU-12 | CPA-35 | rutas/taller.py (panel) | Pasa (parcial) |
| RNF-04 | HU-14, HU-16 | CU-03, CU-11 | CPA-13, CPA-20 | servicios/cotizaciones.py (huella) | Pasa |
| RNF-05 | HU-30 | — | CPA-31; datos ficticios en todas | seguridad.py | Pasa (parcial: falta HTTPS en staging) |
Todos los requisitos Must tienen al menos una historia y un caso de prueba que pasa. Quedan sin caso los requisitos del almacén (RF-08.x, Should/Could), planificados para el Sprint 4.
# 6. Modelos de análisis
Los modelos usan los nombres del glosario (4.2) y del SRS, y coinciden con el esquema db/schema.sql y con el código de backend/app/. Notación UML 2.5.1.
## 6.1 Diagramas de flujo de datos
Pendiente
Descripción: el sistema como un único proceso «Sistema de Órdenes de Servicio y Citas» y sus entidades externas: Cliente (envía solicitud de cita, selección de conceptos, código 2FA, pago; recibe enlace seguro, cotización, código y estado), Recepcionista (datos de recepción, checklist, fotografías, pagos, entrega), Jefe de Mecánicos (asignación, diagnóstico, cotización, fin de trabajo), Gerente (alta de personal, crédito a flotillas; recibe panel) y Servicio de correo/SMS (recibe mensajes salientes).
Archivo fuente: docs/06-analisis/dfd/contexto.drawio
Figura 6.1. Diagrama de flujo de datos de contexto. Fuente: docs/06-analisis/dfd/contexto.drawio
Pendiente
Descripción: los procesos 1.0 Gestionar citas, 2.0 Recibir vehículo, 3.0 Asignar y diagnosticar, 4.0 Cotizar y autorizar, 5.0 Cobrar y entregar y 6.0 Consultar estado/panel; y los almacenes D1 Clientes y vehículos, D2 Citas, D3 Órdenes e historial, D4 Cotizaciones y autorizaciones, D5 Pagos y garantías, D6 Tokens de acceso. Los flujos con las entidades externas deben ser los mismos que en la Figura 6.1 (balanceo).
Archivo fuente: docs/06-analisis/dfd/nivel-0.drawio
Figura 6.2. Diagrama de flujo de datos de nivel 0. Fuente: docs/06-analisis/dfd/nivel-0.drawio
Pendiente
Descripción: subprocesos 4.1 Generar cotización (lee D3, escribe D4), 4.2 Enviar enlace (escribe D6, envía al servicio de correo), 4.3 Seleccionar conceptos opcionales, 4.4 Emitir código 2FA, 4.5 Validar código y registrar autorización (escribe D4 y el historial en D3), 4.6 Rechazar cotización. Entradas y salidas balanceadas con el proceso 4.0 de la Figura 6.2.
Archivo fuente: docs/06-analisis/dfd/nivel-1-cotizar.drawio
Figura 6.3. Diagrama de flujo de datos de nivel 1 del proceso 4.0 Cotizar y autorizar. Fuente: docs/06-analisis/dfd/nivel-1-cotizar.drawio
## 6.2 Modelo de datos
El modelo relacional está en 3FN: cada tabla describe una sola entidad, los atributos derivados del diagrama de clases (/total, /saldoPendiente, /fechaVencimiento, /fechaFin) no se almacenan sino que se calculan en vistas o columnas generadas, y la especialización {disjoint, complete} de Cliente usa una tabla por subclase. El esquema completo, con sus restricciones y disparadores, está en db/schema.sql y se valida en PostgreSQL 16 en cada ejecución de la integración continua.
Pendiente
Descripción: las 26 tablas de db/schema.sql con sus llaves primarias y foráneas y la cardinalidad de cada relación; resaltar el núcleo cliente — vehículo — orden_servicio — recepcion_vehicular (checklist, fotografías) — cotizacion (detalles, autorizaciones, pagos) — token_acceso.
Archivo fuente: db/schema.sql (exportar a docs/06-analisis/er/modelo-er.png)
Figura 6.4. Modelo entidad-relación. Fuente: db/schema.sql (exportar a docs/06-analisis/er/modelo-er.png)
Diccionario de datos de las tablas del flujo núcleo (las demás se documentan en los comentarios de db/schema.sql):
| Entidad | Atributo | Tipo | Nulo | Restricciones | Descripción |
| --- | --- | --- | --- | --- | --- |
| cliente | id_cliente | INTEGER | No | PK, identidad | Identificador del cliente |
|  | tipo_cliente | VARCHAR(10) | No | Particular o Flotilla | Subclase del cliente |
|  | telefono | VARCHAR(20) | No |  | Contacto (dato personal) |
|  | correo | VARCHAR(160) | No |  | Recibe enlace y códigos 2FA |
| vehiculo | id_vehiculo | INTEGER | No | PK | Identificador |
|  | id_cliente | INTEGER | No | FK cliente | Propietario |
|  | placas | VARCHAR(15) | No | Único | Placas en mayúsculas |
|  | vin | VARCHAR(17) | Sí | Único | Número de serie (opcional) |
|  | tipo | tipo_vehiculo | No | Automovil, Motocicleta, Camioneta | Solo vehículos ligeros (RN-07) |
| orden_servicio | folio | VARCHAR(20) | No | PK, formato OS-AAAA-NNNN | Folio de la orden |
|  | estado | estado_orden | No | 7 valores (6.5) | Estado actual |
|  | numero_bahia | SMALLINT | Sí | FK bahia; único entre órdenes activas | Bahía asignada (RN-05) |
|  | id_usuario_responsable | INTEGER | Sí | FK usuario | Mecánico responsable (RN-09) |
|  | entrega_a_credito | BOOLEAN | No | Requiere gerente y flotilla | Excepción de RN-10 |
|  | fecha_entrega | TIMESTAMPTZ | Sí | fecha_apertura | Momento de la entrega |
| recepcion_vehicular | kilometraje | INTEGER | No |  | Lectura del odómetro |
|  | nivel_combustible | nivel_combustible | No | 5 niveles | Combustible al ingreso |
|  | id_cita | INTEGER | Sí | FK cita, único; solo cita Confirmada | Cita de origen |
| fotografia | posicion | posicion_foto | No | Una por posición salvo «Otra» | Frente, Trasera, Izquierda, Derecha (RN-12) |
|  | archivo | VARCHAR(255) | No |  | Ruta en el almacenamiento |
| cotizacion | version | INTEGER | No | ; único con folio | Versión de la cotización |
|  | fecha_emision | DATE | No |  | Inicio de vigencia |
|  | vigencia_dias | INTEGER | No | , por omisión 5 | RN-11 |
|  | estado | estado_cotizacion | No | Pendiente, Autorizada, Rechazada, Vencida | Estado (6.5) |
| detalle_cotizacion | tipo | tipo_concepto | No | ManoDeObra, Refaccion, Insumo | Clase de concepto |
|  | precio_unitario | NUMERIC(10,2) | No |  | Precio en pesos |
|  | opcional / seleccionado | BOOLEAN | No | Solo un opcional puede deseleccionarse | RN-03 |
| autorizacion | medio | medio_autorizacion | No | Remoto exige IP y token | Canal de la autorización |
|  | tipo | tipo_autorizacion | No | Inicial o IncrementoMayor10 | RN-04 |
|  | monto_aceptado | NUMERIC(10,2) | No |  | Monto que el cliente aceptó |
|  | codigo_verificacion_hash | VARCHAR(255) | No | PBKDF2; nunca en claro | Código 2FA (RN-02) |
|  | huella_sha256 | CHAR(64) | Sí | Obligatoria si Confirmada | Detecta alteraciones (RNF-04) |
| token_acceso | token_hash | CHAR(64) | No | PK; SHA-256 del token | El token en claro solo viaja en el enlace |
|  | fecha_expiracion | TIMESTAMPTZ | Sí |  | Se fija al entregar y saldar (RN-01) |
| pago | monto | NUMERIC(10,2) | No | ; solo sobre cotización Autorizada | Abono del cliente |
## 6.3 Diagrama de clases del dominio
El diagrama de clases v4 tiene 26 clases del dominio (mínimo del Equipo B: 12), con atributos, asociaciones, multiplicidades, composiciones, una generalización {disjoint, complete} (Cliente → ClienteParticular | Flotilla), 15 enumeraciones y las restricciones de negocio como notas OCL informales. Las clases marcadas «OfflineSync» (RecepcionVehicular, ChecklistInspeccion, Diagnostico) se capturan sin conexión (RNF-08). Se divide en dos láminas por legibilidad; OrdenServicio, Usuario y TokenAcceso aparecen en ambas como vista parcial.

Figura 6.5a. Diagrama de clases del dominio (1/2): clientes, citas, recepción y orden. Fuente: docs/06-analisis/clases/diagrama-clases-v4-1.png

Figura 6.5b. Diagrama de clases del dominio (2/2): cotización, compras, pagos y garantía. Fuente: docs/06-analisis/clases/diagrama-clases-v4-2.png
## 6.4 Diagrama de objetos
Pendiente
Descripción: instantánea con datos ficticios del caso CPA-13: c1:ClienteParticular (nombre = «Cliente Ficticio»), v1:Vehiculo (placas = «PRB-001», Nissan Versa 2019), os1:OrdenServicio (folio = «OS-2026-0001», estado = Autorizada, bahía 1), r1:RecepcionVehicular (kilometraje = 45210, combustible = Mitad) con su ch1:ChecklistInspeccion (completo = true) y 4 Fotografia; d1:Diagnostico; cot1:Cotizacion (versión 1, estado = Autorizada, total = 1750.00) con 3 DetalleCotizacion; a1:Autorizacion (medio = Remoto, estado = Confirmada, monto = 1750.00) ligada a t1:TokenAcceso; m1:Usuario (rol = Mecanico) como responsable.
Archivo fuente: docs/06-analisis/objetos/orden-autorizada.puml
Figura 6.6. Diagrama de objetos: orden autorizada por el cliente. Fuente: docs/06-analisis/objetos/orden-autorizada.puml
## 6.5 Diagramas de estados
Las transiciones de la orden están programadas en una sola tabla (TRANSICIONES en backend/app/servicios/ordenes.py); cualquier transición que no aparezca aquí es rechazada por el sistema y toda transición válida queda en HistorialEstado.
Pendiente
Descripción: los 7 estados (Abierta, EnEsperaDeBahia, Diagnosticada, Autorizada, ListaParaEntrega, Cerrada, Cancelada) con las transiciones de la tabla siguiente, cada una con evento, [condición] y / rol.
Archivo fuente: docs/06-analisis/estados/orden-servicio.puml
Figura 6.7. Máquina de estados de la Orden de servicio. Fuente: docs/06-analisis/estados/orden-servicio.puml
| Estado origen | Evento | Condición | Estado destino | Rol autorizado |
| --- | --- | --- | --- | --- |
| (inicio) | Registrar recepción | El vehículo no tiene otra orden abierta; si no hay bahía, hay lugar en el estacionamiento (RN-05) | Abierta | Recepcionista |
| Abierta | Recepción sin bahía libre | Las 4 bahías están ocupadas | EnEsperaDeBahia | Recepcionista |
| EnEsperaDeBahia | Asignar bahía | Bahía libre; responsable es mecánico activo (RN-09) | Abierta | Jefe de Mecánicos |
| Abierta | Registrar diagnóstico | Checklist completo y 4 fotografías (RN-12); bahía y responsable asignados | Diagnosticada | Jefe de Mecánicos |
| Diagnosticada | Confirmar código 2FA | Cotización vigente (RN-11); código correcto, de un solo uso y con menos de 5 minutos (RN-02) | Autorizada | Cliente (remoto) o Recepcionista (presencial) |
| Diagnosticada | Rechazar cotización | Cotización vigente | Cancelada | Cliente |
| Autorizada | Terminar trabajo | No hay re-cotización pendiente mayor al 10 % (RN-04) | ListaParaEntrega | Jefe de Mecánicos |
| ListaParaEntrega | Registrar entrega | Saldo pendiente igual a 0, o entrega a crédito autorizada (RN-10) | Cerrada | Recepcionista |
| Abierta, EnEsperaDeBahia, Diagnosticada | Cancelar | — | Cancelada | Gerente |
Pendiente
Descripción: los estados Pendiente, Autorizada, Rechazada y Vencida, con las transiciones de la tabla siguiente.
Archivo fuente: docs/06-analisis/estados/cotizacion.puml
Figura 6.8. Máquina de estados de la Cotización. Fuente: docs/06-analisis/estados/cotizacion.puml
| Estado origen | Evento | Condición | Estado destino | Rol autorizado |
| --- | --- | --- | --- | --- |
| (inicio) | Generar cotización | Orden Diagnosticada (inicial) o Autorizada (re-cotización); al menos un concepto; sin otra cotización pendiente vigente | Pendiente | Recepcionista o Jefe de Mecánicos |
| (inicio) | Re-cotizar | Orden Autorizada y nuevo total total inicial autorizado 1.10 (RN-04) | Autorizada | Recepcionista o Jefe de Mecánicos |
| Pendiente | Cambiar selección | Solo conceptos opcionales (RN-03); invalida códigos ya emitidos | Pendiente | Cliente o Recepcionista |
| Pendiente | Confirmar código 2FA | Vigente y código válido (RN-02) | Autorizada | Cliente o Recepcionista |
| Pendiente | Rechazar | Vigente | Rechazada | Cliente |
| Pendiente | Pasa la fecha de vencimiento | Hoy fecha de emisión + 5 días (RN-11) | Vencida | Sistema |
## 6.6 Diagramas de actividades (to-be)
Pendiente
Descripción: carriles Cliente, Recepcionista, Sistema y Jefe de mecánicos: búsqueda o registro del cliente con aviso de privacidad, captura de kilometraje, combustible, checklist y 4 fotografías, apertura de la orden, decisión «¿hay bahía libre?» (EnEsperaDeBahia con alerta), asignación de bahía y responsable, registro del diagnóstico y validación de RN-12.
Archivo fuente: docs/06-analisis/actividades/recepcion-diagnostico.puml
Figura 6.9. Actividad to-be: recepción y diagnóstico. Fuente: docs/06-analisis/actividades/recepcion-diagnostico.puml
Pendiente
Descripción: carriles Jefe de mecánicos, Sistema y Cliente: generación de la cotización con vigencia de 5 días, envío del enlace seguro, selección de opcionales, decisión aceptar/rechazar, emisión y validación del código de 6 dígitos, registro de la autorización con huella SHA-256, ejecución del trabajo y re-cotización bloqueante si el adicional supera el 10 %.
Archivo fuente: docs/06-analisis/actividades/cotizacion-autorizacion.puml
Figura 6.10. Actividad to-be: cotización y autorización con código 2FA. Fuente: docs/06-analisis/actividades/cotizacion-autorizacion.puml
# 7. Arquitectura y diseño
## 7.1 Estilo arquitectónico
El sistema sigue un estilo cliente-servidor con API REST. El servidor es un monolito modular en capas (ADR-001):
Rutas (app/rutas/): traducen HTTP a llamadas de servicio, validan la entrada con Pydantic y declaran qué rol puede usar cada operación.
Servicios (app/servicios/): toda la lógica y las reglas de negocio RN-xx. Es la única capa que cambia el estado de una orden o de una cotización.
Modelo (app/models.py): entidades del dominio, iguales a las clases de 6.3 y a las tablas de db/schema.sql.
Datos: PostgreSQL (ADR-003), que además refuerza las restricciones con CHECK, índices únicos parciales y disparadores.
Los clientes son dos interfaces web que consumen la misma API: la del personal del taller (tableta o laptop) y el portal del cliente, al que se entra con el enlace seguro (ADR-005). Las interfaces web (PWA) se construyen en los Sprints 4 y 5; hoy la API se opera desde su documentación interactiva en /docs.
| RNF | Decisión de arquitectura que lo atiende |
| --- | --- |
| RNF-04 | Una sola capa de servicios registra las autorizaciones: guarda fecha y hora UTC, IP, medio, monto y una huella SHA-256 de lo aceptado, que se recalcula para detectar alteraciones (CPA-20). El historial de estados y los diagnósticos son registros inmutables (disparador fn_registro_inmutable). |
| RNF-05 | Contraseñas con PBKDF2-SHA256; tokens del cliente y códigos 2FA guardados solo como hash; control de acceso por rol declarado en cada ruta; el portal identifica la orden por el token y no por el folio (OWASP A01, CPA-30); HTTPS lo provee el hospedaje (ADR-004). |
| RNF-07 | Toda la pila es de código abierto: Python, FastAPI, SQLAlchemy, PostgreSQL, pytest (ADR-002 y ADR-003). |
| RNF-08 y RNF-09 | Las entidades «OfflineSync» llevan uuid_local único, generado en el dispositivo: reenviar un registro ya sincronizado no lo duplica (sincronización idempotente). La captura sin conexión vivirá en la PWA con IndexedDB. Endpoint de sincronización por lotes: Pendiente. |
| RNF-10 | Las operaciones del portal son seguras de reintentar: pedir un código nuevo expira el anterior y un código solo se acepta una vez (CPA-15), así que un reintento automático no duplica autorizaciones. |
| RNF-01 | El portal del cliente es web y responsivo; no requiere instalar nada ni conceder permisos. |
## 7.2 Diagramas C4
Pendiente
Descripción: el sistema y sus usuarios: Cliente (portal web con enlace seguro), Recepcionista, Jefe de Mecánicos, Gerente y Encargado de Almacén; sistemas externos: servicio de correo electrónico (enlaces y códigos 2FA) y, en Fase 2, servicio de SMS.
Archivo fuente: docs/07-arquitectura/c4/contexto.puml
Figura 7.1. C4 nivel 1: contexto del sistema. Fuente: docs/07-arquitectura/c4/contexto.puml
Pendiente
Descripción: PWA del personal (navegador en tableta/laptop, con IndexedDB para operar sin conexión), portal del cliente (navegador móvil), API REST FastAPI (Python 3.12), base de datos PostgreSQL 16, almacenamiento de fotografías y servicio de correo; protocolos HTTPS/JSON entre navegador y API y SQL (psycopg) entre API y base de datos.
Archivo fuente: docs/07-arquitectura/c4/contenedores.puml
Figura 7.2. C4 nivel 2: contenedores. Fuente: docs/07-arquitectura/c4/contenedores.puml
Pendiente
Descripción: componentes Rutas del personal (rutas/personal.py), Rutas del taller (rutas/taller.py), Portal (rutas/portal.py), Seguridad (seguridad.py), Servicios de órdenes, citas, cotizaciones y cobro (servicios/), Notificaciones (notificaciones.py) y Modelo/ORM (models.py, db.py), con sus dependencias.
Archivo fuente: docs/07-arquitectura/c4/componentes-api.puml
Figura 7.3. C4 nivel 3: componentes de la API. Fuente: docs/07-arquitectura/c4/componentes-api.puml
## 7.3 Registros de decisiones de arquitectura (ADR)
| Campo | Contenido |
| --- | --- |
| ID y título | ADR-001 Estilo arquitectónico: monolito modular en capas con API REST |
| Fecha y estado | 29/10/2026 · Aceptado (reemplaza la propuesta de microservicios de la Propuesta de Solución Tecnológica) |
| Contexto | Equipo de 5 personas con poca experiencia en FastAPI (R-07), 6 sprints, hospedaje gratuito y reglas de negocio que cruzan varias entidades en una misma transacción (autorizar cambia cotización, orden e historial). |
| Alternativas evaluadas | 1. Microservicios (citas, órdenes, cotizaciones, cobro). 2. Monolito MVC con páginas generadas en el servidor. 3. Monolito modular en capas que expone una API REST. |
| Decisión | Opción 3. Los módulos de servicio están separados por área y solo dependen hacia abajo (7.5), de modo que podrían separarse después si hiciera falta. |
| Consecuencias | + Una sola transacción por operación; un solo despliegue; pruebas de extremo a extremo sencillas. + La API sirve igual a la PWA del personal y al portal del cliente. – Escala como una sola unidad (suficiente para un taller de 4 bahías). – Hay que vigilar que las rutas no contengan lógica de negocio. |
| RNF relacionados | RNF-04, RNF-07, RNF-10 |
| ID y título | ADR-002 Pila tecnológica: Python 3.12 + FastAPI + SQLAlchemy 2 |
| Fecha y estado | 29/10/2026 · Aceptado (la interfaz web queda por decidir en el Sprint 3) |
| Contexto | La propuesta al cliente comprometió Python con FastAPI y herramientas gratuitas. Se necesita validación de datos, documentación automática de la API y un ORM que funcione con PostgreSQL y SQLite. |
| Alternativas evaluadas | 1. Django + Django REST Framework. 2. Node.js + Express. 3. FastAPI + SQLAlchemy + Pydantic. |
| Decisión | Opción 3: validación declarativa, documentación OpenAPI en /docs sin trabajo extra y pruebas con TestClient. |
| Consecuencias | + Curva de aprendizaje corta para un equipo que ya usa Python. – FastAPI no trae panel de administración ni autenticación integrada: se implementó la propia con la biblioteca estándar (seguridad.py). |
| RNF relacionados | RNF-07, RNF-05 |
| ID y título | ADR-003 Base de datos: PostgreSQL 16 |
| Fecha y estado | 29/10/2026 · Aceptado |
| Contexto | El modelo tiene restricciones fuertes: especialización disjunta, una bahía con una sola orden activa, una cita confirmada por bahía y horario, historial inmutable, atributos derivados. |
| Alternativas evaluadas | 1. MySQL 8. 2. SQLite. 3. PostgreSQL 16. |
| Decisión | PostgreSQL en el ambiente de pruebas y producción: tipos ENUM, índices únicos parciales, columnas generadas y disparadores PL/pgSQL. SQLite solo para desarrollo local y pruebas automatizadas; por eso las reglas también se validan en la capa de servicios. |
| Consecuencias | + La base de datos protege las reglas aunque alguien la modifique directamente. – Dos motores (SQLite y PostgreSQL): la CI carga el esquema real en PostgreSQL para detectar diferencias. |
| RNF relacionados | RNF-04, RNF-07, RNF-09 |
| ID y título | ADR-004 Hospedaje del ambiente de pruebas |
| Fecha y estado | 29/10/2026 · Propuesto (decidir antes del Sprint 4) |
| Contexto | Se necesita un ambiente de pruebas con HTTPS, PostgreSQL y almacenamiento de fotografías, sin costo (RNF-07). |
| Alternativas evaluadas | 1. Render (servicio web gratuito) + PostgreSQL gestionado gratuito (Neon o Supabase). 2. Fly.io. 3. Servidor dentro del taller. |
| Decisión | Pendiente. Recomendación inicial: opción 1 por su HTTPS automático y despliegue desde GitHub. |
| Consecuencias | Opción 1: + sin servidor que mantener; – el plan gratuito suspende el servicio tras inactividad y limita el almacenamiento (R-06). |
| RNF relacionados | RNF-05, RNF-07 |
| ID y título | ADR-005 Almacenamiento de fotografías y acceso del cliente con enlace seguro |
| Fecha y estado | 29/10/2026 · Aceptado (acceso del cliente); fotografías: aceptado para v0.1.0 |
| Contexto | El cliente debe consultar y autorizar sin cuenta ni contraseña, pero nadie debe poder ver la orden de otro (OWASP A01). Cada recepción genera al menos 4 fotografías que no deben saturar el hospedaje gratuito. |
| Alternativas evaluadas | Acceso: 1. Cuenta de cliente con contraseña. 2. Folio + teléfono. 3. Token aleatorio en el enlace + código 2FA para autorizar. Fotos: 1. Guardarlas en la base de datos (BLOB). 2. Sistema de archivos del servidor. 3. Servicio de almacenamiento de objetos. |
| Decisión | Acceso: opción 3 — token de 256 bits generado con secrets, guardado solo como hash SHA-256, un enlace activo por orden, que expira al entregar y saldar (RN-01); autorizar exige además el código de 6 dígitos enviado al correo (RN-02). Fotos: opción 2 en v0.1.0 (carpeta MEDIA_DIR, solo JPEG/PNG/WebP de hasta 5 MB, nombre aleatorio); la base guarda solo la ruta, así que migrar a la opción 3 no cambia el modelo. |
| Consecuencias | + El folio no sirve para entrar (CPA-30); quien intercepte el enlace aún necesita el correo para autorizar. – Si el cliente pierde el enlace, el taller debe reenviarlo. – Los archivos locales se pierden si el hospedaje gratuito reinicia el disco: se confirma con ADR-004 y, de ser necesario, se pasa a almacenamiento de objetos. |
| RNF relacionados | RNF-04, RNF-05, RNF-01 |
| ID y título | ADR-006 Reglas de negocio como tablas de decisión DMN con Camunda |
| Fecha y estado | 02/11/2026 · Propuesto (diseño teórico; no implementado) |
| Contexto | Las reglas RN-xx viven hoy como código Python en app/servicios/. Varias son decisiones con umbrales que el cliente puede querer cambiar (10 % de re-cotización, 5 días de vigencia, tipos de vehículo admitidos, crédito a flotillas, conversión del nivel de combustible de RN-14). Cada cambio de umbral exige hoy modificar código, probar y desplegar. |
| Alternativas evaluadas | 1. Mantener las reglas en Python (situación actual). 2. Tablas de decisión DMN 1.3 modeladas en Camunda Modeler y evaluadas por el motor de decisiones de Camunda (DMN Engine) a través de su API REST. 3. Tablas de decisión DMN evaluadas dentro del mismo proceso Python con una biblioteca DMN. |
| Decisión | Opción 2 como diseño objetivo (detallado en 7.9): las decisiones se modelan en DMN con Camunda Modeler, se versionan en docs/07-arquitectura/dmn/ y la capa de servicios las consulta mediante un adaptador servicios/decisiones.py. Los procesos (BPMN) siguen en el código; Camunda solo se usa para decisiones. |
| Consecuencias | + Las reglas quedan como tablas legibles que el Gerente puede revisar y validar sin leer código. + Cada evaluación devuelve la regla que se cumplió, lo que sirve como evidencia de auditoría (RNF-04). – Agrega un servicio más que desplegar y mantener. – El motor no está disponible sin conexión: el adaptador debe tener un respaldo local (7.9). – Hay que confirmar la licencia de la edición de Camunda que se use contra RNF-07. |
| RNF relacionados | RNF-04, RNF-07, RNF-08 |
## 7.4 Diagramas de artefactos y de despliegue
Pendiente
Descripción: el artefacto backend/ (paquete Python con app/ y requirements.txt), db/schema.sql y, cuando exista, el paquete estático de la PWA; con sus dependencias de manifestación hacia los componentes de 7.3.
Archivo fuente: docs/07-arquitectura/despliegue/artefactos.puml
Figura 7.4. Diagrama de artefactos. Fuente: docs/07-arquitectura/despliegue/artefactos.puml
Pendiente
Descripción: nodo «dispositivo» tableta/laptop del taller y celular del cliente (navegador), nodo «servidor» del hospedaje con el proceso uvicorn y la API, nodo «base de datos» PostgreSQL 16 y almacenamiento de fotografías; conexiones HTTPS y TCP/5432, según el hospedaje que se elija en ADR-004.
Archivo fuente: docs/07-arquitectura/despliegue/despliegue.puml
Figura 7.5. Diagrama de despliegue del ambiente de pruebas. Fuente: docs/07-arquitectura/despliegue/despliegue.puml
## 7.5 Diagrama de paquetes
Dependencias entre paquetes de backend/app (todas en un solo sentido, sin ciclos): rutas  servicios  models  db; rutas  seguridad, schemas; dentro de servicios: cobro  cotizaciones  ordenes, y citas es independiente.
Pendiente
Descripción: los paquetes app.rutas, app.servicios (ordenes, citas, cotizaciones, cobro), app.models, app.schemas, app.seguridad, app.notificaciones y app.db, con las dependencias «import» descritas arriba.
Archivo fuente: docs/07-arquitectura/paquetes.puml
Figura 7.6. Diagrama de paquetes del backend. Fuente: docs/07-arquitectura/paquetes.puml
## 7.6 Diagramas de clases de la solución
Pendiente
Descripción: las clases tal como existen en el código: routers personal, taller y portal; módulos de servicio ordenes (abrir_orden, asignar, registrar_diagnostico, cambiar_estado), cotizaciones (crear_cotizacion, solicitar_codigo, confirmar_codigo, huella), cobro (registrar_pago, entregar); entidades OrdenServicio, RecepcionVehicular, Cotizacion, Autorizacion, TokenAcceso; y los esquemas Pydantic de entrada y salida.
Archivo fuente: docs/07-arquitectura/clases-solucion.puml
Figura 7.7. Clases de la solución del flujo núcleo. Fuente: docs/07-arquitectura/clases-solucion.puml
## 7.7 Diagramas de secuencia
Pendiente
Descripción: Recepcionista → POST /ordenes → ordenes.abrir_orden (valida vehículo, cita y capacidad) → crea OrdenServicio, HistorialEstado y RecepcionVehicular → respuesta con folio y alerta de bahías; luego POST /ordenes/{folio}/fotografias por cada posición.
Archivo fuente: docs/07-arquitectura/secuencias/recepcion.puml
Figura 7.8. Secuencia: recepción del vehículo (escenario principal del flujo núcleo). Fuente: docs/07-arquitectura/secuencias/recepcion.puml
Pendiente
Descripción: Cliente → POST /portal/{token}/codigo → token_valido → solicitar_codigo → notificaciones (correo); Cliente → POST /portal/{token}/autorizacion → confirmar_codigo (vigencia, código, huella) → cambiar_estado(Autorizada).
Archivo fuente: docs/07-arquitectura/secuencias/autorizacion-remota.puml
Figura 7.9. Secuencia: autorización remota con código 2FA. Fuente: docs/07-arquitectura/secuencias/autorizacion-remota.puml
Pendiente
Descripción: Jefe de mecánicos crea cotización versión 2 → el servicio compara con el total inicial → queda Pendiente y se envía enlace → terminar es rechazado (RN-04) hasta que el cliente autoriza.
Archivo fuente: docs/07-arquitectura/secuencias/recotizacion.puml
Figura 7.10. Secuencia: re-cotización mayor al 10 %. Fuente: docs/07-arquitectura/secuencias/recotizacion.puml
Pendiente
Descripción: Recepcionista → POST pagos → registrar_pago (no excede saldo) → POST entrega → entregar (saldo o crédito) → Cerrada, Garantía, bahía libre y token expirado.
Archivo fuente: docs/07-arquitectura/secuencias/entrega.puml
Figura 7.11. Secuencia: pago y entrega. Fuente: docs/07-arquitectura/secuencias/entrega.puml
## 7.8 Diagrama de comunicación
Pendiente
Descripción: objetos :RutaTaller, :ServicioOrdenes, os:OrdenServicio, b:Bahia, m:Usuario y :HistorialEstado, con los mensajes numerados 1 asignar, 1.1 obtener bahía, 1.2 validar responsable, 1.3 ocupar bahía, 1.4 cambiarEstado(Abierta) si estaba en espera.
Archivo fuente: docs/07-arquitectura/comunicacion-asignacion.puml
Figura 7.12. Comunicación: asignación de bahía. Fuente: docs/07-arquitectura/comunicacion-asignacion.puml
## 7.9 Modelado de decisiones con DMN y Camunda
Esta sección describe el diseño propuesto en ADR-006. Camunda todavía no forma parte del código ni del despliegue; las reglas siguen implementadas en Python en app/servicios/.
Qué es DMN y para qué se usa aquí.
DMN (Decision Model and Notation, estándar del OMG, versión 1.3) describe decisiones de negocio como tablas de decisión: columnas de entrada, columnas de salida y una fila por regla, con una política de acierto (hit policy) que dice qué hacer si se cumplen varias filas. Las expresiones de cada celda se escriben en FEEL (Friendly Enough Expression Language), por ejemplo > 10, [13..37] o "Flotilla". Camunda aporta dos piezas: Camunda Modeler (aplicación de escritorio gratuita para dibujar las tablas y guardarlas como archivos .dmn) y el motor de decisiones que recibe los datos de entrada y devuelve el resultado.
En este proyecto Camunda se usa solo para decisiones (DMN), no para orquestar procesos (BPMN): el flujo de la orden (estados de 6.5) sigue controlado por servicios/ordenes.py, y únicamente le pregunta al motor «¿qué dice la regla?» en los puntos donde hoy hay un if con umbrales de negocio.
Tablas de decisión propuestas.
| Decisión (clave) | Regla | Entradas | Salidas | Hit policy |
| --- | --- | --- | --- | --- |
| requiere_recotizacion | RN-04 | total inicial, total nuevo | requiere autorización (sí/no), motivo | UNIQUE |
| vigencia_cotizacion | RN-11 | días desde la emisión | vigente (sí/no) | UNIQUE |
| vehiculo_admitido | RN-07 | tipo de vehículo, peso (t) | admitido (sí/no), motivo | FIRST |
| permite_entrega | RN-10 | saldo pendiente, tipo de cliente, crédito autorizado por el Gerente | entregar (sí/no), motivo | FIRST |
| nivel_combustible | RN-14 | método de medición, porcentaje OBD-II | nivel (Reserva, 1/4, 1/2, 3/4, Lleno o No verificable) | UNIQUE |
| nivel_contingencia | RN-15 | hay luz, hay internet, horas de corte, batería (%) | nivel de operación (1, 2 o 3) | FIRST |
Como ejemplo, la tabla permite_entrega (RN-10) queda así; se lee de arriba hacia abajo y gana la primera fila que se cumpla (FIRST):
| # | saldo | tipoCliente | creditoAutorizado | entregar | motivo |
| --- | --- | --- | --- | --- | --- |
|  | <= 0 | - | - | true | "Saldo cubierto" |
| 2 | > 0 | "Flotilla" | true | true | "Crédito a flotilla" |
| 3 | > 0 | - | - | false | "Saldo pendiente (RN-10)" |
Cómo se integra con el backend.
Modelado y versionado. Cada tabla se dibuja en Camunda Modeler y se guarda en docs/07-arquitectura/dmn/<clave>.dmn, en git, con revisión por Pull Request como el resto del código. El Gerente valida la tabla impresa antes de publicarla.
Despliegue. Los archivos .dmn se despliegan al motor de Camunda, que corre como un contenedor aparte junto a la API (un nodo más en el diagrama de despliegue de 7.4).
Evaluación. Un nuevo módulo app/servicios/decisiones.py expone una función evaluar(clave, datos) que llama a la API REST del motor con las variables de entrada y devuelve las salidas. Los demás servicios solo dependen de esa función; por ejemplo, cobro.entregar llama a evaluar("permite_entrega", {...}) en lugar de comparar el saldo por su cuenta. Así se respeta la regla de 7.1: la lógica de negocio sigue fuera de las rutas.
Respaldo sin conexión. Si el motor no responde (corte de internet, RNF-08, o contingencia de RN-15), el adaptador evalúa una copia local de las mismas tablas con una biblioteca DMN de Python, o, en su defecto, la implementación actual en Python. La PWA sin conexión no consulta al motor: las decisiones que dependen de él se vuelven a evaluar al sincronizar (RNF-09).
Auditoría. Cada evaluación guarda en el historial de la orden la clave de la decisión, su versión y la fila que se cumplió, como evidencia de por qué se permitió o bloqueó una operación (RNF-04).
Pruebas. Cada fila de cada tabla tiene su caso en backend/tests/ (test_dmn_<clave>.py); los casos CPA existentes de RN-04, RN-07, RN-10 y RN-11 deben seguir pasando sin cambios, lo que prueba que la migración no alteró el comportamiento.
Plan de adopción.
Se migraría una decisión a la vez, empezando por requiere_recotizacion (RN-04), que es la más simple y la que el cliente tiene más probabilidad de ajustar. Antes de iniciar hay que confirmar con el equipo y el docente: (1) la edición y versión de Camunda y que su licencia cumpla RNF-07 para el uso que se le dará; (2) dónde se hospeda el motor (ADR-004); y (3) si el beneficio justifica un servicio adicional en un taller de 4 bahías o si conviene la opción 3 de ADR-006 (DMN evaluado dentro de la misma API).
Pendiente
Descripción: las seis decisiones de la tabla de 7.9 como rectángulos de decisión, sus datos de entrada (orden, cotización, cliente, vehículo, recepción, estado de la infraestructura) como óvalos y la fuente de conocimiento «Reglas de negocio 4.7» enlazada a cada decisión; exportado de Camunda Modeler.
Archivo fuente: docs/07-arquitectura/dmn/drd.dmn
Figura 7.13. Diagrama de requisitos de decisión (DRD). Fuente: docs/07-arquitectura/dmn/drd.dmn
# 8. Diseño de la interfaz de usuario
Esta sección corresponde al corte de la Review 5 (Sprints 4 y 5). La API del flujo núcleo ya existe (sección 9); el prototipo de alta fidelidad, la evaluación heurística y la prueba con usuarios se hacen sobre los wireframes de 4.10 una vez validados con el cliente.
## 8.1 Prototipo de alta fidelidad
Pendiente
## 8.2 Accesibilidad
Pendiente
## 8.3 Evaluación heurística recibida
Pendiente
## 8.4 Prueba con usuarios y SUS
Pendiente
# 9. Implementación del Release v0.1.0
## 9.1 Pila tecnológica
| Capa | Tecnología y versión | ADR que la justifica |
| --- | --- | --- |
| Interfaz | PWA (Pendiente). Hoy: documentación interactiva OpenAPI de FastAPI (/docs) | ADR-001, ADR-002 |
| Lógica de negocio / API | Python 3.12, FastAPI 0.115+, Pydantic 2, SQLAlchemy 2.0, Uvicorn | ADR-002 |
| Base de datos | PostgreSQL 16 (esquema db/schema.sql); SQLite para desarrollo y pruebas | ADR-003 |
| Hospedaje del ambiente de pruebas | Pendiente | ADR-004 |
| Integración continua | GitHub Actions (.github/workflows/ci.yml) | — |
## 9.2 Instrucciones de instalación y ejecución
Los mismos pasos están en el README.md del repositorio. Requisitos: Python 3.12 o superior y Git.
Clonar el repositorio y entrar a backend/.
Crear un entorno virtual e instalar dependencias:
python -m venv .venv y pip install -r requirements.txt.
Copiar .env.example como .env. Sin cambios usa SQLite local; para PostgreSQL, crear la base con psql -d taller -f db/schema.sql y poner su DATABASE_URL. El .env nunca se sube al repositorio.
Cargar los datos ficticios: python -m app.semilla --demo. Crea las 4 bahías, un usuario por rol (correos @taller.test), un cliente particular y una flotilla con crédito. La contraseña se toma de SEED_PASSWORD o se genera e imprime una sola vez.
Ejecutar: uvicorn app.main:app --reload y abrir http://localhost:8000/docs.
Pruebas: python -m pytest.
## 9.3 Integración continua y flujo de trabajo
El pipeline de GitHub Actions se ejecuta en cada push a main o a una rama rol/* y en cada Pull Request, con tres trabajos:
Pruebas del backend: instala dependencias y ejecuta las 35 pruebas de pytest.
Esquema en PostgreSQL: levanta PostgreSQL 16 y carga db/schema.sql con ON_ERROR_STOP, para detectar errores del esquema real.
Documento de Ingeniería: compila este documento LaTeX y publica el PDF como artefacto.
Flujo de trabajo: cada rol trabaja en su rama (rol/product-owner, rol/scrum-master, rol/qa-lead, rol/developers); los commits llevan el formato «Rol: mensaje» y se integran a main con un merge sin fast-forward, para que quede visible qué integró cada rol. Por acuerdo del equipo, la rama main se integra mediante Pull Request con al menos una revisión y la CI aprobada (CONTRIBUTING.md).
Pendiente
Descripción: captura de la pestaña Actions de GitHub con los tres trabajos (Pruebas del backend, Esquema en PostgreSQL, Documento de Ingeniería) en verde para el último commit de main.
Archivo fuente: .github/workflows/ci.yml
Figura 9.1. Ejecución exitosa del pipeline de integración continua. Fuente: .github/workflows/ci.yml
## 9.4 Evidencia del flujo núcleo
Pendiente. Mientras tanto, el flujo completo está cubierto por las pruebas automatizadas CPA-01, CPA-13, CPA-22 y CPA-35.
Pendiente
Descripción: pantalla de recepción en el ambiente de pruebas con datos ficticios: kilometraje, combustible, checklist completo, las 4 fotografías y el folio generado.
Archivo fuente: docs/09-implementacion/evidencia/01-recepcion.png
Figura 9.2. Apertura de orden con checklist y fotografías. Fuente: docs/09-implementacion/evidencia/01-recepcion.png
Pendiente
Descripción: pantalla de la tableta del jefe de mecánicos con la bahía y el responsable asignados, el diagnóstico guardado y la orden en estado Diagnosticada.
Archivo fuente: docs/09-implementacion/evidencia/02-diagnostico.png
Figura 9.3. Diagnóstico registrado. Fuente: docs/09-implementacion/evidencia/02-diagnostico.png
Pendiente
Descripción: portal del cliente en un celular: la cotización desglosada, la selección de opcionales, la captura del código de 6 dígitos y la confirmación con fecha y hora.
Archivo fuente: docs/09-implementacion/evidencia/03-autorizacion.png
Figura 9.4. Cotización con autorización registrada. Fuente: docs/09-implementacion/evidencia/03-autorizacion.png
Pendiente
Descripción: pantalla con las órdenes abiertas, su estado, bahía, responsable y días de estancia.
Archivo fuente: docs/09-implementacion/evidencia/04-ordenes-abiertas.png
Figura 9.5. Lista de órdenes abiertas. Fuente: docs/09-implementacion/evidencia/04-ordenes-abiertas.png
# 10. Reporte final de pruebas e incidencias
## 10.1 Resultado de los casos de prueba
Corte parcial (29/10/2026). El reporte final se completa en el Sprint 6 con la ejecución de aceptación con el cliente y el QA cruzado.
| Indicador | Valor |
| --- | --- |
| Casos de prueba diseñados | (CPA-01 a CPA-35, sección 5.2) |
| Casos ejecutados | , automatizados |
| Pasan | 35 |
| Fallan | . CPA-11 falló en su primera ejecución (el portal respondía 404 ante una cotización vencida, en lugar del aviso de RN-11); se corrigió antes de integrar a main. |
| Bloqueados | 0 |
| Pruebas unitarias automatizadas (número y resultado en CI) | pruebas de pytest; se ejecutan en GitHub Actions en cada push y Pull Request |
## 10.2 Incidencias
Incluye las incidencias internas, del QA cruzado y del cliente. El tiempo de atención se mide desde que se registró hasta que se cerró.
| Severidad | Registradas | Cerradas | Rechazadas (con justificación) | Abiertas | Tiempo promedio de atención |
| --- | --- | --- | --- | --- | --- |
| S1 |  |  |  |  |  |
| S2 |  |  |  |  |  |
| S3 |  |  |  |  |  |
| S4 |  |  |  |  |  |
## 10.3 Defectos conocidos que pasan a la Fase 2
| Issue | Descripción | Severidad | Prioridad | Motivo por el que no se corrigió |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
## 10.4 QA cruzado realizado al otro equipo
Pendiente
# 11. Paquete de transferencia a la Fase 2
Lo necesario para que un equipo, incluso uno distinto, continúe el proyecto en Ingeniería de Software II.
| Apartado | Contenido |
| --- | --- |
| Backlog restante priorizado | Historias con release Fase 2 de la sección 4.5: HU-05, HU-11, HU-19, HU-24 y HU-29. |
| Deuda técnica conocida | Pendiente |
| Riesgos abiertos | Registro de riesgos de la sección 2.4. |
| Decisiones pendientes con el cliente | Hospedaje del ambiente de pruebas (ADR-004) y validación de RN-12 y RN-13 (sección 4.11). |
| Accesos y configuración | Repositorio en GitHub y GitHub Actions; las credenciales no se incluyen en el documento ni en el repositorio. |
| Recomendaciones | Pendiente |
# 12. Retrospectiva del proyecto y contribución individual
## 12.1 Retrospectiva del proyecto
| ¿Qué funcionó bien? | ¿Qué no funcionó? | ¿Qué haríamos distinto en la Fase 2? |
| --- | --- | --- |
| Pendiente | Pendiente | Pendiente |
## 12.2 Contribución individual
| Integrante | Principales aportes | Evidencia (issues, PR, documentos) | Revisiones de código o documentos hechas a otros |
| --- | --- | --- | --- |
| Ángel Yael Avendaño Guzmán (Product Owner) | Enlace con el cliente, levantamiento de requerimientos en entrevistas, priorización del Product Backlog y aceptación de entregables. | Rama rol/product-owner | — |
| Abdías Daniel Chávez Cruz (Scrum Master / Tech Lead) | Facilitación de Scrum, arquitectura del backend en FastAPI, diseño de la base de datos relacional y gestión técnica de Pull Requests. | Rama rol/scrum-master; backend/; db/schema.sql | — |
| Dulce María Estudillo Rosado (QA Lead / Developer) | Plan de pruebas, casos de aceptación, validación de calidad y QA cruzado al otro equipo. | Rama rol/qa-lead; sección 5 | — |
| Isis Alhelí González Maldonado (Developer) | Especificación de requisitos (SRS), historias de usuario y modelado de procesos del negocio. | Rama rol/developers; sección 4 | — |
| Isis Yamilet Meléndez Hernández (Developer) | Integración y compilación del Documento de Ingeniería, flujos de CI en GitHub Actions y apoyo en desarrollo. | Rama rol/developers; docs/documento/; .github/workflows/ | — |
# 13. Referencias
Schwaber, K., & Sutherland, J. (2020). La Guía de Scrum. https://scrumguides.org/
ISO/IEC/IEEE. (2018). ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering. ISO.
ISO/IEC. (2023). ISO/IEC 25010:2023 Systems and software engineering — SQuaRE — Product quality model. ISO.
ISO/IEC/IEEE. (2021). ISO/IEC/IEEE 29119-3:2021 Software and systems engineering — Software testing — Part 3: Test documentation. ISO.
Object Management Group. (2017). OMG Unified Modeling Language, Version 2.5.1. https://www.omg.org/spec/UML/2.5.1
Object Management Group. (2021). Decision Model and Notation (DMN), Version 1.3. https://www.omg.org/spec/DMN/1.3
Camunda. (s.f.). DMN reference [Documentación]. https://docs.camunda.io/docs/components/modeler/dmn/
# Anexos
Los anexos se numeran con letras:
Anexo A. Guiones y minutas de las entrevistas con el cliente (mínimo 20 preguntas en el guion inicial).
Anexo B. Minutas de las Sprint Reviews con aceptaciones y rechazos del cliente.
Anexo C. Detalle completo de las historias de usuario y los casos de prueba, si no caben en el cuerpo.
Anexo D. Manual breve de uso del flujo del núcleo (Equipo A: para la auxiliar de oficina; Equipo B: para la recepcionista).
Anexo E. Aviso de privacidad (borrador).