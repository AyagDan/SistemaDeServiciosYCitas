Universidad del Istmo · Campus Ixtepec

Ingeniería en Desarrollo de Software y Sistemas Inteligentes

Ingeniería de Software I (IDSSI-27) · Quinto semestre

**Machote: Documento de Ingeniería del Proyecto – Fase 1**

Plantilla del documento que cada equipo entrega para ser evaluado

**Equipo:** [A (6 integrantes) / B (5 integrantes)]

**Cliente:** [Cooperativa Totoperas del Istmo / Servicio Automotriz Hermanos Ruiz]

**Producto:** [Nombre del sistema]

**Versión del documento:** [v0.1 … v2.0] · **Fecha:** [dd/mm/aaaa]

**Contenido**

0. Cómo usar este machote

Portada

1. Información general del proyecto

2. Gestión del proyecto con Scrum

3. Visión y viabilidad del producto

4. Especificación de requisitos de software (SRS)

5. Plan de pruebas y trazabilidad

6. Modelos de análisis

7. Arquitectura y diseño

8. Diseño de la interfaz de usuario

9. Implementación del Release v0.1.0

10. Reporte final de pruebas e incidencias

11. Paquete de transferencia a la Fase 2

12. Retrospectiva del proyecto y contribución individual

13. Referencias

Anexos

Lista de verificación antes de entregar

# 0. Cómo usar este machote

Este documento es la plantilla del **Documento** **de** **Ingeniería** **del** **Proyecto** **–** **Fase** **1** que cada equipo entrega al profesor para su evaluación. Reúne en un solo archivo lo que el equipo produce durante los sprints 0 a 6 y que se encuentra en la carpeta docs/ del repositorio.

## 0.1 Reglas de uso

* Conserven la numeración y el orden de las secciones. Si una sección no aplica, déjenla con la leyenda "No aplica" y una justificación de una línea.
* Los recuadros grises marcados como **"Instrucción"** explican qué debe contener cada sección. **Bórrenlos antes de entregar.**
* El texto gris entre corchetes, como [Escriba aquí…], es un marcador: reemplácenlo por contenido propio.
* Las filas de ejemplo en las tablas solo muestran el formato; sustitúyanlas por los datos de su proyecto.
* Los diagramas se insertan como imágenes legibles y su archivo fuente (draw.io, PlantUML o Mermaid) queda en el repositorio. Cada diagrama lleva número, título y ruta de su fuente: *Figura 4.2. Máquina de estados de Pedido. Fuente: docs/04-analisis/estados/pedido.puml*.
* Cuando el contenido sea muy extenso (por ejemplo, las 35 historias de usuario o los 25 casos de prueba), el documento incluye la tabla resumen y el detalle completo puede quedar en un anexo o en el repositorio, con su enlace.

## 0.2 Entrega acumulativa

El documento **crece sprint a sprint**. En cada Sprint Review se entrega la versión vigente con las secciones correspondientes completas; el profesor evalúa solo las secciones del corte, pero puede pedir corregir las anteriores.

| **Corte** | **Versión del documento** | **Secciones que deben estar completas** | **Evaluación en la que cuenta** |
| --- | --- | --- | --- |
| Review 0 (sem. 5) | v0.1 | Portada, 1, 2.1– 2.4, 3 | Parcial 1 |
| Review 1 (sem. 7) | v0.2 | + 4.1– 4.5 (borrador), 4.6, 4.7 | Parcial 1 |
| Review 2 (sem. 9) | v1.0 (SRS firmado) | + 4 completa, 5.1–5.3, 2.5 | Parcial 2 |
| Review 3 (sem. 11) | v1.1 | + 6 | Parcial 3 |
| Review 4 (sem. 13) | v1.2 | + 7.1–7.5, 9.1–9.3 | Parcial 3 |
| Review 5 (sem. 15) | v1.3 | + 7.6–7.8, 8, 9.4 | Ordinaria |
| Demo final (sem. 16) | v2.0 (final de la Fase 1) | Todo el documento, incluidas 10, 11, 12, 13 y anexos | Ordinaria |

## 0.3 Formato de entrega

