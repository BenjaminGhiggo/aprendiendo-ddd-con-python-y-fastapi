# Capítulo 13 — Dependency Injection (and Bootstrapping)

> Estado: ✅ COMPLETO · Parte II (cierre) · Fuente: `docs/fuente/...md` (cap. 13)

## La pregunta motor (§3.5)
> *"Mis handlers importan directo email/UoW/Redis y para testear mockeo todo.
> ¿Cómo hago las dependencias fáciles de cambiar sin tanto mock?"*

## Secciones (índice)
- [x] 13.a Implicit Versus Explicit Dependencies
- [x] 13.b Aren't Explicit Dependencies Totally Weird and Java-y?
- [x] 13.c Preparing Handlers: Manual DI with Closures and Partials
- [x] 13.d An Alternative Using Classes
- [x] 13.e A Bootstrap Script
- [x] 13.f Message Bus Is Given Handlers at Runtime
- [x] 13.g Using Bootstrap in Our Entrypoints
- [x] 13.h Initializing DI in Our Tests
- [x] 13.i Building an Adapter "Properly": A Worked Example
  - [x] Define the Abstract and Concrete Implementations
  - [x] Make a Fake Version for Your Tests
  - [x] Figure Out How to Integration Test the Real Thing
- [x] 13.j Wrap-Up

## Figuras del capítulo (§3.8)
- [x] Figure 13-1. Without bootstrap
- [x] Figure 13-2. Bootstrap takes care of all that in one place
- [x] Figure 13-3. Bootstrapper between entrypoints and message bus

## Comprobación (§3.4)
- [x] Ejercicios · [x] pytest (34 passed) · [x] Preguntas de recuerdo · [x] Integrado en el proyecto
