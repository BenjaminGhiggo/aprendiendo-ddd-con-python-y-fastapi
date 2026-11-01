# Capítulos — Fase 1 (el libro *Cosmic Python*)

Cada capítulo es **autocontenido** (como `lecciones/`): dentro de su carpeta están
**la clase** (`README.md`), **el código** del proyecto tal como queda al final de ese
capítulo (`proyecto/`) y los **ejercicios** (`ejercicios/`).

El código es un **snapshot por capítulo**: el capítulo N parte del código del N-1 y lo
hace evolucionar. Para ver qué cambió entre capítulos, se comparan sus carpetas
`proyecto/` (o el historial de Git).

| # | Capítulo | Carpeta | Estado |
|---|----------|---------|--------|
| 01 | Domain Modeling | [01-domain-modeling](01-domain-modeling/) | ✅ completo |
| 02 | Repository Pattern | [02-repository-pattern](02-repository-pattern/) | ✅ completo |
| 03 | Coupling and Abstractions | [03-coupling-y-abstracciones](03-coupling-y-abstracciones/) | ✅ completo |
| 04 | Service Layer + API (FastAPI) | [04-service-layer-fastapi](04-service-layer-fastapi/) | ✅ completo |
| 05 | TDD High/Low Gear | [05-tdd-marchas](05-tdd-marchas/) | ✅ completo |
| 06 | Unit of Work | [06-unit-of-work](06-unit-of-work/) | ✅ completo |
| 07 | Aggregates | [07-aggregates](07-aggregates/) | ✅ completo |
| 08 | Events and the Message Bus | [08-events-message-bus](08-events-message-bus/) | ✅ completo |
| 09 | Going to Town on the Message Bus | [09-message-bus-a-fondo](09-message-bus-a-fondo/) | ✅ completo |
| 10 | Commands and Command Handler | [10-commands](10-commands/) | ✅ completo |
| 11 | Event-Driven Microservices | [11-microservicios-eventos](11-microservicios-eventos/) | ✅ completo |
| 12 | CQRS | [12-cqrs](12-cqrs/) | ✅ completo |
| 13 | Dependency Injection (and Bootstrapping) | [13-dependency-injection](13-dependency-injection/) | ✅ completo |

> ✅ **Los 13 capítulos del libro están completos.** Quedan los apéndices como material
> opcional de cierre (ver [`../../progreso/apendices.md`](../../progreso/apendices.md)).

- El código de un capítulo se corre con, p. ej.,
  `uv run pytest fase-1/capitulos/01-domain-modeling/proyecto/ -q`.
- El avance detallado por secciones está en [`../progreso/`](../progreso/).