* **Archivos:** este documento en Word (.docx) y en PDF, en docs/entregas/ del repositorio, y la liga del PDF en la minuta de la Review.
* **Nombre del archivo:** IS1-Fase1-Equipo<A|B>-v<versión>.pdf, por ejemplo IS1-Fase1-EquipoA-v1.0.pdf.
* **Formato:** carta, márgenes de 2.5 cm, fuente de 11 puntos, encabezados numerados, numeración de páginas, figuras y tablas numeradas.
* **Citas y referencias:** formato APA 7. Toda norma, libro o dato de terceros se cita; las referencias deben ser verificables.
* **Uso de IA:** se declara en la sección 2.6. Cualquier integrante debe poder explicar cualquier parte del documento.

Si la versión del documento no coincide con lo que hay en el repositorio y en el tablero, el profesor toma como válido el repositorio.

# Portada

***Instrucción:*** *Llenen todos los campos. El nombre del producto lo elige el equipo y se mantiene durante el proyecto.*

| **Campo** | **Dato** |
| --- | --- |
| Asignatura | Ingeniería de Software I (IDSSI-27) |
| Documento | Documento de Ingeniería del Proyecto – Fase 1 |
| Equipo | [A (6 integrantes) / B (5 integrantes)] |
| Cliente | [Cooperativa Totoperas del Istmo / Servicio Automotriz Hermanos Ruiz] |
| Nombre del producto | [Nombre que el equipo da al sistema] |
| Versión del documento | [v0.1 … v2.0] |
| Fecha | [dd/mm/aaaa] |
| Repositorio | [URL de GitHub] |

## Control de versiones

| **Versión** | **Fecha** | **Autor(es)** | **Descripción del cambio** | **Revisó** |
| --- | --- | --- | --- | --- |
| v0.1 | [dd/mm/aaaa] | [Nombres] | Versión inicial: visión y viabilidad (Sprint 0) | [Nombre] |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Aprobación del cliente

***Instrucción:*** *Se llena en la Review 2 (firma del SRS) y en la demo final (aceptación del Release v0.1.0). Si el cliente rechaza, se registra el motivo y la fecha de la nueva revisión.*

| **Hito** | **Resultado (aceptado / aceptado con observaciones / rechazado)** | **Observaciones** | **Firma del cliente** | **Fecha** |
| --- | --- | --- | --- | --- |
| SRS v1.0 (Review 2) |  |  |  |  |
| Release v0.1.0 (Demo final) |  |  |  |  |

# 1. Información general del proyecto

## 1.1 Integrantes y roles

***Instrucción:*** *Un renglón por integrante. Anoten su usuario de GitHub tal como aparece en el repositorio, porque con él se revisa la contribución individual. Si el Scrum Master rotó, indiquen en qué sprints tuvo el rol cada persona.*

| **Nombre completo** | **Matrícula** | **Usuario GitHub** | **Rol(es) y sprints** | **Áreas principales de contribución** |
| --- | --- | --- | --- | --- |
| [Nombre] | [ ] | [@usuario] | Product Owner (S0–S6) | [Requisitos, relación con el cliente…] |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 1.2 Enlaces del proyecto

| **Recurso** | **Enlace** |
| --- | --- |
| Repositorio | [URL] |
| Tablero (GitHub Projects / Jira) | [URL] |
| Prototipo de UI (Figma / Penpot) | [URL] |
| Ambiente de pruebas (staging) | [URL] (desde el Sprint 4) |
| Release v0.1.0 | [URL de GitHub Releases] |
| Canal de comunicación del equipo | [Nombre del canal] |

## 1.3 Resumen ejecutivo

***Instrucción:*** *Máximo media página, escrita para el cliente y sin jerga técnica: qué problema se resuelve, qué se entregó en la Fase 1, qué queda para la Fase 2 y cuál es el estado del producto. Esta sección se reescribe en cada versión.*

[Escriba aquí el resumen ejecutivo.]

# 2. Gestión del proyecto con Scrum

## 2.1 Acuerdos de trabajo

***Instrucción:*** *Resumen de CONTRIBUTING.md: horarios y canal de comunicación, tiempo máximo de respuesta, cómo se toman las decisiones, convenciones de ramas y commits, y consecuencias por incumplimiento.*

[Escriba aquí los acuerdos de trabajo.]

## 2.2 Definición de Listo (DoR) y Definición de Terminado (DoD)

***Instrucción:*** *Partan de la versión base del documento "Cronograma y entregables por sprint". Pueden hacerla más exigente, nunca más laxa. Registren los cambios por sprint.*

