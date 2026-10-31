# Metodología de aprendizaje

Este repositorio documenta un aprendizaje guiado que va **desde cero absoluto en
Python** hasta los patrones de arquitectura del libro
*Architecture Patterns with Python* (Harry Percival y Bob Gregory, O'Reilly, 2020),
también conocido como **Cosmic Python**.

La fuente está en [`docs/fuente/`](docs/fuente/):

- `Architecture-Patterns-with-Python.md` — **fuente citable** (texto del libro).
- `Architecture-Patterns-with-Python.pdf` — PDF original del libro (497 págs).

> El libro y su versión online se distribuyen bajo licencia
> **Creative Commons CC BY-NC-ND**:
> *"The code (and the online version of the book) is licensed under a Creative
> Commons CC BY-NC-ND license ... as long as you give attribution."*
> (Preface → License)

---

## 1. Perfil del aprendiz

- **Cero absoluto en programación.** No se asume nada: ni qué es una variable, ni
  qué significa "ejecutar" un programa, ni cómo se instala Python.
- Idioma de trabajo: **español**.

---

## 2. Las 9 reglas de formato

Toda lección y toda respuesta deben cumplir estas reglas (son el "cómo se ve"
cada respuesta):

1. **Justificar el código desde la fuente.** Cada pieza de código es resultado de
   aplicar lo que la fuente enseña; se explica y justifica por qué se escribe así.
2. **Empezar por lo básico y escalar por dolor/necesidad.** Solo se añade
   complejidad (una capa, un patrón) cuando aparece un *dolor* o *necesidad*
   concreta, y esa decisión se justifica citando la fuente.
3. **Formato de pasos enumerados.** Toda explicación va en pasos numerados.
4. **FastAPI en lugar de Flask.** Donde el libro usa Flask, aquí usamos FastAPI.
5. **Primero Python.** Antes de la arquitectura se enseña Python desde cero.
6. **Citar la fuente en cada respuesta.** Siempre el fragmento exacto usado, con
   su capítulo/sección.
7. **Mostrar siempre el árbol de archivos.**
8. **UV para dependencias.** Se usa [`uv`](https://docs.astral.sh/uv/).
9. **Explicar cada diagrama Mermaid.**

---

## 3. Cómo se aprende (el "cómo" pedagógico)

Estas cuatro decisiones definen la experiencia. Cada una está respaldada por la
fuente.

### 3.1 Ritmo: micro-pasos

- Lecciones **muy cortas y frecuentes**: **un solo concepto nuevo por lección**.
- Avance lento y seguro; antes de un concepto nuevo, el anterior ya se practicó.

### 3.2 Tu rol: pair programming con huecos

- Yo (el asistente) escribo la **base del código** y la explico.
- Dejo **huecos marcados** (`# TODO: ...`) para que **tú escribas las partes
  clave**; luego comparo tu solución con la de referencia.
- Justificación (fuente):
  > *"we outline an 'Exercise for the Reader,' and point you to a GitHub location
  > where you can download some partially finished code for the chapter with a few
  > missing parts to write yourself."* (Preface → Example Code and Coding Along)
  > *"We learned most of what we know from pairing with people, writing code with
  > them, and learning by doing."* (íd.)

### 3.3 El código: los tests primero

- Cuando entremos en lógica no trivial, **primero se escribe la prueba `pytest`**
  y después la implementación que la hace pasar.
- Justificación (fuente):
  > *"We use TDD at work, so we tend to show listings of tests first, followed by
  > implementation."* (Preface → Who Should Read This Book)

### 3.4 Comprobación del aprendizaje (las 4 juntas)

Cada lección cierra comprobando que el concepto quedó, con las cuatro vías:

1. **Ejercicios prácticos** — retos de código que resuelves tú (los "huecos").
2. **Pruebas automáticas (`pytest`)** — tu código debe pasar los tests; es el
   semáforo objetivo de "funciona".
3. **Preguntas de recuerdo** — al final explicas el concepto con tus palabras,
   sin mirar.
4. **Mini-proyecto que crece** — todo se integra en **un único proyecto que
   evoluciona** lección a lección.

---

## 4. El mini-proyecto que crece

- **Fase Python (lecciones 00–0x):** como partimos de cero, se usan ejemplos
  mínimos para aprender el lenguaje.
- **Fase arquitectura (desde Domain Modeling):** adoptamos el **proyecto único
  del libro** — un sistema de **asignación de pedidos a lotes de stock
  (allocation)** — y lo construimos capítulo a capítulo.
- Justificación (fuente):
  > *"we've structured the book around a single example project ... We'll build
  > up this project as the chapters progress, as if you've paired with us."*
  > (Preface → Example Code and Coding Along)

---

## 5. Estructura fija de cada lección

Cada lección vive en `lecciones/NN-nombre/` y sigue siempre este guion
(en pasos numerados, regla 3):

1. **Objetivo** — el único concepto nuevo de esta micro-lección.
2. **Cita de la fuente** — el fragmento que motiva o respalda el concepto.
3. **El dolor/necesidad** — por qué hace falta esto ahora (regla 2).
4. **Explicación paso a paso** — con el código base ya escrito y comentado.
5. **Diagrama Mermaid** (cuando aporte) + su explicación en prosa (regla 9).
6. **Árbol de archivos** actualizado (regla 7).
7. **Tu turno (huecos / ejercicio)** — las partes que escribes tú.
8. **Prueba `pytest`** — el test que tu código debe pasar.
9. **Preguntas de recuerdo** — para cerrar.

---

## 6. Herramientas

- **Python 3.12+**
- **uv** para entorno y dependencias (regla 8)
- **pytest** para las pruebas
- **FastAPI** para la capa web (regla 4)

---

## 7. Mapa del aprendizaje (orden previsto)

**Fase 0 — Python desde cero** (regla 5): ejecutar código, variables, tipos,
condicionales, bucles, funciones, estructuras de datos, clases/objetos,
excepciones, módulos, entorno con `uv`, y primer `pytest`.

**Fase 1 — Arquitectura (Cosmic Python):**

1. Domain Modeling / DDD (cap. 1)
2. Repository Pattern (cap. 2)
3. Coupling & Abstractions (cap. 3)
4. Service Layer + API con **FastAPI** (cap. 4)
5. TDD en marchas alta y baja (cap. 5)
6. Unit of Work (cap. 6)
7. Aggregates & Consistency (cap. 7)
8. Events & Message Bus y arquitectura dirigida por eventos (caps. 8–13)
