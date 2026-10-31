# Metodología de aprendizaje

Este repositorio documenta un aprendizaje guiado que va **desde cero en Python**
hasta los patrones de arquitectura del libro
*Architecture Patterns with Python* (Harry Percival y Bob Gregory, O'Reilly, 2020),
también conocido como **Cosmic Python**.

La fuente está en [`docs/fuente/`](docs/fuente/):

- `Architecture-Patterns-with-Python.md` — **fuente citable** (texto del libro).
- `Architecture-Patterns-with-Python.pdf` — versión PDF generada a partir del `.md`.

> El libro y su versión online se distribuyen bajo licencia
> **Creative Commons CC BY-NC-ND**. Cita de la fuente:
> *"The code (and the online version of the book) is licensed under a Creative
> Commons CC BY-NC-ND license, which means you are free to copy and share it with
> anyone you like, for non-commercial purposes, as long as you give attribution."*
> (Preface → License)

## Las 9 reglas

Toda lección y toda respuesta deben cumplir estas reglas:

1. **Justificar el código desde la fuente.** Cada pieza de código propuesta debe
   ser resultado de aplicar lo que la fuente enseña, y hay que explicar y
   justificar por qué se escribe así.
2. **Empezar por lo básico y escalar por dolor/necesidad.** Se arranca con lo
   más simple y solo se añade complejidad (una capa, un patrón) cuando aparece
   un *dolor* o una *necesidad* concreta — y esa decisión se justifica citando
   de dónde sale en la fuente.
3. **Formato de pasos enumerados.** Toda explicación se da en pasos numerados.
4. **FastAPI en lugar de Flask.** Donde el libro usa Flask, aquí usamos
   **FastAPI** (el libro mismo dice que el framework es un detalle de
   implementación menor; ver regla 1 para justificar cada adaptación).
5. **Primero Python.** Antes de la arquitectura se enseña Python desde cero.
6. **Citar la fuente en cada respuesta.** Cada respuesta incluye el fragmento de
   texto exacto de la fuente que se usó (con referencia al capítulo/sección).
7. **Mostrar siempre el árbol de archivos.** Cada paso muestra el árbol de
   archivos actualizado.
8. **UV para dependencias.** Las dependencias se gestionan e instalan con
   [`uv`](https://docs.astral.sh/uv/).
9. **Explicar cada diagrama Mermaid.** Todo diagrama se escribe en Mermaid y se
   explica en prosa.

## Por qué "empezar por el dolor"

Esta metodología refleja el propio método del libro. Cita de la fuente:

> *"We structure our explorations of architectural patterns around an example
> app, building it up chapter by chapter."* (Preface → Who Should Read This Book)

y

> *"as project size grows, the most obvious way of doing things isn't always the
> way that helps you manage complexity and evolving requirements."*
> (Preface → Why Python?)

Es decir: no introducimos un patrón porque sí, sino cuando el crecimiento del
proyecto hace que "la forma obvia" empiece a doler.

## Mapa del aprendizaje (orden previsto)

0. **Python desde cero** (regla 5) — fundamentos antes de tocar arquitectura.
1. **Domain Modeling / DDD** (cap. 1)
2. **Repository Pattern** (cap. 2)
3. **Coupling & Abstractions** (cap. 3)
4. **Service Layer + API** con **FastAPI** (cap. 4) — *FastAPI en vez de Flask*.
5. **TDD en marchas alta y baja** (cap. 5)
6. **Unit of Work** (cap. 6)
7. **Aggregates & Consistency** (cap. 7)
8. **Events & Message Bus** (cap. 8) → arquitectura dirigida por eventos (caps. 9–13)

Cada lección vive en `lecciones/NN-nombre/` con su código, sus pruebas y su
explicación en pasos.