| **Definición de Listo** | **Definición de Terminado** |
| --- | --- |
| ~ [Criterios] | ~ [Criterios] |

## 2.3 Resumen de sprints

***Instrucción:*** *Un renglón por sprint terminado. La velocidad es los puntos de historia* ***terminados según la DoD****, no los iniciados. Agreguen al final la gráfica de velocidad y, si la usan, la de quemado (burndown).*

| **Sprint** | **Fechas** | **Objetivo del sprint** | **¿Se cumplió? (sí / parcial / no)** | **Puntos comprometidos** | **Puntos terminados** |
| --- | --- | --- | --- | --- | --- |
| S0 |  |  |  | — | — |
| S1 |  |  |  |  |  |
| S2 |  |  |  |  |  |
| S3 |  |  |  |  |  |
| S4 |  |  |  |  |  |
| S5 |  |  |  |  |  |
| S6 |  |  |  |  |  |

### Evidencia de los eventos

***Instrucción:*** *Por sprint, la ruta a la minuta de la Review, a la retrospectiva y a los registros del Daily en el repositorio. Para cada retrospectiva, anoten las acciones de mejora y si se aplicaron en el siguiente sprint.*

| **Sprint** | **Minuta de Review** | **Retrospectiva** | **Acciones de mejora acordadas** | **¿Se aplicaron?** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 2.4 Registro de riesgos

***Instrucción:*** *Mínimo* ***8 riesgos*** *desde el Sprint 0, actualizados en cada sprint. Probabilidad e impacto: alta / media / baja. Respuesta: evitar, mitigar, transferir o aceptar.*

| **ID** | **Riesgo** | **Probabilidad** | **Impacto** | **Respuesta y responsable** | **Estado** |
| --- | --- | --- | --- | --- | --- |
| R-01 | Un integrante abandona el curso a mitad del semestre | Media | Alto | Mitigar: conocimiento compartido mediante revisión cruzada de PR; responsable: SM | Abierto |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## 2.5 Solicitudes de cambio

***Instrucción:*** *Registren* ***todas*** *las solicitudes de cambio del cliente, ya sea que se acepten o no. Lo que se evalúa es el análisis de impacto y la negociación, no aceptar todo.*

| **ID / issue** | **Fecha** | **Solicitud del cliente** | **Impacto (requisitos, modelos, pruebas, esfuerzo)** | **Decisión y justificación** | **Release** |
| --- | --- | --- | --- | --- | --- |
| SC-01 / #[n] |  |  |  | [Aceptada / rechazada / pospuesta a Fase 2] | [v0.1.0 / Fase 2] |
|  |  |  |  |  |  |

## 2.6 Declaración de uso de inteligencia artificial

***Instrucción:*** *Indiquen qué herramientas usaron, para qué partes y cómo verificaron el resultado. También se declara no usar IA. Nunca se ingresan datos personales reales.*

| **Herramienta** | **Sección o artefacto** | **Para qué se usó** | **Cómo se verificó** | **Responsable** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |

# 3. Visión y viabilidad del producto

## 3.1 Problema y contexto del cliente

***Instrucción:*** *Describan el negocio y el problema con las palabras del cliente, apoyándose en las entrevistas (citen la minuta). No copien el anteproyecto: deben aparecer hallazgos que solo se obtuvieron mediante preguntas.*

[Escriba aquí el problema y su contexto.]

## 3.2 Objetivos del producto e indicadores

| **Objetivo** | **Indicador** | **Situación actual** | **Meta** | **Cómo se medirá** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 3.3 Alcance

| **Dentro del alcance de la Fase 1** | **Dentro del alcance de la Fase 2** | **Fuera de alcance** |
| --- | --- | --- |
| ~ [Lista] | ~ [Lista] | ~ [Lista] |

## 3.4 Stakeholders

***Instrucción:*** *Incluyan a todos los usuarios del anteproyecto y a los que descubran. Agreguen el diagrama del mapa de poder/interés.*

| **Stakeholder** | **Rol en el negocio** | **Interés en el sistema** | **Poder / interés** | **Estrategia de participación** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 3.5 Proceso actual (as-is)

***Instrucción:*** *Diagrama de actividades del proceso tal como funciona hoy, con sus problemas señalados.*

[Figura 3.1. Proceso actual. Fuente: ruta en el repositorio]

## 3.6 Estudio de viabilidad

