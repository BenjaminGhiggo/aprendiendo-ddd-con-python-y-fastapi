# Capítulo 9 — Going to Town on the Message Bus

> Estado: ✅ COMPLETO · Parte II · Fuente: `docs/fuente/...md` (cap. 9)

## La pregunta motor (§3.5)
> _(se completa al empezar)_

## Secciones (índice)
- [x] 9.a A New Requirement Leads Us to a New Architecture
  - [x] Imagining an Architecture Change: Everything Will Be an Event Handler
- [x] 9.b Refactoring Service Functions to Message Handlers
  - [x] The Message Bus Now Collects Events from the UoW
  - [x] Our Tests Are All Written in Terms of Events Too
  - [x] A Temporary Ugly Hack: The Message Bus Has to Return Results
  - [x] Modifying Our API to Work with Events
- [x] 9.c Implementing Our New Requirement
  - [x] Our New Event
- [x] 9.d Test-Driving a New Handler
  - [x] Implementation
  - [x] A New Method on the Domain Model
- [x] 9.e Optionally: Unit Testing Event Handlers in Isolation with a Fake Message Bus
- [x] 9.f Wrap-Up
  - [x] What Have We Achieved?
  - [x] Why Have We Achieved?

## Figuras del capítulo (§3.8)
- [x] Figure 9-1. Before
- [x] Figure 9-2. The message bus is now the main entrypoint to the service layer
- [x] Figure 9-3. Batch quantity changed means deallocate and reallocate
- [x] Figure 9-4. Sequence diagram for reallocation flow

## Comprobación (§3.4)
- [x] Ejercicios · [ ] pytest · [ ] Preguntas de recuerdo · [ ] Integrado en el proyecto
