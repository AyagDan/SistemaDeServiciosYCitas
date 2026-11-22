# Manual técnico · Backend del Sistema de Órdenes de Servicio y Citas

Equipo B · Ingeniería de Software I (IDSSI-27) · versión del documento v0.2.10 · 18/11/2026.

Este manual describe el backend (`backend/`) y la base de datos (`db/`). La instalación y la ejecución están en
el [README](../README.md); las reglas de negocio (RN-xx), los requisitos (RF y RNF) y las historias de usuario
están en el Documento de Ingeniería (`docs/documento/`).

## 1. Arquitectura

La aplicación es una API REST en Python con FastAPI. Se organiza en capas, y cada capa solo usa a la de abajo:

| Capa | Carpeta | Qué hace |
|---|---|---|
| Rutas | `backend/app/rutas/` | Reciben las peticiones HTTP, validan el rol del usuario y llaman a los servicios. No contienen reglas de negocio. |
| Servicios | `backend/app/servicios/` | Reglas de negocio: órdenes, cotizaciones, citas y cobro. Lanzan `ReglaNegocioError` (respuesta 409) o `NoEncontradoError` (404). |
| Modelos | `backend/app/models.py` | Tablas y enumeraciones con SQLAlchemy. |
| Base de datos | `db/schema.sql` | Esquema de PostgreSQL con sus restricciones. En SQLite las tablas se crean solas. |

Módulos de apoyo:

| Módulo | Función |
|---|---|
| `config.py` | Variables de entorno y parámetros de las reglas de negocio. |
| `db.py` | Motor de la base de datos y sesión por petición. |
| `schemas.py` | Modelos de Pydantic que validan las entradas y dan forma a las respuestas. |
| `seguridad.py` | Cifrado de contraseñas, sesiones firmadas, control de acceso por rol y token del cliente. |
| `notificaciones.py` | Envío de enlaces y códigos. En la Fase 1 se guardan en una bandeja y en la bitácora; no se envían correos reales. |
| `reloj.py` | Fuente única de la hora; las pruebas la sustituyen para comprobar vigencias. |
| `errores.py` | Excepciones de negocio. |
| `semilla.py` | Crea las 4 bahías y, con `--demo`, usuarios y clientes ficticios. |

Diagramas: el mapa de tecnologías está en `docs/07-arquitectura/tecnologias/diagrama-tecnologias.png` y el
diagrama de clases del dominio en `docs/06-analisis/clases/` (se genera a partir de `models.py`).

## 2. Estructura del código

```
backend/
├── app/
│   ├── main.py           aplicación FastAPI, manejadores de errores y ruta /salud
│   ├── rutas/            personal.py (sesión, usuarios, clientes, citas), taller.py (órdenes,
│   │                     cotizaciones, cobro, panel), portal.py (enlace seguro del cliente)
│   ├── servicios/        ordenes.py, cotizaciones.py, cobro.py, citas.py
│   └── models.py, schemas.py, seguridad.py, config.py, db.py, ...
├── tests/                42 pruebas automatizadas
├── requirements.txt      dependencias con sus versiones
└── .env.example          plantilla de configuración
```

## 3. Máquina de estados de la orden

Una orden pasa por 10 estados: `Abierta`, `EnEsperaDeBahia`, `Diagnosticada`, `Autorizada`, `EnReparacion`,
`EsperandoRefaccion`, `EsperandoAutorizacionAdicional`, `ListaParaEntrega`, `Cerrada` y `Cancelada`. Las
transiciones permitidas están en una sola tabla, `TRANSICIONES` en `backend/app/servicios/ordenes.py`; cualquier
otra se rechaza y cada cambio válido queda en `HistorialEstado` con su fecha y su responsable. El diagrama está
en la sección 6.5 del documento y su fuente en `docs/06-analisis/estados/orden-servicio.puml`.

## 4. Base de datos

`db/schema.sql` crea las 26 tablas: `usuario`, `cliente`, `cliente_particular`, `flotilla`, `vehiculo`, `bahia`,
`cita`, `orden_servicio`, `asignacion_colaborador`, `historial_estado`, `diagnostico`, `recepcion_vehicular`,
`checklist_inspeccion`, `fotografia`, `token_acceso`, `cotizacion`, `detalle_cotizacion`, `autorizacion`, `pago`,
`garantia`, `proveedor`, `refaccion`, `solicitud_refaccion`, `compra`, `detalle_compra` y `entrega_refaccion`.

El diagrama entidad-relación de las 20 tablas que usa el backend está en `docs/06-analisis/er/` y se genera a partir
de `models.py` con `python docs/06-analisis/er/generar_er.py`. Las 6 tablas de refacciones y compras son de la Fase 2.

Las reglas de integridad viven también en la base de datos: tipos enumerados para los estados, restricciones
`CHECK` (por ejemplo, una cita confirmada exige bahía y usuario que la confirma, y un crédito exige quién lo
autorizó) y un índice que impide que dos órdenes activas ocupen la misma bahía.

Para usar PostgreSQL:

```bash
createdb taller
psql -d taller -f db/schema.sql
```

Con SQLite (el valor por defecto), `app.semilla` o el arranque de la API crean las tablas. Las pruebas usan SQLite
en memoria.

## 5. Configuración

Las variables se leen del entorno o de `backend/.env` (que no se sube al repositorio; la plantilla es
`backend/.env.example`):

| Variable | Para qué sirve | Valor por defecto |
|---|---|---|
| `DATABASE_URL` | Base de datos | SQLite local (`backend/taller.db`) |
| `SECRET_KEY` | Llave que firma las sesiones del personal | Se genera al arrancar; las sesiones se invalidan al reiniciar |
| `PORTAL_URL` | URL pública del portal del cliente, para armar su enlace seguro | `http://localhost:8000/portal` |
| `SEED_PASSWORD` | Contraseña de los usuarios de demostración | Se genera y se imprime una vez |
| `MEDIA_DIR` | Carpeta de las fotografías de recepción | `backend/media` |

Parámetros de las reglas de negocio (`backend/app/config.py`): 4 bahías y 5 lugares de estacionamiento (RN-05),
cotización vigente 5 días (RN-11), código 2FA vigente 5 minutos (RN-02), umbral de re-autorización del 10 %
(RN-04), garantía de 30 días (RN-13), sesión de 8 horas y fotografías de hasta 5 MB.

## 6. API

La documentación interactiva, con los campos de cada petición, está en `/docs` (OpenAPI) cuando la API corre.
Los endpoints se agrupan así:

| Grupo | Endpoints |
|---|---|
| Sistema y autenticación | `GET /salud`, `POST /auth/login`, `GET /auth/yo` |
| Usuarios | `POST /usuarios`, `GET /usuarios` |
| Clientes y vehículos | `POST /clientes`, `GET /clientes`, `POST /clientes/{id_cliente}/vehiculos`, `GET /vehiculos/{id_vehiculo}/historial` |
| Citas | `GET /citas`, `POST /citas/solicitudes`, `POST /citas/{id_cita}/confirmar`, `POST /citas/{id_cita}/cancelar` |
| Órdenes | `POST /ordenes`, `GET /ordenes`, `GET /ordenes/{folio}`, `PUT /ordenes/{folio}/checklist`, `POST /ordenes/{folio}/fotografias`, `.../asignacion`, `.../diagnosticos`, `.../reparacion`, `.../espera-refaccion`, `.../reanudacion`, `.../terminar`, `.../cancelar` |
| Cotizaciones | `POST` y `GET /ordenes/{folio}/cotizaciones`; `PUT .../cotizaciones/{id}/seleccion`; `POST .../cotizaciones/{id}/codigo` y `.../autorizacion` |
| Cobro | `GET /ordenes/{folio}/saldo`, `POST .../pagos`, `.../credito`, `.../entrega` |
| Panel | `GET /bahias`, `GET /panel` |
| Portal del cliente | `GET /portal/{token}`, `PUT .../seleccion`, `POST .../codigo`, `.../autorizacion`, `.../rechazo` |

No hay endpoints de sincronización sin conexión (HU-25 y HU-26): quedan fuera de la versión actual.

## 7. Seguridad

- **Contraseñas:** se guardan con PBKDF2-SHA256, una sal aleatoria y 260 000 iteraciones; nunca en claro.
- **Sesiones del personal:** token firmado con HMAC-SHA256 y una vigencia de 8 horas.
- **Control de acceso por rol (OWASP A01):** cada endpoint declara qué roles lo usan con `requiere_rol(...)`. El
  Gerente no hereda permisos operativos.
- **Enlace del cliente (RN-01):** solo se guarda la huella SHA-256 del token, no el token. Expira al cerrar la
  orden con saldo cero.
- **Autorización de la cotización (RN-02, RNF-04):** código de 6 dígitos, de un solo uso y vigente 5 minutos; se
  guarda una huella SHA-256 de lo que el cliente aceptó para detectar alteraciones.
- **Datos:** el repositorio solo contiene datos ficticios y el `.env` está excluido con `.gitignore`.

## 8. Pruebas

Se ejecutan con `python -m pytest` desde `backend/`. Usan SQLite en memoria, un reloj controlable y datos ficticios
(`backend/tests/conftest.py`).

| Archivo | Pruebas | Qué cubre |
|---|---|---|
| `test_acceso.py` | 5 | Sesión, credenciales y permisos por rol, enlace del cliente |
| `test_citas_panel.py` | 5 | Citas y panel del gerente |
| `test_recepcion.py` | 9 | Recepción, checklist, fotografías, bahías y diagnóstico |
| `test_cotizacion.py` | 11 | Cotización, vigencia, 2FA y re-cotización mayor al 10 % |
| `test_cobro.py` | 5 | Pago, entrega, crédito a flotillas y garantía |
| `test_estados.py` | 7 | Máquina de estados: reparación, espera de refacción y autorización adicional |

La evidencia de la última ejecución está en `docs/pruebas/resultado-pruebas.txt`.