***Instrucción:*** *Cada tipo de viabilidad con evidencia y una conclusión. La legal debe considerar la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (DOF 20-03-2025): qué datos personales se tratarán, para qué finalidades y con qué medidas de seguridad.*

| **Tipo** | **Análisis y evidencia** | **Conclusión (viable / viable con condiciones / no viable)** |
| --- | --- | --- |
| Técnica |  |  |
| Económica |  |  |
| Operativa |  |  |
| Legal |  |  |
| De calendario |  |  |

**Conclusión general:** [Escriba aquí si el proyecto es viable y bajo qué condiciones.]

# 4. Especificación de requisitos de software (SRS)

***Instrucción:*** *Estructura adaptada de ISO/IEC/IEEE 29148:2018. El SRS es lo que el cliente firma en la Review 2. Cada requisito tiene un identificador único que se utiliza para la trazabilidad.*

## 4.1 Propósito, alcance y audiencia del SRS

[Escriba aquí.]

## 4.2 Glosario del dominio

***Instrucción:*** *Mínimo* ***25 términos (Equipo A)*** *o* ***20 términos (Equipo B)****, con los nombres que usa el cliente. Los nombres de las clases del dominio (sección 6) deben salir de aquí.*

| **Término** | **Definición** | **Sinónimos que usa el cliente** |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |

## 4.3 Descripción general

### 4.3.1 Usuarios y sus características

| **Tipo de usuario** | **Tareas principales** | **Experiencia tecnológica** | **Dispositivo y contexto de uso** |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### 4.3.2 Restricciones, supuestos y dependencias

[Restricciones de presupuesto, tecnológicas, legales y de calendario; supuestos por validar; dependencias externas.]

## 4.4 Requisitos funcionales

***Instrucción:*** *Un requisito por renglón, redactado como "El sistema deberá…". Prioridad con MoSCoW. Cada requisito se vincula con las historias que lo implementan.*

| **ID** | **Requisito funcional** | **Módulo** | **Prioridad (MoSCoW)** | **Historias relacionadas** |
| --- | --- | --- | --- | --- |
| RF-01 | El sistema deberá permitir… | M1 | Must | HU-01, HU-02 |
|  |  |  |  |  |
|  |  |  |  |  |

## 4.5 Historias de usuario (Product Backlog)

***Instrucción:*** *Mínimo* ***35 historias (Equipo A)*** *o* ***30 historias (Equipo B)****. Las de prioridad Must incluyen al menos 2 criterios de aceptación en formato Dado-Cuando-Entonces y cumplen con INVEST. Incluyan aquí la tabla resumen y el detalle de las historias del flujo núcleo; el resto puede quedar en el tablero con su enlace. Agreguen la imagen del story map con el corte del release v0.1.0.*

| **ID / issue** | **Historia (Como… quiero… para…)** | **Prioridad** | **Puntos** | **Release** | **Estado** |
| --- | --- | --- | --- | --- | --- |
| HU-01 / #[n] | Como [rol], quiero [capacidad], para [beneficio] | Must | 3 | v0.1.0 | Terminada |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

### Detalle de una historia (repetir por cada historia del flujo núcleo)

| **Campo** | **Contenido** |
| --- | --- |
| ID e issue |  |
| Historia | Como [rol], quiero [capacidad], para [beneficio] |
| Criterio de aceptación 1 | Dado [contexto], cuando [acción], entonces [resultado verificable] |
| Criterio de aceptación 2 | Dado…, cuando…, entonces… |
| Reglas de negocio | RN-… |
| Wireframe | [Enlace o figura] |
| Casos de prueba | CPA-… |

[Figura 4.1. Story map con el corte del release v0.1.0.]

## 4.6 Requisitos no funcionales

***Instrucción:*** *Mínimo* ***12 (Equipo A)*** *o* ***10 (Equipo B)****, clasificados según las nueve características de* ***ISO/IEC 25010:2023****. Cada uno debe ser medible: con una métrica, un umbral y una forma de verificarlo. "El sistema será rápido" no se acepta.*

| **ID** | **Característica ISO/IEC 25010:2023** | **Requisito** | **Métrica y umbral** | **Cómo se verificará** |
| --- | --- | --- | --- | --- |
| RNF-01 | Eficiencia de desempeño | La búsqueda de clientes… | Menos de 2 s con 5,000 registros | Prueba de rendimiento con datos ficticios |
|  |  |  |  |  |
|  |  |  |  |  |

