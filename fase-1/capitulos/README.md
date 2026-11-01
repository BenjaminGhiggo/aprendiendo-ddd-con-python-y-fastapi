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
| 02 | Repository Pattern | [02-repository-pattern](02-repository-pattern/) | 🟡 en curso |
| 03 | Coupling and Abstractions | _(pendiente)_ | ⬜ |
| 04 | Service Layer + API (FastAPI) | _(pendiente)_ | ⬜ |
| 05 | TDD High/Low Gear | _(pendiente)_ | ⬜ |
| 06 | Unit of Work | _(pendiente)_ | ⬜ |
| 07 | Aggregates | _(pendiente)_ | ⬜ |
| 08–13 | Event-Driven Architecture | _(pendiente)_ | ⬜ |

- El código de un capítulo se corre con, p. ej.,
  `uv run pytest fase-1/capitulos/01-domain-modeling/proyecto/ -q`.
- El avance detallado por secciones está en [`../progreso/`](../progreso/).
