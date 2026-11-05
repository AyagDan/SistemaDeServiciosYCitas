# subirGithub · Cómo subir el trabajo de cada rol

Esta carpeta tiene una guía de comandos **para copiar y pegar** por cada rol de Scrum. Cada guía sube los
cambios de ese rol al repositorio del equipo:

https://github.com/AyagDan/SistemaDeServiciosYCitas

| Rol | Rama | Guía |
|---|---|---|
| Product Owner | `rol/product-owner` | [`product-owner/COMANDOS.md`](product-owner/COMANDOS.md) |
| Scrum Master | `rol/scrum-master` | [`scrum-master/COMANDOS.md`](scrum-master/COMANDOS.md) |
| QA Lead | `rol/qa-lead` | [`qa-lead/COMANDOS.md`](qa-lead/COMANDOS.md) |
| Developers | `rol/developers` | [`developers/COMANDOS.md`](developers/COMANDOS.md) |

## Cómo funciona

1. Cada rol trabaja en **su propia rama** (`rol/...`) y solo sube **sus archivos** (cada guía lista cuáles).
2. Sube su rama a GitHub y abre un **Pull Request** hacia `main`.
3. **Otro integrante** revisa el Pull Request y hace el merge cuando la CI esté en verde.

Nadie sube directo a `main`.

## Requisitos (una vez por persona)

- [Git](https://git-scm.com/downloads) y [GitHub CLI (`gh`)](https://cli.github.com/) instalados.
- Una cuenta de GitHub con acceso al repositorio.
- Opcional, para compilar el documento: MiKTeX o TeX Live (`pdflatex`). Para las pruebas: Python 3.12+.

## Paso 0 · Una sola vez, lo hace quien tiene el trabajo completo (Abdías)

Hoy el repositorio del equipo solo tiene `main` y las ramas personales `rama/NOMBRE`; las ramas por rol todavía
**no existen ahí**, y `main` del repositorio va atrasado respecto al trabajo local. Desde la carpeta del proyecto
que tiene todas las ramas, ejecuta:

```bash
git fetch origin
git push origin rol/product-owner rol/scrum-master rol/qa-lead rol/developers
```

Después de esto cada rol ya puede seguir su guía. Los cambios llegan a `main` cuando se integran los Pull Requests
de cada rama.

## Reglas rápidas

- Commits con el formato **`Rol: mensaje`**, en español y en presente (ver `CONTRIBUTING.md`).
- Nunca subas contraseñas, el archivo `.env`, ni datos personales reales de clientes (LFPDPPP). El `.env` ya está
  ignorado por Git.
- Antes de abrir el PR, revisa con `git status` que solo estén tus archivos.
- Si tus cambios incluyen texto o código generado con IA, declara su uso en la sección 2.6 del documento.