## 4.7 Reglas de negocio y requisitos de dominio

***Instrucción:*** *Incluyan las reglas del anteproyecto y las descubiertas en las entrevistas, con la fuente de cada una.*

| **ID** | **Regla de negocio** | **Fuente (anteproyecto / entrevista con fecha)** | **Requisitos que afecta** |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 4.8 Requisitos de protección de datos personales

***Instrucción:*** *Qué datos personales se recaban, con qué finalidad, quién puede consultarlos y qué medidas de seguridad se aplicarán. Incluyan un borrador del aviso de privacidad.*

[Escriba aquí.]

## 4.9 Casos de uso

***Instrucción:*** *Diagrama de casos de uso de cada módulo, con un mínimo de* ***8 casos documentados (Equipo A)*** *o* ***7 (Equipo B)****, incluidos todos los del flujo núcleo. Un caso de uso es un objetivo del actor ("Registrar pedido"), no una pantalla.*

[Figura 4.2. Diagrama de casos de uso del módulo …]

### Plantilla de caso de uso (repetir por cada caso)

| **Campo** | **Contenido** |
| --- | --- |
| ID y nombre | CU-01 Registrar pedido |
| Actor principal |  |
| Actores secundarios |  |
| Descripción breve |  |
| Precondiciones |  |
| Flujo principal | 1. El actor…  2. El sistema… |
| Flujos alternos | A1 (paso n): … |
| Flujos de excepción | E1 (paso n): … |
| Postcondiciones |  |
| Reglas de negocio | RN-… |
| Requisitos relacionados | RF-…, HU-… |

## 4.10 Prototipos de baja fidelidad

***Instrucción:*** *Wireframes de todas las pantallas del flujo núcleo, cada uno con la historia o el caso de uso que representa.*

[Figuras 4.x. Wireframes.]

## 4.11 Validación de requisitos con el cliente

***Instrucción:*** *Resumen de las sesiones de validación: qué se mostró, qué cambió y qué acordó el cliente. Incluyan los defectos de documentación que reportó el otro equipo en la revisión cruzada y cómo se atendieron.*

| **Fecha** | **Técnica (recorrido, prototipo, revisión)** | **Hallazgos** | **Cambios acordados** |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

# 5. Plan de pruebas y trazabilidad

## 5.1 Plan de pruebas

***Instrucción:*** *Estructura adaptada de ISO/IEC/IEEE 29119-3:2021.*

| **Apartado** | **Contenido** |
| --- | --- |
| Alcance | [Qué se prueba y qué no en la Fase 1] |
| Niveles de prueba | [Unitarias, integración, sistema, aceptación] |
| Enfoque | [Manual / automatizado; herramientas] |
| Entornos | [Local, CI, staging; datos ficticios] |
| Criterios de entrada |  |
| Criterios de salida | [Por ejemplo: 0 defectos S1/S2 abiertos] |
| Roles | [QA Lead, developers, equipo contrario, cliente] |
| Riesgos de las pruebas |  |
| Calendario | [Por sprint] |

## 5.2 Casos de prueba de aceptación

***Instrucción:*** *Mínimo* ***25 casos (Equipo A)*** *o* ***20 (Equipo B)****, cada uno vinculado a una historia o caso de uso. Incluyan casos de flujos alternos, valores límite y control de acceso por rol. La columna de resultado se llena al ejecutarlos (sección 10).*

| **ID** | **Historia / CU** | **Precondiciones** | **Pasos** | **Resultado esperado** | **Resultado (Pasa / Falla / Bloqueado)** |
| --- | --- | --- | --- | --- | --- |
| CPA-01 | HU-… |  | 1. …  2. … |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## 5.3 Matriz de trazabilidad

***Instrucción:*** *Ningún requisito Must puede quedar sin historia ni caso de prueba. Se actualiza en cada versión y en el Sprint 6 incluye el resultado de las pruebas.*

| **Requisito** | **Historias** | **Caso de uso** | **Casos de prueba** | **Componente / módulo** | **Resultado** |
| --- | --- | --- | --- | --- | --- |
| RF-01 | HU-01, HU-02 | CU-01 | CPA-01, CPA-02 | [Paquete o clase] | [Pasa] |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

# 6. Modelos de análisis

