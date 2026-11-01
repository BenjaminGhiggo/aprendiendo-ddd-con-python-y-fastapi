# Proyecto — Sistema de asignación (allocation) · snapshot Capítulo 13

Snapshot del proyecto al final del **Capítulo 13 (Dependency Injection y Bootstrapping)**,
el **último capítulo del libro**. Parte del código del Capítulo 12.

Novedades de este capítulo:
- `notificaciones.py` — ejemplo trabajado: una dependencia implícita (`email`) convertida en
  un **adaptador**: ABC `NotificacionesAbstractas` + `NotificacionesEmail` (real).
- `mensajeria.py` — los handlers declaran **dependencias explícitas** (`uow`,
  `notificaciones`, `publicar`), y el bus pasa de módulo estático a **clase** `BusMensajes`.
- `bootstrap.py` — el **composition root**: declara defaults, arranca el ORM, **inyecta**
  dependencias en los handlers (vía `inspect.signature`) y devuelve el bus listo.
- `api.py` — el entrypoint ya no arma la UoW: pide un **bus** del bootstrap.
- `test_bootstrap.py` — prueba la inyección de dependencias en sí.

## Correr las pruebas
```bash
uv run pytest fase-1/capitulos/13-dependency-injection/proyecto/ -q      # 34 passed
```

## Glosario del dominio (lenguaje del negocio)
| Español (nuestro código) | Inglés (libro) | Qué es |
|---|---|---|
| bootstrap | bootstrap / composition root | único lugar donde se inyectan deps y se inicializa |
| BusMensajes | MessageBus | el bus, ahora una clase con sus handlers inyectados |
| NotificacionesAbstractas | AbstractNotifications | la abstracción del adaptador de notificaciones |
| inyectar_dependencias | inject_dependencies | casa la firma del handler con las deps por nombre |
