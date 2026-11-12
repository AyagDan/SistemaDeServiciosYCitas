Propuesta de Solución Tecnológica: Sistema de Órdenes de Servicio y Citas

Proyecto: Automatización y Control del Ciclo de Servicio

Empresa Solicitante: Servicio Automotriz Hermanos Ruiz, S.A. de C.V.

Equipo Proveedor: Equipo B (5 integrantes)

1. Resumen Ejecutivo y Enfoque

Nuestro objetivo es transformar la operación manual actual (cuadernos, llamadas constantes y órdenes en papel) en una plataforma digital ágil, transparente y segura. Trabajaremos bajo la metodología Scrum en sprints de dos semanas, garantizando entregas incrementales y revisiones continuas (*Sprint Reviews*) para asegurar que el sistema se adapte exactamente a las necesidades reales del taller.

1. solución a los problemas actuales del taller

La propuesta de software ataca directamente los 5 puntos críticos que hoy le cuestan dinero y clientes a la empresa:

* Fin a las disputas por costos: Toda cotización y su respectiva autorización quedarán registradas digitalmente con fecha, hora, monto y medio de aprobación, eliminando el "dijo que sí, pero cobra otra cosa".
* Reducción de llamadas innecesarias: Implementaremos un sistema de notificaciones y un enlace seguro web para que los clientes consulten el estado de su vehículo desde su celular sin saturar a la recepcionista.
* Control de vehículos y bahías: Visualización en tiempo real de las 4 bahías de trabajo y el estatus de las refacciones para evitar unidades detenidas sin justificación.
* Historial vehicular unificado: Cada vez que un cliente regrese, el sistema mostrará el historial completo de reparaciones anteriores y garantías vigentes.
* Evidencia contra reclamos por daños: El módulo de recepción incluirá un *checklist* digital y carga fotográfica obligatoria del estado inicial del vehículo.

1. Propuesta de Arquitectura y Alcance Funcional

Para cumplir con las restricciones del proyecto (uso exclusivo de herramientas gratuitas, de código abierto y planes educativos), proponemos una arquitectura moderna basada en microservicios y APIs:

* Backend / Lógica de Negocio: Desarrollado en Python con FastAPI, garantizando alta velocidad de respuesta, seguridad y la generación automática de documentación técnica.
* Interfaz de Usuario (Frontend):
  + *Para el personal (Gerente, Recepción, Mecánicos, Almacén):* Una interfaz web optimizada (con botones grandes y accesibles para tabletas en el área de trabajo con ruido y manos sucias).
  + *Para el Cliente:* Una vista web responsiva accesible mediante un enlace seguro enviado por correo o mensaje, sin necesidad de instalar aplicaciones móviles.
* Control de Versiones y Despliegue: Repositorio centralizado en GitHub de la organización del curso, asegurando transparencia y trazabilidad mediante *Pull Requests* y ramas de desarrollo.

1. Enfoque del Primer Producto Mínimo Funcional (Release v0.1.0)

Para la Fase 1, nos enfocaremos en construir y desplegar el flujo núcleo operativo de extremo a extremo:

1. Recepción: La recepcionista registra al cliente, vehículo, kilometraje, nivel de combustible y fotos de ingreso.
2. Diagnóstico y Asignación: La orden se asigna a un mecánico y a una de las 4 bahías disponibles, registrando el diagnóstico técnico.
3. Cotización y Autorización: Se genera el presupuesto de mano de obra y refacciones, enviándolo al cliente para su validación digital registrada.
4. Monitoreo Gerencial: El gerente cuenta con un panel para visualizar las órdenes abiertas, sus estados actuales y la carga de trabajo del taller.

5. Consideraciones Legales y de Seguridad

Debido al manejo de información de clientes, el sistema cumplirá estrictamente con las directrices de la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (DOF), incorporando avisos de privacidad y uso exclusivo de datos ficticios durante las fases de prueba y desarrollo.