***Instrucción:*** *Todos los modelos deben ser consistentes con el glosario y el SRS. Notación UML 2.5.1. Cada figura debe tener número, título y ruta de su archivo fuente.*

## 6.1 Diagramas de flujo de datos

***Instrucción:*** *Nivel de contexto, nivel 0 y nivel 1 de un proceso principal. Los flujos deben estar equilibrados entre niveles.*

[Figuras 6.1 a 6.3.]

## 6.2 Modelo de datos

***Instrucción:*** *Diagrama entidad-relación normalizado al menos a 3FN, y diccionario de datos.*

[Figura 6.4. Modelo entidad-relación.]

| **Entidad** | **Atributo** | **Tipo** | **Nulo** | **Restricciones (PK, FK, único, rango)** | **Descripción** |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## 6.3 Diagrama de clases del dominio

***Instrucción:*** *Mínimo* ***14 clases (Equipo A)*** *o* ***12 (Equipo B)****, con atributos, asociaciones y multiplicidades. Sin métodos de implementación ni clases técnicas (como controladores o repositorios).*

[Figura 6.5.]

## 6.4 Diagrama de objetos

***Instrucción:*** *Instantánea con datos ficticios realistas que valide un escenario del flujo núcleo.*

[Figura 6.6.]

## 6.5 Diagramas de estados

***Instrucción:*** *Equipo A: como mínimo* ***Pedido*** *y* ***Entrega****. Equipo B: como mínimo* ***Orden de servicio*** *y* ***Cotización****. Cada transición indica un evento, una condición y un rol autorizado.*

[Figuras 6.7 y 6.8.]

| **Estado origen** | **Evento** | **Condición** | **Estado destino** | **Rol autorizado** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 6.6 Diagramas de actividades (to-be)

***Instrucción:*** *Al menos dos procesos clave cómo funcionarán con el sistema, con carriles por rol.*

[Figuras 6.9 y 6.10.]

# 7. Arquitectura y diseño

## 7.1 Estilo arquitectónico

***Instrucción:*** *Expliquen el estilo elegido (capas, MVC, cliente-servidor con API…) y cómo atiende al menos* ***4 requisitos no funcionales*** *de la sección 4.6.*

| **RNF** | **Decisión de arquitectura que lo atiende** |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |

## 7.2 Diagramas C4

***Instrucción:*** *Contexto, Contenedores y Componentes de al menos un contenedor.*

[Figuras 7.1 a 7.3.]

## 7.3 Registros de decisiones de arquitectura (ADR)

***Instrucción:*** *Mínimo* ***4 ADR****: estilo arquitectónico, pila tecnológica, base de datos y hospedaje. Equipo A: un ADR adicional sobre el soporte sin conexión. Equipo B: un ADR adicional sobre el almacenamiento de fotos y el acceso del cliente mediante un enlace seguro. Cada ADR evalúa al menos dos alternativas.*

### Plantilla de ADR (repetir por cada decisión)

| **Campo** | **Contenido** |
| --- | --- |
| ID y título | ADR-001 [Decisión] |
| Fecha y estado | [Propuesto / aceptado / reemplazado por ADR-…] |
| Contexto | [Qué problema o fuerza obliga a decidir] |
| Alternativas evaluadas | 1. … 2. … |
| Decisión |  |
| Consecuencias | [Positivas y negativas; qué se vuelve más fácil o más difícil] |
| RNF relacionados | RNF-… |

## 7.4 Diagramas de artefactos y de despliegue

***Instrucción:*** *Deben reflejar el ambiente de pruebas real: nodos, artefactos instalados y protocolos de comunicación.*

[Figuras 7.4 y 7.5.]

## 7.5 Diagrama de paquetes

***Instrucción:*** *Organización de módulos y sus dependencias, sin dependencias circulares.*

[Figura 7.6.]

## 7.6 Diagramas de clases de la solución

***Instrucción:*** *Clases del flujo del núcleo tal como existen en el código (controladores, servicios, repositorios, entidades). Deben coincidir con el repositorio.*

[Figura 7.7.]

## 7.7 Diagramas de secuencia

***Instrucción:*** *Mínimo* ***4****, incluido el escenario principal del flujo del núcleo.*

[Figuras 7.8 a 7.11.]

## 7.8 Diagrama de comunicación

***Instrucción:*** *Al menos uno.*

[Figura 7.12.]

# 8. Diseño de la interfaz de usuario

