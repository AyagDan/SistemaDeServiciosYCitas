Universidad del Istmo · Campus Ixtepec

Ingeniería en Desarrollo de Software y Sistemas Inteligentes

Ingeniería de Software I (IDSSI) · Quinto semestre

**Revisión y observaciones · Equipo B**

Retroalimentación del Documento de Ingeniería · Corte Review 1

**Equipo B (5 integrantes):** Sistema de Órdenes de Servicio y Citas · Servicio Automotriz Hermanos Ruiz

**Documento revisado:** versión v0.1

**Fecha de entrega de esta revisión:** martes 10 de noviembre de 2026

**Fecha límite para correcciones:** viernes 27 de noviembre de 2026, 23:59 h.

**Contenido**

1. Resultado de la revisión

2. Lo que hicieron bien

3. Observaciones por atender

4. Plan de atención y fecha de entrega

5. Cómo entregar las correcciones

# 1. Resultado de la revisión

Se revisó su Documento de Ingeniería (versión v0.1) contra el **machote del Documento de Ingeniería – Fase 1** y la **rúbrica general de equipo por sprint** del curso, en el corte de la **Review 1**. Ese corte exige: portada; sección 1; 2.1 a 2.4; sección 3; 4.1 a 4.3; 4.5 (borrador); 4.6 y 4.7.

Su documento va mucho más allá de ese corte. Ese avance se revisó y se comentó, pero la rúbrica no otorga puntos extra por adelantarse: solo se evalúa si mejora o empeora la corrección y la consistencia.

| **Criterio de la rúbrica** | **Peso** | **Nivel obtenido** | **Puntos** |
| --- | --- | --- | --- |
| Completitud de entregables | 25% | Satisfactorio (3) | 18.75 |
| Corrección técnica | 25% | Satisfactorio (3) | 18.75 |
| Consistencia y trazabilidad | 15% | Satisfactorio (3) | 11.25 |
| Valor para el cliente | 10% | Excelente (4) | 10.00 |
| Proceso Scrum | 15% | Suficiente (2) | 7.50 |
| Gestión de incidencias | 10% | No evaluable en este corte | — |
| **Subtotal** | **90%** |  | **66.25 / 90** |
| **Calificación del documento** |  | 66.25 ÷ 90 × 10 | **7.4 / 10** |

La gestión de incidencias no se calificó en este corte porque la revisión cruzada comienza en el Sprint 2. La calificación se calculó sobre el 90% restante de la rúbrica y se convirtió a una escala de 10.

# 2. Lo que hicieron bien

* **Hallazgos propios del cliente:** separan explícitamente lo que vino del anteproyecto de lo que descubrieron en la entrevista (código de verificación, aprobación de conceptos por separado, reubicación por espera de refacciones, confirmación manual de citas, mecánico responsable). Las reglas citan su fuente con fecha. Este fue el criterio mejor calificado.
* **Requisitos no funcionales muy bien definidos:** todos son medibles y verificables. Destacan RNF-04 (huella SHA-256 para detectar alteraciones) y RNF-09 (200 registros, 0 duplicados, interrupción a mitad de la sincronización).
* **Plan de pruebas de nivel profesional:** 35 casos con valores límite correctos (día 5 frente a 6, 10% exacto frente a 10.06%, 5 min frente a 5 min 1 s) y control de acceso, incluido el intento de abrir la orden de otro cliente (OWASP A01). Están automatizados y la matriz de trazabilidad llega hasta el módulo de código.
* **Otros avances:** 13 casos de uso con flujos alternos (el mínimo era de 7), 6 ADR con alternativas evaluadas, protección de datos con aviso de privacidad y backend con integración continua.
* **Riesgos y declaración de IA:** registro de 12 riesgos bien diferenciados (incluido uno cerrado con su acción) y una declaración detallada sobre el uso de IA.

# 3. Observaciones por atender

Están ordenadas por sección. La severidad indica qué tanto afecta la calidad del documento: **Alta** (bloquea la firma del SRS), **Media** (debe corregirse antes de la Review 2) y **Baja** (corrección menor).

