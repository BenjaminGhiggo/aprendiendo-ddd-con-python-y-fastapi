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
- **Comprobación (las 4):** ejercicios prácticos + pytest + preguntas de recuerdo
  + un mini-proyecto único que crece (el "allocation" del libro).

## Las 9 reglas de formato

1. Justifica cada línea de código desde la fuente.
2. Empieza por lo básico; añade complejidad solo con dolor/necesidad, justificado desde la fuente.
3. Explica en pasos numerados.
4. Usa **FastAPI**, no Flask.
5. Enseña Python primero.
6. Cita el fragmento exacto de la fuente en cada respuesta.
7. Muestra el árbol de archivos en cada paso.
8. Instala dependencias con **uv**.
9. Dibuja diagramas en Mermaid y explícalos.

## Estructura fija de cada lección (`lecciones/NN-nombre/`)

1. Objetivo (1 concepto) · 2. Cita de la fuente · 3. El dolor/necesidad ·
4. Explicación paso a paso · 5. Diagrama Mermaid + explicación · 6. Árbol de archivos ·
7. Tu turno (huecos/ejercicio) · 8. Prueba pytest · 9. Preguntas de recuerdo.

Fuente citable: `docs/fuente/Architecture-Patterns-with-Python.md`.
