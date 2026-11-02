# Herramientas locales: sitio de estudio y API

🏠 [Volver al inicio](../README.md)

Dos herramientas opcionales que corren **en tu computadora** (no hace falta ningún servidor
externo). Siempre desde la raíz del repo.

## 1. Sitio de estudio navegable (MkDocs)

Convierte todas las lecciones y capítulos en un sitio web con **menú en orden de estudio**,
**buscador**, **diagramas Mermaid dibujados**, **claves plegables** y cada `.py` como página
con su código resaltado. No modifica ningún archivo del repo: trabaja sobre una copia en `build/`.

```bash
uv sync --group docs                                              # una vez: instala MkDocs
uv run --group docs python despliegue/sitio/construir_sitio.py    # prepara build/
uv run --group docs mkdocs serve -f build/mkdocs.yml              # abre http://127.0.0.1:8000
```
> Si cambias un README, vuelve a correr `construir_sitio.py` para ver el cambio.

Para generar el sitio como archivos HTML (carpeta `site/`):
```bash
uv run --group docs mkdocs build -f build/mkdocs.yml
```

## 2. API del proyecto *allocation* (Capítulo 13)

Levanta la API del capítulo 13 **sin modificar su código**: la conecta a un SQLite con el
`bootstrap` del capítulo, agrega `POST /lotes` (el `add_batch` del libro) y carga datos de ejemplo.

```bash
uv run uvicorn main:app --app-dir despliegue/api --reload         # abre http://127.0.0.1:8000/docs
```

Prueba en orden desde `/docs`:
1. `GET /asignaciones/pedido-demo` → ya existe (datos de ejemplo).
2. `POST /lotes` → crea stock nuevo.
3. `POST /asignar` → responde `202 {"ok": true}` (CQS: escribir no devuelve datos).
4. `GET /asignaciones/{id_pedido}` → lee el modelo de lectura (CQRS).

Si pides más stock del que hay, verás en la terminal el aviso del handler de eventos:
`[EMAIL] para stock@ejemplo.com: Sin stock para ...`.

> La base es `/tmp/allocation.db`; bórrala para empezar de cero. Para usar otra base, define
> la variable `DATABASE_URL` (por ejemplo, una URL de Postgres).

> Las dos herramientas usan el puerto 8000: córrelas de a una, o agrega `--port 8001` a una.