## 8.1 Prototipo de alta fidelidad

***Instrucción:*** *Enlace al prototipo navegable y capturas del flujo principal y de dos flujos adicionales. Expliquen las decisiones de diseño según el contexto de uso de cada tipo de usuario (dispositivo, conectividad, experiencia).*

[Enlace y figuras.]

## 8.2 Accesibilidad

***Instrucción:*** *Qué criterios de WCAG 2.2 se consideraron (contraste, tamaño de objetivos táctiles, textos alternativos, navegación por teclado) y cómo se verificaron.*

[Escriba aquí.]

## 8.3 Evaluación heurística recibida

***Instrucción:*** *Hallazgos que reportó el otro equipo con las 10 heurísticas de Nielsen, y cómo se atendieron.*

| **Issue** | **Heurística** | **Hallazgo** | **Severidad** | **Acción tomada** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 8.4 Prueba con usuarios y SUS

***Instrucción:*** *Prueba con* ***3 a 5 personas*** *ajenas al equipo:* *tareas que realizaron, problemas observados, puntaje* *promedio del SUS con su cálculo y cambios derivados.*

| **Participante (perfil, sin nombre)** | **Tarea** | **¿La completó?** | **Tiempo** | **Problemas observados** | **Puntaje SUS** |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

**Puntaje SUS promedio:** [ ] · **Cambios realizados a partir de la prueba:** [ ]

# 9. Implementación del Release v0.1.0

## 9.1 Pila tecnológica

| **Capa** | **Tecnología y versión** | **ADR que la justifica** |
| --- | --- | --- |
| Interfaz |  |  |
| Lógica de negocio / API |  |  |
| Base de datos |  |  |
| Hospedaje del ambiente de pruebas |  |  |
| Integración continua |  |  |

## 9.2 Instrucciones de instalación y ejecución

***Instrucción:*** *Pasos para que una persona ajena al equipo instale y ejecute el sistema localmente siguiendo el README. Incluyan cómo cargar los datos de prueba ficticios.*

[Escriba aquí o indique la sección del README.]

## 9.3 Integración continua y flujo de trabajo

***Instrucción:*** *Qué ejecuta el pipeline (compilación, linter, pruebas), reglas de protección de main y estadísticas del repositorio: número de pull requests fusionados y revisados.*

[Escriba aquí y agregue una captura de pantalla de una ejecución exitosa.]

## 9.4 Evidencia del flujo núcleo

***Instrucción:*** *Capturas paso a paso del flujo del núcleo funcionando en el* ***ambiente de pruebas*** *(no en local), con datos ficticios. Equipo A: registro de pedido, cálculo del total por tipo de cliente y consulta de la producción requerida. Equipo B: apertura de orden con checklist, diagnóstico, cotización con autorización registrada y lista de órdenes abiertas.*

[Figuras 9.x.]

# 10. Reporte final de pruebas e incidencias

## 10.1 Resultado de los casos de prueba

| **Indicador** | **Valor** |
| --- | --- |
| Casos de prueba diseñados |  |
| Casos ejecutados |  |
| Pasan |  |
| Fallan |  |
| Bloqueados |  |
| Pruebas unitarias automatizadas (número y resultado en CI) |  |

## 10.2 Incidencias

***Instrucción:*** *Incluyan las de todos los orígenes: internas, QA cruzado y cliente. El tiempo de atención se mide desde que se registró hasta que se cerró.*

| **Severidad** | **Registradas** | **Cerradas** | **Rechazadas (con justificación)** | **Abiertas** | **Tiempo promedio de atención** |
| --- | --- | --- | --- | --- | --- |
| S1 |  |  |  |  |  |
| S2 |  |  |  |  |  |
| S3 |  |  |  |  |  |
| S4 |  |  |  |  |  |

## 10.3 Defectos conocidos que pasan a la Fase 2

| **Issue** | **Descripción** | **Severidad** | **Prioridad** | **Motivo por el que no se corrigió** |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |

## 10.4 QA cruzado realizado al otro equipo

***Instrucción:*** *Resumen de los casos ejecutados en* *el sistema del otro equipo, los defectos reportados y las* *correcciones verificadas en la ronda 2.*

[Escriba aquí.]

# 11. Paquete de transferencia a la Fase 2

***Instrucción:*** *Lo necesario para que un equipo, incluso uno distinto, continúe el proyecto de Ingeniería de Software II.*

