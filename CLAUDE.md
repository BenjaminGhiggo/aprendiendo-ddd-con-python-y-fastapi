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

## Estructura fija de cada lección (`lecciones/NN-nombre/`)

0. La pregunta (W→X) · 1. Objetivo · 2. Cita de la fuente · 3. El dolor/necesidad ·
4. Explicación paso a paso (sin recortar) · 5. Figura del libro + diagrama Mermaid (código) ·
6. Árbol de archivos · 7. Tu turno (huecos) · 8. Prueba pytest · 9. Preguntas de recuerdo.

El avance se registra en la carpeta `progreso/` (índice en `progreso/README.md`
y un archivo por capítulo con secciones y figuras).
Fuente citable: `docs/fuente/Architecture-Patterns-with-Python.md`.
