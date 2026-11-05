# Product Owner · Cómo subir tus cambios a GitHub

Repositorio: https://github.com/AyagDan/SistemaDeServiciosYCitas
Tu rama: `rol/product-owner`
Tus archivos: Información general (1), visión y viabilidad (3), SRS con backlog, historias y casos de uso (4), propuesta de solución y fuentes de los diagramas de visión.

> Copia cada bloque, pégalo en **PowerShell** o **Git Bash** y pulsa Enter. Hazlos en orden.
> Si un comando muestra un error en rojo, **detente** y ve a «Si algo falla» al final.

## Solo la primera vez

### 1. Entra a GitHub y baja el proyecto

Inicia sesión (se abre el navegador; elige GitHub.com y HTTPS):

```bash
gh auth login
```

Baja el proyecto y entra a la carpeta:

```bash
git clone https://github.com/AyagDan/SistemaDeServiciosYCitas.git
cd SistemaDeServiciosYCitas
```

Dile a Git quién eres (cambia el nombre y el correo por los tuyos, los de tu cuenta de GitHub):

```bash
git config user.name "Tu Nombre"
git config user.email "tu-correo@ejemplo.com"
```

> Si ya tienes el proyecto clonado, solo entra a su carpeta (`cd SistemaDeServiciosYCitas`) y salta al paso siguiente.

## Cada vez que quieras subir tus cambios

### 2. Ponte en tu rama y tráela al día

```bash
git fetch origin
git checkout rol/product-owner
git pull origin rol/product-owner
git merge origin/main --no-edit
```

> Hazlo dentro de la carpeta `SistemaDeServiciosYCitas` (si abriste una terminal nueva, primero entra con `cd SistemaDeServiciosYCitas`).
> `git merge origin/main` trae lo que otros roles ya integraron. Si dice «Already up to date», perfecto.
> Si dice `CONFLICT`, ve a «Si algo falla».

### 3. Haz tus cambios

Edita tus archivos como siempre. Cuando termines, mira qué cambió:

```bash
git status
```

### 4. Si tocaste archivos `.tex`, compila el documento (recomendado)

Corre el comando dos veces y revisa que no haya errores:

```bash
cd docs/documento
pdflatex -interaction=nonstopmode IS1-Fase1-EquipoB.tex
pdflatex -interaction=nonstopmode IS1-Fase1-EquipoB.tex
cd ../..
```

### 5. Prepara solo los archivos de tu rol

```bash
git add docs/documento/secciones/01-informacion-general.tex docs/documento/secciones/03-vision-viabilidad.tex docs/documento/secciones/04-srs.tex docs/03-vision docs/propuesta
```

Si agregas imágenes o fuentes de wireframes y casos de uso en `docs/04-requisitos/`, súbelas con una línea aparte: `git add docs/04-requisitos`.

Comprueba que **solo aparezcan archivos tuyos** (ni contraseñas, ni `.env`, ni datos reales de clientes):

```bash
git status
git diff --cached --name-only
```

Si aparece un archivo que no debe subirse: `git restore --staged ruta/del/archivo`.

### 6. Guarda los cambios (commit)

El mensaje empieza con `Product Owner:` y explica en una frase qué hiciste. Ejemplo:

```bash
git commit -m "Product Owner: agrega la historia HU-27 al backlog (sección 4.5)"
```

Cambia el texto entre comillas por el tuyo, pero **conserva el prefijo `Product Owner:`**.

### 7. Sube tu rama

```bash
git push -u origin rol/product-owner
```

### 8. Abre el Pull Request

```bash
gh pr create --base main --head rol/product-owner --title "Product Owner: resumen de tus cambios" --body "Qué cambió y por qué. Secciones o historias relacionadas."
```

Si no tienes `gh`, abre este enlace en el navegador y pulsa **Create pull request**:

https://github.com/AyagDan/SistemaDeServiciosYCitas/compare/main...rol/product-owner?expand=1

Si el Pull Request ya existía, `git push` ya lo actualizó: no hace falta crear otro.

**Después:** otro integrante debe revisar el Pull Request y hacer el merge (nunca tu propio PR). La CI debe estar en verde.

## Si algo falla

| Mensaje | Qué hacer |
|---|---|
| `CONFLICT (content): Merge conflict in archivo` | Abre ese archivo, busca `<<<<<<<` y `>>>>>>>`, deja el texto correcto y borra esas marcas. Luego: `git add archivo` y `git commit -m "Product Owner: resuelve conflicto con main"`. |
| `error: pathspec '...' did not match any file(s)` | Alguna ruta de `git add` no existe en tu copia. Quítala del comando y repite. |
| `nothing to commit, working tree clean` | No hay cambios nuevos que guardar; no hace falta subir nada. |
| `rejected ... non-fast-forward` | Alguien subió a tu rama antes. Corre `git pull origin rol/product-owner` y luego otra vez `git push -u origin rol/product-owner`. |
| `Permission denied` o `403` | Tu cuenta no tiene acceso. Pide a Abdías que te agregue como colaborador del repositorio, o corre `gh auth login` con la cuenta correcta. |
| `couldn't find remote ref rol/product-owner` | La rama aún no está en GitHub. Pide a Abdías que haga el «Paso 0» del `LEEME.md` de `subirGithub/`. |
| `Your local changes ... would be overwritten by merge` | Tienes cambios sin guardar. Guárdalos con los pasos 5 y 6 y luego repite el paso 2. |
