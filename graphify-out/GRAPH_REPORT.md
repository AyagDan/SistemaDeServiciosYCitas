# Graph Report - Florentino  (2026-11-05)

## Corpus Check
- 34 files · ~77,385 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 25 file(s) not represented in the graph (top: .tex 17, .puml 5, (none) 1)

## Summary
- 550 nodes · 1531 edges · 22 communities (21 shown, 1 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 265 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f963b4f9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- conftest.py
- RolUsuario
- Acuerdos de trabajo · Equipo B
- Usuario
- models.py
- with
- main.py
- schemas.py
- ordenes.py
- 4. Especificación de requisitos de software (SRS)
- cobro.py
- IS1-Fase1-EquipoB-v1.1_5717b748.md
- 7. Arquitectura y diseño
- 2. Gestión del proyecto con Scrum
- 3. Visión y viabilidad del producto
- 6. Modelos de análisis
- Sistema de Órdenes de Servicio y Citas
- 10. Reporte final de pruebas e incidencias
- 8. Diseño de la interfaz de usuario
- 9. Implementación del Release v0.1.0
- 1. Información general del proyecto

## God Nodes (most connected - your core abstractions)
1. `Usuario` - 59 edges
2. `RolUsuario` - 53 edges
3. `OrdenServicio` - 37 edges
4. `Base` - 27 edges
5. `ReglaNegocioError` - 26 edges
6. `Cotizacion` - 20 edges
7. `abrir_orden()` - 19 edges
8. `NoEncontradoError` - 18 edges
9. `solicitar_codigo()` - 18 edges
10. `confirmar_codigo()` - 18 edges

## Surprising Connections (you probably didn't know these)
- `Ramas y Pull Requests` --references--> `main()`  [INFERRED]
  CONTRIBUTING.md → docs/documento/generar-docx.py
- `preparar_base()` --uses--> `Base`  [INFERRED]
  backend/app/semilla.py → backend/app/db.py
- `sesion_db()` --uses--> `Base`  [INFERRED]
  backend/tests/conftest.py → backend/app/db.py
- `regla_violada()` --uses--> `ReglaNegocioError`  [INFERRED]
  backend/app/main.py → backend/app/errores.py
- `no_encontrado()` --uses--> `NoEncontradoError`  [INFERRED]
  backend/app/main.py → backend/app/errores.py

## Import Cycles
- None detected.

## Communities (22 total, 1 thin omitted)

### Community 0 - "conftest.py"
Cohesion: 0.06
Nodes (29): crear_motor(), get_db(), Cliente, ClienteParticular, Flotilla, TipoVehiculo, Vehiculo, buscar_clientes() (+21 more)

### Community 1 - "RolUsuario"
Cohesion: 0.08
Nodes (44): Autorizacion, RolUsuario, huella(), verificar_huella(), codigo_cliente(), encabezado(), enlace_cliente(), flujo() (+36 more)

### Community 2 - "Acuerdos de trabajo · Equipo B"
Cohesion: 0.13
Nodes (12): Acuerdos de trabajo · Equipo B, Commits, Comunicación, Código, Datos personales, Decisiones, Documentos, Incumplimiento (+4 more)

### Community 3 - "Usuario"
Cohesion: 0.10
Nodes (31): Usuario, agenda(), historial_vehiculo(), listar_usuarios(), yo(), detalle_orden(), resumen_orden(), abrir_orden() (+23 more)

### Community 4 - "models.py"
Cohesion: 0.08
Nodes (34): NoEncontradoError, ReglaNegocioError, Cotizacion, DetalleCotizacion, EstadoAutorizacion, EstadoOrden, MedioAutorizacion, TokenAcceso (+26 more)

### Community 5 - "with"
Cohesion: 0.05
Nodes (42): run, name, runs-on, steps, PGPASSWORD, POSTGRES_DB, POSTGRES_PASSWORD, name (+34 more)

### Community 6 - "main.py"
Cohesion: 0.19
Nodes (5): ciclo_de_vida(), no_encontrado(), regla_violada(), salud(), preparar_base()

### Community 7 - "schemas.py"
Cohesion: 0.08
Nodes (42): EstadoCotizacion, TipoConcepto, agregar_vehiculo(), cancelar_cita(), confirmar_cita(), crear_usuario(), login(), solicitar_cita() (+34 more)

### Community 8 - "ordenes.py"
Cohesion: 0.12
Nodes (28): Base, AsignacionColaborador, Bahia, Canal, ChecklistInspeccion, Cita, Diagnostico, EstadoBahia (+20 more)

### Community 9 - "4. Especificación de requisitos de software (SRS)"
Cohesion: 0.12
Nodes (16): 4.10 Prototipos de baja fidelidad, 4.11 Validación de requisitos con el cliente, 4.1 Propósito, alcance y audiencia del SRS, 4.2 Glosario del dominio, 4.3.1 Usuarios y sus características, 4.3.2 Restricciones, supuestos y dependencias, 4.3 Descripción general, 4.4 Requisitos funcionales (+8 more)

### Community 10 - "cobro.py"
Cohesion: 0.11
Nodes (13): Garantia, Pago, Mensaje, ultimo_mensaje(), ahora(), hoy(), utc(), autorizar_credito() (+5 more)

### Community 12 - "IS1-Fase1-EquipoB-v1.1_5717b748.md"
Cohesion: 0.18
Nodes (10): 11. Paquete de transferencia a la Fase 2, 12.1 Retrospectiva del proyecto, 12.2 Contribución individual, 12. Retrospectiva del proyecto y contribución individual, 13. Referencias, 5.1 Plan de pruebas, 5.2 Casos de prueba de aceptación, 5.3 Matriz de trazabilidad (+2 more)

### Community 13 - "7. Arquitectura y diseño"
Cohesion: 0.20
Nodes (10): 7.1 Estilo arquitectónico, 7.2 Diagramas C4, 7.3 Registros de decisiones de arquitectura (ADR), 7.4 Diagramas de artefactos y de despliegue, 7.5 Diagrama de paquetes, 7.6 Diagramas de clases de la solución, 7.7 Diagramas de secuencia, 7.8 Diagrama de comunicación (+2 more)

### Community 14 - "2. Gestión del proyecto con Scrum"
Cohesion: 0.25
Nodes (8): 2.1 Acuerdos de trabajo, 2.2 Definición de Listo (DoR) y Definición de Terminado (DoD), 2.3 Resumen de sprints, 2.4 Registro de riesgos, 2.5 Solicitudes de cambio, 2.6 Declaración de uso de inteligencia artificial, 2. Gestión del proyecto con Scrum, Evidencia de los eventos

### Community 15 - "3. Visión y viabilidad del producto"
Cohesion: 0.29
Nodes (7): 3.1 Problema y contexto del cliente, 3.2 Objetivos del producto e indicadores, 3.3 Alcance, 3.4 Stakeholders, 3.5 Proceso actual (as-is), 3.6 Estudio de viabilidad, 3. Visión y viabilidad del producto

### Community 16 - "6. Modelos de análisis"
Cohesion: 0.29
Nodes (7): 6.1 Diagramas de flujo de datos, 6.2 Modelo de datos, 6.3 Diagrama de clases del dominio, 6.4 Diagrama de objetos, 6.5 Diagramas de estados, 6.6 Diagramas de actividades (to-be), 6. Modelos de análisis

### Community 17 - "Sistema de Órdenes de Servicio y Citas"
Cohesion: 0.29
Nodes (6): Base de datos (PostgreSQL), Compilar el documento, Contenido del repositorio, Ejecutar el backend, Equipo, Sistema de Órdenes de Servicio y Citas

### Community 18 - "10. Reporte final de pruebas e incidencias"
Cohesion: 0.40
Nodes (5): 10.1 Resultado de los casos de prueba, 10.2 Incidencias, 10.3 Defectos conocidos que pasan a la Fase 2, 10.4 QA cruzado realizado al otro equipo, 10. Reporte final de pruebas e incidencias

### Community 19 - "8. Diseño de la interfaz de usuario"
Cohesion: 0.40
Nodes (5): 8.1 Prototipo de alta fidelidad, 8.2 Accesibilidad, 8.3 Evaluación heurística recibida, 8.4 Prueba con usuarios y SUS, 8. Diseño de la interfaz de usuario

### Community 20 - "9. Implementación del Release v0.1.0"
Cohesion: 0.40
Nodes (5): 9.1 Pila tecnológica, 9.2 Instrucciones de instalación y ejecución, 9.3 Integración continua y flujo de trabajo, 9.4 Evidencia del flujo núcleo, 9. Implementación del Release v0.1.0

### Community 21 - "1. Información general del proyecto"
Cohesion: 0.50
Nodes (4): 1.1 Integrantes y roles, 1.2 Enlaces del proyecto, 1.3 Resumen ejecutivo, 1. Información general del proyecto

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `RolUsuario` connect `RolUsuario` to `conftest.py`, `Usuario`, `schemas.py`, `ordenes.py`, `cobro.py`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 47 inferred relationships involving `Usuario` (e.g. with `agenda()` and `agregar_vehiculo()`) actually correct?**
  _`Usuario` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06416275430359937 - nodes in this community are weakly interconnected._
- **Why does `Usuario` connect `Usuario` to `conftest.py`, `models.py`, `schemas.py`, `ordenes.py`, `cobro.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `RolUsuario` (e.g. with `listar_usuarios()` and `Sesion`) actually correct?**
  _`RolUsuario` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `RolUsuario` be split into smaller, more focused modules?**
  _Cohesion score 0.08033362598770852 - nodes in this community are weakly interconnected._
- **Are the 28 inferred relationships involving `OrdenServicio` (e.g. with `historial_vehiculo()` and `detalle_orden()`) actually correct?**
  _`OrdenServicio` has 28 INFERRED edges - model-reasoned connections that need verification._