| **#** | **Sección** | **Qué encontramos** | **Qué deben hacer (se considera atendida cuando…)** | **Severidad** |
| --- | --- | --- | --- | --- |
| B1 | Figuras en general | De unas 40 figuras, solo 3 o 4 son diagramas reales (as-is y de clases del dominio). El resto son recuadros "Pendiente" con una descripción. Las historias citan wireframes (Figuras 4.5 a 4.10) que no existen. Describir un diagrama no equivale a entregarlo. | Entregar, como diagramas reales y con el archivo fuente en el repositorio, las figuras correspondientes al SRS: el story map (4.1), los tres diagramas de casos de uso (4.2 a 4.4) y los seis wireframes (4.5 a 4.10). Las figuras de análisis y diseño pueden quedar para su sprint, pero **sin citarlas como si existieran**. Atendida cuando no hay referencias a figuras inexistentes. | Alta |
| B2 | 3.3 y 4.5 | **Alcance sobredimensionado.** Casi todo el sistema está en la versión 0.1.0. El anteproyecto pide ,para la Fase 1 ,solo el flujo núcleo funcionando y el resto especificado y diseñado. La operación sin conexión (HU-25 y HU-26, 16 puntos) es su mayor riesgo técnico (R-02) y está comprometida para v0.1.0. | Proponer un Release v0.1.0 centrado en el flujo núcleo del anteproyecto, negociarlo con el cliente y actualizar 3.3, 3.6, el release de cada historia en 4.5 y el story map. Atendida cuando el cliente aceptó el nuevo alcance y queda registrado en la minuta. | Alta |
| B3 | Anexo A y 4.11 | Se cita la entrevista del 19/10/2026, pero no hay guion ni minuta. Los anexos todavía contienen el texto de las instrucciones del machote. | Agregar el guion y la minuta de la entrevista como Anexo A, y reemplazar el texto del machote por los anexos reales. Atendida cuando cada regla "de entrevista" en 4.7 puede rastrearse hasta la minuta. | Media |
| B4 | 2.3, 1.2, 4.5 y 12.2 | La evidencia del proceso es débil: no hay fechas ni puntos de ningún sprint; por lo tanto, no es posible calcular la velocidad. Los issues aparecen como "#[1]", y el tablero y las minutas de Review como "Pendiente". La columna de revisiones hechas a otros está vacía, aunque su DoD exige una revisión en cada PR. | Registrar las 30 historias como issues reales en el tablero y poner su número en 4.5; completar las fechas y los puntos de 2.3; agregar las minutas de Review y de retrospectiva; llenar en 12.2 las revisiones de PR que hizo cada integrante. Atendida cuando cada dato puede comprobarse en GitHub. | Alta |
| B5 | 2.1 y 9.3 | Usan una rama por rol de Scrum (rol/developers, rol/qa-lead). No es una práctica de la industria: mezcla el trabajo de varias personas e historias y diluye la revisión. | Cambiar a una rama por historia o tarea (GitHub Flow, como se vio en clase) y actualizar el CONTRIBUTING.md y la sección 2.1. Atendida cuando las ramas nuevas siguen la convención tipo/número-descripción. | Media |
| B6 | 2.6 y 12.2 | La declaración de IA indica que el backend, las 35 pruebas, la integración continua y las secciones 5, 6, 7, 9 y 10.1 fueron generados con la ayuda de un asistente, bajo la responsabilidad de **un solo integrante**. Declararlo es correcto, pero concentra el trabajo y el conocimiento. La fila "Por declarar" deja sin declarar el resto del documento. | Completar la declaración en todas las secciones y realizar una sesión interna en la que el Tech Lead explique al equipo la estructura del backend, las reglas implementadas y las pruebas. Recuerden que en la Review cualquier integrante puede ser preguntado sobre el código. Atendida cuando no hay filas "Por declarar" y la sesión tiene minuta. | Media |
| B7 | 6.5 | La máquina de estados de la Orden no tiene el estado "En reparación" ni estados para esperar refacción (RN-06) o autorización adicional (RN-04). La HU-09 habla de "En Diagnóstico" y el modelo de "Diagnosticada". | Agregar los estados y transiciones faltantes al modelo y a la tabla TRANSICIONES del código, con sus pruebas, y unificar los nombres de los estados en las historias, el modelo y el código. Atendida cuando el modelo, las historias y el código usan los mismos estados y las pruebas pasan. | Media |
| B8 | 4.6 | RNF-07 (usar herramientas gratuitas) es una restricción del proyecto, no una característica de calidad. RNF-05 exige cifrar "datos sensibles", pero 3.6 establece que no se tratan. No hay RNF de compatibilidad, de adecuación funcional ni de protección. | Mover RNF-07 a restricciones (4.3.2), corregir RNF-05 y agregar RNF medibles de compatibilidad, adecuación funcional y protección. Atendida cuando las nueve características de ISO/IEC 25010:2023 están consideradas. | Baja |
| B9 | 4.5 | Varios criterios de aceptación no son verificables por falta de datos concretos: "filtra instantáneamente" (HU-05), "firma visual o sello" (HU-01). | Reescribir los criterios vagos de todas las historias en criterios medibles. Atendida cuando cada criterio tiene un resultado que puede comprobarse mediante una prueba. | Baja |
| B10 | 4.7.1 | Los procedimientos de contingencia (lectura OBD-II, trasvase de combustible) demuestran conocimiento del dominio, pero son una propuesta del equipo no validada y añaden alcance que nadie pidió. | Presentarlos al cliente durante la sesión de B2. Si no los acepta, retirarlos del SRS o moverlos a la Fase 2. Atendida cuando su estado queda en la minuta. | Baja |
| B11 | Portada y 3.4 | El documento se llama v0.1 aunque su contenido corresponde a una versión más avanzada. Incluye al "equipo de desarrollo" y al "docente evaluador" como stakeholders del producto. | Versionar según el machote y, en la versión 3.4, retirar a quienes no sean stakeholders del producto. | Baja |

# 4. Plan de atención y fecha de entrega

