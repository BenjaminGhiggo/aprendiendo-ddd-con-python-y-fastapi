# Metodología de aprendizaje

Este repositorio documenta un aprendizaje guiado que va **desde cero absoluto en
Python** hasta los patrones de arquitectura del libro
*Architecture Patterns with Python* (Harry Percival y Bob Gregory, O'Reilly, 2020),
también conocido como **Cosmic Python**.

La fuente está en [`docs/fuente/`](docs/fuente/):

- `Architecture-Patterns-with-Python.md` — **fuente citable** (texto del libro).
- `Architecture-Patterns-with-Python.pdf` — PDF original del libro (497 págs).
- `imagenes/` — **figuras rescatadas del PDF** (ver §3.8).

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

Toda lección y toda respuesta deben cumplir estas reglas (el "cómo se ve" cada
respuesta):

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
9. **Diagramas en Mermaid y explicados.** (Formato preciso en §3.9.)

---

## 3. Cómo se aprende (el "cómo" pedagógico)

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
2. **Pruebas automáticas (`pytest`)** — tu código debe pasar los tests.
3. **Preguntas de recuerdo** — explicas el concepto con tus palabras, sin mirar.
4. **Mini-proyecto que crece** — todo se integra en un único proyecto que
   evoluciona lección a lección (ver §4).

### 3.5 Aprendizaje dirigido por preguntas (requisitos que cambian)

- **Toda lección nace de una pregunta real** del tipo:
  > *"Tengo **W** (lo que ya hice). Ahora me piden **X**: una regla o funcionalidad
  > **nueva**, **modificada** o **eliminada**. ¿Qué debo hacer? ¡Estoy perdido!"*
- A partir de ese "estoy perdido" trabajamos: nombramos el dolor, decidimos el
  cambio mínimo y lo justificamos desde la fuente. Nunca se introduce un concepto
  "porque toca", sino porque **un requisito lo exige**.
- Justificación (fuente):
  > *"A New Requirement Leads Us to a New Architecture."* (Cap. 9)
  > *"...the most obvious way of doing things isn't always the way that helps you
  > manage complexity and evolving requirements."* (Preface → Why Python?)

### 3.6 No recortar pasos intermedios

- Nunca saltar de A a C escondiendo B. En particular, la secuencia
  **clase → instancia → objeto → uso** se muestra **paso por paso**, no todo en
  una sola línea.
- Si aparece una instancia, un objeto o un valor intermedio, **se nombra y se
  ve**. Comprimir "deja en el aire" a quien aprende.

### 3.7 Lo simple antes que lo avanzado ("low gear")

- Se usa la forma **explícita y simple** aunque sea más larga (p. ej. un `for`
  explícito antes que una *list comprehension*).
- Un método/forma "idiomática" avanzada se introduce **solo cuando el dolor lo
  pide** y se justifica desde la fuente; nunca por elegancia ni por ahorrar líneas.
- Justificación (fuente):
  > *"When starting a journey, the bicycle needs to be in a low gear so that it can
  > overcome inertia."* (Cap. 5 → High and Low Gear)

### 3.8 Las figuras de la fuente no se omiten

- El `.md` perdió las imágenes del libro (solo conserva los pies de figura). Las
  imágenes **sí están en el PDF**.
- Para **cada figura** que un capítulo referencie, la lección debe:
  1. **Rescatar y mostrar la imagen original** desde el PDF, guardada en
     `docs/fuente/imagenes/fig-N-M.png`.
  2. **Reproducirla como diagrama Mermaid** (código; ver §3.9) **fiel a la figura
     del libro**.
  3. **Explicarla en prosa**: qué muestra y por qué importa.
- Lo mismo aplica a **cualquier imagen que el aprendiz comparta**: se analiza y se
  usa, nunca se ignora.

### 3.9b Ejercicios de refuerzo (académicos)

Cada lección incluye una carpeta `paso6_ejercicios/` (en Fase 1: `ejercicios/micro-paso-M/`) con **3 ejercicios resueltos** más
**1 reto opcional** para el aprendiz. Formato de cada ejercicio:

1. **Problema** — enunciado en lista enumerada.
2. **Solución mala (que funciona)** — corre, pero con un defecto.
3. **Solución buena** — corregida, **resaltando qué hacía mal la anterior**.

El reto (4.º) trae solo el enunciado: el aprendiz escribe su solución mala y su buena,
y se revisan juntos. Cada solución se guarda como `.py` ejecutable **verificado**.

**Estructura de carpetas (dividida, no aglomerada):** cada ejercicio tiene **su propio
`README.md`** (enunciado + mala/buena), y cada tipo de solución va en su subcarpeta.
No hay un `ejercicios.md` único.

```
lecciones/NN-nombre/paso6_ejercicios/
├── ejercicio-1/
│   ├── README.md               (enunciado + mala/buena de ESTE ejercicio)
│   ├── solucion_mala/main.py
│   └── solucion_buena/main.py
├── ejercicio-2/ …
├── ejercicio-3/ …
└── ejercicio-4-reto/
    ├── README.md
    ├── solucion_mala/main.py   (plantilla para el aprendiz)
    └── solucion_buena/main.py  (plantilla para el aprendiz)
```

Nombres explícitos (`solucion_mala` / `solucion_buena`) y punto de entrada estándar
`main.py` en cada una, para que la estructura escale con orden.

**Ver la mejora:** desde la carpeta del ejercicio,
`git diff --no-index solucion_mala/main.py solucion_buena/main.py` muestra línea por
línea qué cambió.

**Cada herramienta en su escala:**

1. **Ejercicios pequeños (Fase 0) → carpetas** `solucion_mala/` y `solucion_buena/`.
   Duplicar pocas líneas cuesta poco y tenerlas lado a lado se lee mejor.
2. **Proyecto que crece (Fase 1, allocation) → un único código que evoluciona con
   Git.** La versión simple es un commit, la mejora es el commit siguiente, y cada
   capítulo cierra en su rama (ver §6.1). No se duplica código.
3. **No se usa Git dentro de subcarpetas** (repos anidados o submódulos): un repo
   anidado no sube su contenido y los submódulos exigen repos aparte.

**Dónde vive cada cosa (orden del repo):**

- **Fase 0 (Python/POO/SOLID):** cada lección autocontenida en `lecciones/NN-nombre/`.
- **Fase 1 (el libro):** cada capítulo es **autocontenido** en
  `fase-1/capitulos/NN-nombre/`, como una lección:
  - `README.md` — la **clase** del capítulo (micro-pasos, estructura 0–9).
  - `proyecto/` — el **código** del proyecto tal como queda **al final de ese
    capítulo** (un *snapshot*). El capítulo N parte del código del N-1 y lo evoluciona;
    la diferencia entre capítulos se ve comparando sus `proyecto/`. Se corre con, p. ej.,
    `uv run pytest fase-1/capitulos/01-domain-modeling/proyecto/ -q`.
  - `ejercicios/micro-paso-M/` — **ejercicios de refuerzo** por micro-paso (misma
    estructura que `lecciones/`: 3 ejercicios + 1 reto, `solucion_mala/main.py` vs
    `solucion_buena/main.py`).

### 3.9 Los diagramas se entregan como código Mermaid

- Los diagramas se dan **como bloque de código Mermaid** (el aprendiz lo pega en
  un previsualizador). **No** se renderizan a imagen.
- Deben **reproducir fielmente las figuras que da el libro** (mismos nombres,
  cajas, relaciones y sentido). Cuando el diagrama venga de una figura concreta,
  se cita (p. ej. *"Figure 1-3"*).
- Siempre acompañados de su **explicación en prosa** (regla 9).

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

## 5. Estructura fija de cada lección (formato "formulario académico")

Cada lección vive en `lecciones/NN-nombre/` y es un **formulario**: como un compendio
académico, junta teoría, fórmulas, propiedades, errores típicos, ejemplos resueltos y
problemas propuestos con claves. La **plantilla de referencia** es
[`lecciones/05-listas-y-diccionarios/`](lecciones/05-listas-y-diccionarios/).

### 5.1 Guía y orden de estudio

- El repo tiene un **"▶ EMPIEZA AQUÍ"** en el [`README.md`](README.md) raíz y una guía
  [`COMO-ESTUDIAR.md`](COMO-ESTUDIAR.md).
- [`lecciones/README.md`](lecciones/README.md) lista las lecciones **en orden**, con
  *Antes necesitas*, tiempo aproximado y un mapa Mermaid de dependencias.
- Cada lección tiene arriba **"Orden de estudio: N de 18"**, la **Ruta de estudio** (tabla de
  pasos con tiempos) y navegación **⬅️ anterior · 🏠 índice · ➡️ siguiente** (arriba y abajo).
- Al final, un **semáforo 🚦** indica si se puede avanzar: 🟢 ≥ 9/12 problemas + `paso3`
  correcto + preguntas sin mirar · 🟡 6–8 (repasar §8 y §9) · 🔴 < 6 (repetir).
- El aprendiz registra su avance en `progreso/fase-0-python.md` → *"Mi avance"*.

### 5.2 Secciones del README (paso 0)

La numeración es **fija en todas las lecciones** (el semáforo y la guía la citan por número):

- Arriba: título, *"Orden de estudio: N de 18"*, navegación ⬅️🏠➡️ y **🧭 Ruta de estudio**.
- **§0 🧭 La pregunta** — *"Tengo W, ahora me piden X, ¿qué hago?"* (§3.5)
- **§1 Objetivos** — qué podrá hacer al terminar.
- **§2 Cita de la fuente** — fragmento exacto, verificado contra `docs/fuente/`.
- **§3 El dolor / necesidad** — por qué lo que tenía ya no basta (regla 2).
- **§4 📘 Teoría** — definiciones en recuadros, vocabulario y regla de oro.
- **§5 y §6 🧮 Formulario** — tablas *operación · sintaxis · ejemplo · resultado* (en SOLID:
  *síntoma · regla · plantilla · qué logra* y una tabla de diagnóstico).
- **§7 📐 Propiedades** — las reglas que siempre se cumplen.
- **§8 ⚠️ Errores frecuentes** — ❌ así no · qué pasa (mensaje real) · ✅ así sí.
- **§9 ✍️ Ejemplos resueltos** — 4, de fácil a avanzado, paso a paso y con traza (§3.6).
- **§10 📝 Problemas propuestos** — 12: 4 🟢, 4 🟡, 4 🔴 (el último, puente al libro).
- **§11 🔑 Claves** — respuestas plegadas, **sacadas de la salida real** del solucionario.
- **§12 🗺️ Mapa mental / figura** — Mermaid en código (§3.9) + explicación; figura del libro si la hay (§3.8).
- **§13 🌳 Árbol de archivos** (regla 7).
- **§14 🤝 Tu turno y ✅ comprobación** — ejecutar y comparar (00–07) o pytest rojo → verde (08+).
- **§15 ❓ Preguntas de recuerdo** — con respuesta plegada (§3.4).
- **§16 🚦 Semáforo** — criterio para pasar a la siguiente.

### 5.3 Archivos (numerados en el orden en que se estudian)

```
lecciones/NN-nombre/
├── README.md                    ← PASO 0 · EMPIEZA AQUÍ (el formulario)
├── paso1_formulas.py            ← PASO 1 · cada fila de las tablas, ejecutable y etiquetada (L1, D1…)
├── paso2_ejemplos_resueltos.py  ← PASO 2 · los ejemplos resueltos del README
├── paso3_tu_turno.py            ← PASO 3 · huecos # TODO + "Salida esperada" (§3.2)
├── paso4_tu_turno_solucion.py   ← PASO 4 · solución de referencia
├── test_paso3_tu_turno.py       ← (desde la 08) test de paso3: rojo → verde (§3.3)
├── paso5_solucionario/          ← PASO 5 · nivel_basico.py, nivel_intermedio.py, nivel_avanzado.py
└── paso6_ejercicios/            ← PASO 6 · refuerzo mala vs buena (§3.9b)
```

- Se usa `pasoN_…` y no `N_…` porque un módulo cuyo nombre empieza con un número **no se puede
  importar** (importa desde la Lección 08, con pytest).
- **pytest se corre una lección a la vez** (`uv run pytest lecciones/NN-nombre -q`): desde la 08 todas
  repiten `paso3_tu_turno.py` y `test_paso3_tu_turno.py`; juntar dos lecciones da *import file mismatch*.
  Los tests de `paso3` empiezan en **rojo a propósito** (TDD: el aprendiz los pone en verde).
- **Verificación obligatoria** antes de dar una lección por construida: todos los `.py` corren
  (código de salida 0), las tablas y claves salen de la salida real, los Mermaid renderizan y
  las citas existen en la fuente.

---

## 6. Herramientas

- **Python 3.12** (exacto; fijado en `.python-version` y `requires-python = ">=3.12,<3.13"`).
  No se usa 3.13 ni otra versión.
- **uv** para entorno y dependencias (regla 8)
- **pytest** para las pruebas
- **FastAPI** para la capa web (regla 4)

### 6.1 Flujo de trabajo con Git

Todo lo que hagamos y aprendamos se registra con **Git**: ramas y commits.

1. **Rama de integración:** `ccr-b56bf27c-qa5zqh` (la designada por la sesión).
2. **Una rama por trabajo/lección**, partiendo de la de integración:
   - lecciones → `leccion-NN-nombre` (ej. `leccion-01-variables`)
   - configuración/ajustes → `config/...` o `chore/...`
   - capítulos del libro (Fase 1) → `capitulo-NN-nombre`; cada mejora del proyecto
     es un commit dentro de esa rama. Así lo organiza el libro:
     *"each chapter has its own branch"* (Preface → Example Code and Coding Along).
3. **Commits pequeños y descriptivos** a medida que avanzamos (no uno gigante al final).
4. Al terminar, se **mergea** la rama de trabajo en la de integración y se hace push.
5. Git también es **material de aprendizaje**: explicamos cada comando que usamos.

---

## 7. Mapa del aprendizaje (orden previsto)

**Fase 0 — Python desde cero** (regla 5): ejecutar código, variables, tipos,
condicionales, bucles, funciones, estructuras de datos, clases/objetos,
excepciones, módulos, entorno con `uv`, y primer `pytest` (lecciones 00–08);
**POO a fondo** (encapsulación, herencia, polimorfismo, abstracción; 09–12) y
**SOLID** (SRP, OCP, LSP, ISP, DIP; 13–17, con foco en SRP y DIP, que usa el libro).

**Fase 1 — Arquitectura (Cosmic Python):**

1. Domain Modeling / DDD (cap. 1)
2. Repository Pattern (cap. 2)
3. Coupling & Abstractions (cap. 3)
4. Service Layer + API con **FastAPI** (cap. 4)
5. TDD en marchas alta y baja (cap. 5)
6. Unit of Work (cap. 6)
7. Aggregates & Consistency (cap. 7)
8. Events & Message Bus y arquitectura dirigida por eventos (caps. 8–13)

El avance se registra en [`progreso/`](progreso/) — un índice general
([`progreso/README.md`](progreso/README.md)) y un archivo por capítulo con sus
secciones y figuras.
