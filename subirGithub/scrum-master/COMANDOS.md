# Scrum Master · Cómo subir tus cambios a GitHub

Repositorio: https://github.com/AyagDan/SistemaDeServiciosYCitas
Tu rama: `rol/scrum-master`
Tus archivos: Portada y cómo usar el machote (0), gestión Scrum (2), transferencia (11), retrospectiva (12), anexos (14), lista de verificación (15), preámbulo LaTeX, README, CONTRIBUTING, Avances.txt, PDF de entregas, grafo del proyecto y esta carpeta `subirGithub/`.

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
git checkout rol/scrum-master
git pull origin rol/scrum-master
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
git add docs/documento/secciones/00-como-usar.tex docs/documento/secciones/00-portada.tex docs/documento/secciones/02-gestion-scrum.tex docs/documento/secciones/11-transferencia.tex docs/documento/secciones/12-retrospectiva.tex docs/documento/secciones/14-anexos.tex docs/documento/secciones/15-lista-verificacion.tex docs/documento/preambulo.tex docs/documento/IS1-Fase1-EquipoB.tex docs/entregas README.md CONTRIBUTING.md Avances.txt .gitignore graphify-out subirGithub
```

Si cambiaste código y quieres actualizar el grafo antes de subir: `graphify update .`

Comprueba que **solo aparezcan archivos tuyos** (ni contraseñas, ni `.env`, ni datos reales de clientes):

```bash
git status
git diff --cached --name-only
```

Si aparece un archivo que no debe subirse: `git restore --staged ruta/del/archivo`.

### 6. Guarda los cambios (commit)

El mensaje empieza con `Scrum Master:` y explica en una frase qué hiciste. Ejemplo:

```bash
git commit -m "Scrum Master: registra el Sprint 2 en el resumen de sprints (sección 2.3)"
```

Cambia el texto entre comillas por el tuyo, pero **conserva el prefijo `Scrum Master:`**.

### 7. Sube tu rama

```bash
git push -u origin rol/scrum-master
```

### 8. Abre el Pull Request

```bash
gh pr create --base main --head rol/scrum-master --title "Scrum Master: resumen de tus cambios" --body "Qué cambió y por qué. Secciones o historias relacionadas."
```

Si no tienes `gh`, abre este enlace en el navegador y pulsa **Create pull request**:

https://github.com/AyagDan/SistemaDeServiciosYCitas/compare/main...rol/scrum-master?expand=1

Si el Pull Request ya existía, `git push` ya lo actualizó: no hace falta crear otro.

**Después:** otro integrante debe revisar el Pull Request y hacer el merge (nunca tu propio PR). La CI debe estar en verde.

## Si algo falla

| Mensaje | Qué hacer |
|---|---|
| `CONFLICT (content): Merge conflict in archivo` | Abre ese archivo, busca `<<<<<<<` y `>>>>>>>`, deja el texto correcto y borra esas marcas. Luego: `git add archivo` y `git commit -m "Scrum Master: resuelve conflicto con main"`. |
| `error: pathspec '...' did not match any file(s)` | Alguna ruta de `git add` no existe en tu copia. Quítala del comando y repite. |
| `nothing to commit, working tree clean` | No hay cambios nuevos que guardar; no hace falta subir nada. |
| `rejected ... non-fast-forward` | Alguien subió a tu rama antes. Corre `git pull origin rol/scrum-master` y luego otra vez `git push -u origin rol/scrum-master`. |
| `Permission denied` o `403` | Tu cuenta no tiene acceso. Pide a Abdías que te agregue como colaborador del repositorio, o corre `gh auth login` con la cuenta correcta. |
| `couldn't find remote ref rol/scrum-master` | La rama aún no está en GitHub. Pide a Abdías que haga el «Paso 0» del `LEEME.md` de `subirGithub/`. |
| `Your local changes ... would be overwritten by merge` | Tienes cambios sin guardar. Guárdalos con los pasos 5 y 6 y luego repite el paso 2. |
