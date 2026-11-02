# Instrucciones del repositorio

Este repo es un **aprendizaje guiado** de Python → DDD/arquitectura, basado en el
libro *Architecture Patterns with Python* (Cosmic Python).

**Antes de responder cualquier cosa en este repo, sigue [`METODOLOGIA.md`](METODOLOGIA.md).**

## Perfil del aprendiz

- **Cero absoluto en programación.** No asumir nada previo. En español.

## Cómo se enseña

- **Ritmo: micro-pasos** — un solo concepto nuevo por lección.
- **Rol: pair programming** — yo escribo la base y dejo huecos `# TODO:` para que
  el aprendiz escriba las partes clave; luego comparo con la referencia.
- **Tests primero** cuando haya lógica no trivial (pytest antes que implementación).
- **Dirigido por preguntas** — cada lección nace de "tengo W, me piden X, ¿qué hago?".
- **No recortar pasos** — clase→instancia→objeto→uso, cada uno visible.
- **Lo simple antes que lo avanzado** — forma explícita; lo idiomático solo con dolor.
- **Comprobación (las 4):** ejercicios + pytest + preguntas de recuerdo + mini-proyecto
  único que crece (el "allocation" del libro).

## Las 9 reglas de formato

1. Justifica cada línea de código desde la fuente.
2. Empieza por lo básico; añade complejidad solo con dolor/necesidad, justificado desde la fuente.
3. Explica en pasos numerados.
4. Usa **FastAPI**, no Flask.
5. Enseña Python primero.
6. Cita el fragmento exacto de la fuente en cada respuesta.
7. Muestra el árbol de archivos en cada paso.
8. Instala dependencias con **uv**.
9. Diagramas en Mermaid y explicados.

## Figuras y diagramas

- **Las figuras del libro NO se omiten** (§3.8): se rescatan del PDF a
  `docs/fuente/imagenes/fig-N-M.png`, se muestran y se explican.
- **Los diagramas se entregan como CÓDIGO Mermaid** (§3.9), NO renderizados a
  imagen. El aprendiz los pega en un previsualizador. Deben **reproducir fielmente
  las figuras del libro**.

## Herramientas y Git

- **Python 3.12 exacto** (`.python-version` = 3.12; `requires-python = ">=3.12,<3.13"`).
  Nunca 3.13 ni otra versión.
- **uv** para entorno y dependencias.
- **Git para todo:** rama de integración `ccr-b56bf27c-qa5zqh`; una rama por
  lección (`leccion-NN-nombre`) o ajuste (`config/...`, `chore/...`); commits
  pequeños; merge a integración al terminar. Git también se explica como aprendizaje.
- **Escala:** ejercicios pequeños en carpetas `solucion_mala/` y `solucion_buena/`
  (comparar con `git diff --no-index`); el proyecto de la Fase 1 es un único código
  que evoluciona por commits, con una rama por capítulo (`capitulo-NN-nombre`).
  Nunca Git dentro de subcarpetas.

## Dónde vive cada cosa

- **Fase 0:** lecciones autocontenidas en `lecciones/NN-nombre/`, en formato **formulario** con
  archivos numerados (`paso1_…` a `paso6_ejercicios/`). Plantilla: `lecciones/05-listas-y-diccionarios/`.
- **Guía de estudio:** `README.md` raíz (▶ EMPIEZA AQUÍ), `COMO-ESTUDIAR.md` y `lecciones/README.md`
  (orden, requisitos, tiempos). Si agregas o renombras una lección, actualiza los tres.
- **Fase 1 (el libro):** cada capítulo es autocontenido en `fase-1/capitulos/NN-nombre/`:
  `README.md` (la clase), `proyecto/` (el código al final de ese capítulo, un snapshot
  que parte del capítulo anterior) y `ejercicios/micro-paso-M/` (refuerzo por micro-paso).
  Se corre con, p. ej., `uv run pytest fase-1/capitulos/01-domain-modeling/proyecto/ -q`.

## Convenciones del proyecto `allocation` (Fase 1)

- **Tests por capítulo, nunca global.** Cada snapshot repite nombres (`test_modelo.py`, etc.),
  así que un `uv run pytest` global choca por colisión de basenames. Correr siempre la **ruta
  del capítulo** (como arriba).
- **Handlers de evento aislados.** Desde el cap. 10 el bus envuelve cada handler de evento en
  `try/except`: si uno falla, se **ignora en silencio** y no rompe el comando. Consecuencia al
  estudiar (cap. 12–13): los handlers que escriben el **modelo de lectura** usan `uow.sesion`,
  así que con la **UoW falsa** (sin `.sesion`) fallan sin ruido; el read model **solo se llena
  con la UoW real** (`test_vistas.py`). No es un bug, es la propiedad de resiliencia.
- **Bootstrap en tests (cap. 13+).** Montar el bus con `bootstrap(iniciar_orm=False, ...)`
  porque el `conftest.py` ya arranca el ORM; `True` en un test ya mapeado da "mappers duplicados".

## Estructura fija de cada lección (`lecciones/NN-nombre/`) — formato formulario

Detalle completo en `METODOLOGIA.md` §5. Resumen:

- **Arriba:** "Orden de estudio: N de 18", navegación ⬅️🏠➡️ (también abajo) y **Ruta de estudio**.
- **Secciones con numeración FIJA:** §0 pregunta (W→X) · §1 objetivos · §2 cita de la fuente ·
  §3 dolor · §4 teoría (recuadros, vocabulario, regla de oro) · §5–§6 tablas de fórmulas ·
  §7 propiedades · §8 errores frecuentes (mensaje real) · §9 4 ejemplos resueltos · §10 12
  problemas (4🟢 4🟡 4🔴) · §11 claves plegadas · §12 mapa/figura Mermaid · §13 árbol ·
  §14 tu turno + comprobación · §15 preguntas de recuerdo con respuesta · §16 semáforo 🚦.
- **Archivos en orden de estudio:** `README.md` (paso 0) · `paso1_formulas.py` ·
  `paso2_ejemplos_resueltos.py` · `paso3_tu_turno.py` (`# TODO`) · `paso4_tu_turno_solucion.py` ·
  `test_paso3_tu_turno.py` (desde la 08) · `paso5_solucionario/` · `paso6_ejercicios/`.
  Prefijo `pasoN_` (no `N_`) para que sean importables.
- **pytest una lección a la vez** (`uv run pytest lecciones/NN-nombre -q`): desde la 08 todas repiten
  `paso3_tu_turno.py` / `test_paso3_tu_turno.py`, y juntar dos lecciones da *import file mismatch*.
  Los tests de `paso3` están en **rojo a propósito** hasta que el aprendiz complete los `# TODO`.
- **Verificar siempre:** todo `.py` corre, tablas/claves salen de la salida real, Mermaid
  renderiza, citas existen en la fuente.
- **Progreso:** `progreso/fase-0-python.md` separa *"Mi avance"* (lo marca el aprendiz) de
  *"Material construido"* (lo mantiene el asistente).

El avance se registra en la carpeta `progreso/` (índice en `progreso/README.md`
y un archivo por capítulo con secciones y figuras).
Fuente citable: `docs/fuente/Architecture-Patterns-with-Python.md`.