| **Apartado** | **Contenido** |
| --- | --- |
| Backlog restante priorizado | [Enlace y resumen por módulo] |
| Deuda técnica conocida |  |
| Riesgos abiertos |  |
| Decisiones pendientes con el cliente |  |
| Accesos y configuración | [Qué cuentas y servicios existen; nunca contraseñas en el documento] |
| Recomendaciones |  |

# 12. Retrospectiva del proyecto y contribución individual

## 12.1 Retrospectiva del proyecto

| **¿Qué funcionó bien?** | **¿Qué no funcionó?** | **¿Qué haríamos distinto en la Fase 2?** |
| --- | --- | --- |
| ~ [ ] | ~ [ ] | ~ [ ] |

## 12.2 Contribución individual

***Instrucción:*** *Cada integrante describe, con sus propias palabras, su aporte y enlaza la evidencia. El profesor lo contrasta con el repositorio, el tablero y la coevaluación; esta última se entrega por separado en un formulario privado.*

| **Integrante** | **Principales aportes** | **Evidencia (issues, PR, documentos)** | **Revisiones de código o documentos hechas a otros** |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

# 13. Referencias

***Instrucción:*** *Formato APA 7, en orden alfabético. Solo fuentes que realmente consultaron y que se pueden verificar. Como mínimo deben aparecer las normas y guías que usaron:*

Schwaber, K., & Sutherland, J. (2020). *La Guía de Scrum*. [<u>https://scrumguides.org/</u>](https://scrumguides.org/)

ISO/IEC/IEEE. (2018). *ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering*. ISO.

ISO/IEC. (2023). *ISO/IEC 25010:2023 Systems and software engineering — SQuaRE — Product quality model*. ISO.

ISO/IEC/IEEE. (2021). *ISO/IEC/IEEE 29119-3:2021 Software and systems engineering — Software testing — Part 3: Test documentation*. ISO.

Object Management Group. (2017). *OMG Unified Modeling Language, Version 2.5.1*. [<u>https://www.omg.org/spec/UML/2.5.1</u>](https://www.omg.org/spec/UML/2.5.1)

[Agreguen aquí el resto de sus referencias.]

# Anexos

***Instrucción:*** *Numeren los anexos con letras. Contenido mínimo:*

* **Anexo A.** Guiones y minutas de las entrevistas con el cliente (mínimo 20 preguntas en el guion inicial).
* **Anexo B.** Minutas de las Sprint Reviews con aceptaciones y rechazos del cliente.
* **Anexo C.** Detalle completo de las historias de usuario y los casos de prueba, si no caben en el cuerpo.
* **Anexo D.** Manual breve de uso del flujo del núcleo (Equipo A: para la auxiliar de oficina; Equipo B: para la recepcionista).
* **Anexo E.** Aviso de privacidad (borrador).

# Lista de verificación antes de entregar

***Instrucción:*** *Revísenla en equipo antes de cada entrega. Bórrenla del documento final o déjenla marcada como evidencia de revisión.*

| **✓** | **Verificación** |
| --- | --- |
| ☐ | Se borraron todas las instrucciones y los marcadores entre corchetes. |
| ☐ | La portada, el control de versiones y los enlaces están actualizados. |
| ☐ | Las secciones del corte están completas según la tabla 0.2. |
| ☐ | Se alcanzan los mínimos de su equipo: historias, RNF, glosario, casos de uso, casos de prueba, clases del dominio, ADR, secuencias y riesgos. |
| ☐ | Todo requisito no funcional tiene una métrica y un umbral. |
| ☐ | La matriz de trazabilidad no tiene requisitos Must con historia ni caso de prueba. |
| ☐ | Los nombres del glosario, del SRS, de los modelos y del código coinciden. |
| ☐ | Cada figura tiene número, título, es legible y su archivo fuente está en el repositorio. |
| ☐ | Las solicitudes de cambio y las incidencias están registradas junto con su decisión. |
| ☐ | Se declaró el uso de IA. |
| ☐ | No hay datos personales reales ni contraseñas en el documento ni en el repositorio. |
| ☐ | Las referencias están en formato APA 7 y son verificables. |
| ☐ | El PDF y el .docx están en docs/entregas/ con el nombre correcto. |
| ☐ | Otro integrante, distinto del autor principal, revisó el documento completo. |