**Fecha límite para entregar todas las correcciones: viernes 27 de noviembre de 2026, 23:59 h.** Las observaciones de severidad Alta (B1, B2 y B4) deben ser atendidas a más tardar el **viernes 20 de noviembre**, salvo los wireframes (lunes 23).

| **#** | **Actividad** | **Rol sugerido** | **Horas-persona** | **Fecha límite** |
| --- | --- | --- | --- | --- |
| B1 | Story map, 3 diagramas de casos de uso y 6 wireframes; quitar referencias a figuras inexistentes | Developers (interfaz) + QA Lead | 12 | Story map y casos de uso: vie 20 nov  Wireframes: lun 23 nov |
| B2 | Reducir el Release v0.1.0 y negociarlo con el cliente | Product Owner | 4 | Propuesta: vie 13 nov  Negociación y cambios: vie 20 nov |
| B3 | Guion y minuta de la entrevista; limpiar anexos | Product Owner | 3 | Jue 12 nov |
| B4 | Issues reales, fechas y puntos, minutas y revisiones por integrante | Scrum Master | 7,5 | Vie 13 nov |
| B5 | Cambiar a una rama por historia y actualizar CONTRIBUTING.md | Scrum Master | 2 | Mié 11 nov |
| B6 | Completar declaración de IA y sesión interna de transferencia del código | Tech Lead + todo el equipo | 8,5 | Declaración: vie 13 nov  Sesión: mié 18 nov |
| B7 | Corregir la máquina de estados (modelo, código y pruebas) | Tech Lead + QA Lead | 8 | Mié 25 nov |
| B8 | Reclasificar y completar los RNF | Developer (SRS) | 3 | Lun 23 nov |
| B9 | Hacer verificables los criterios de aceptación | Developer (SRS) + QA Lead | 2 | Mar 24 nov |
| B10 | Validar con el cliente los procedimientos de contingencia | Product Owner | 1 | Vie 20 nov |
| B11 | Corregir versión y stakeholders | Scrum Master | 0,5 | Mar 10 nov |
| — | Integrar los cambios, revisión cruzada interna y generar el PDF | Scrum Master | 2,5 | Vie 27 nov |
|  | **Total estimado** |  | **54 h** |  |

## 4.1 Cómo se calcularon los tiempos

* **Capacidad del equipo:** según el cronograma del curso, cada integrante dedica al proyecto unas 7 horas a la semana (1 hora en clase y 6 fuera de clase). Con 5 integrantes son 35 horas por semana.
* **Dedicación a las correcciones:** se supone que el equipo dedica el **60%** de esa capacidad a estas correcciones y el resto a seguir avanzando en el sprint en curso. Eso da **21 horas por semana**, unas 4,2 horas por día hábil. Se usa el 60% en lugar del 50% porque el equipo ya adelantó trabajo de sprints posteriores (pruebas, modelos y backend) y puede concentrarse más en la corrección.
* **Calendario:** se cuenta a partir del **martes 10 de noviembre de 2026**, en días hábiles (lunes a viernes). El **lunes 16 de noviembre** no se cuenta porque es día de descanso oficial (tercer lunes de noviembre, conmemoración de la Revolución Mexicana).
* **Resultado:** el trabajo estimado cabe en **14 días hábiles**, por lo que la fecha de entrega es el **viernes** **27 de noviembre de 2026**. Incluye un margen pequeño para imprevistos.
* **Orden:** las fechas parciales priorizan lo más urgente y lo que otras tareas necesitan (por ejemplo, la sesión con el cliente antes de rehacer los modelos que dependen de ella).
* **Dependencia importante:** el story map (B1) depende del nuevo alcance (B2), y B10 se valida en la misma sesión con el cliente que B2. Conviene pedir esa sesión para la semana del 17 al 20 de noviembre.

# 5. Cómo entregar las correcciones

1. **Registren cada observación como un issue** en su repositorio, con el ID de este documento en el título (por ejemplo, "B2 · Rehacer proceso actual"). Etiquetas: tipo:defecto-doc, severidad (sev:S2 para Alta, sev:S3 para Media, sev:S4 para Baja) y origen:cliente. Asígnenlo a un responsable con la fecha límite indicada en la tabla.
2. **Corrijan en una rama por observación o por grupo de observaciones relacionadas,** e integrenla a main mediante un pull request revisado por otro integrante. El PR debe cerrar su issue (Closes #n).
3. **Actualicen el documento** a la versión **v0.2**, con una nueva fila en el control de versiones que indique "Atención a las observaciones de la Review 1".
4. **Agreguen al documento un anexo** titulado **"Atención de observaciones"** con una tabla que incluya: ID de la observación, issue, PR y cómo se resolvió. Si deciden no atender alguna, expliquen por qué; un rechazo justificado es válido.
5. **Suban el PDF y el .docx a `docs/entregas/`** con el nombre del machote y avisen en el canal del curso.

Lo que entreguen después de la fecha límite, o sin issue y PR que lo respalde, se considera no atendido. La forma en que gestionen estas observaciones cuenta para el criterio "Gestión de incidencias" del siguiente corte.