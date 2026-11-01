# Capítulo 12 — Command-Query Responsibility Segregation (CQRS)

> Estado: ✅ COMPLETO · Parte II · Fuente: `docs/fuente/...md` (cap. 12)

## La pregunta motor (§3.5)
> *"El endpoint de asignar modifica el stock Y devuelve datos; al recargar asigna dos veces.
> ¿Cómo separo leer de escribir?"*

## Secciones (índice)
- [x] 12.a Domain Models Are for Writing
- [x] 12.b Most Users Aren't Going to Buy Your Furniture
- [x] 12.c Post/Redirect/Get and CQS
- [x] 12.d Hold On to Your Lunch, Folks
- [x] 12.e Testing CQRS Views
- [x] 12.f "Obvious" Alternative 1: Using the Existing Repository
- [x] 12.g Your Domain Model Is Not Optimized for Read Operations
- [x] 12.h "Obvious" Alternative 2: Using the ORM
- [x] 12.i SELECT N+1 and Other Performance Considerations
- [x] 12.j Time to Completely Jump the Shark
  - [x] Updating a Read Model Table Using an Event Handler
- [x] 12.k Changing Our Read Model Implementation Is Easy
- [x] 12.l Wrap-Up

## Figuras del capítulo (§3.8)
- [x] Figure 12-1. Separating reads from writes
- [x] Figure 12-2. Sequence diagram for read model

## Comprobación (§3.4)
- [x] Ejercicios · [x] pytest (32 passed) · [x] Preguntas de recuerdo · [x] Integrado en el proyecto
