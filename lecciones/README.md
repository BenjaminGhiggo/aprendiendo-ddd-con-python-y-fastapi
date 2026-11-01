# Lecciones

Cada lección es **autocontenida**: su clase completa está en el `README.md` de su
carpeta, junto a su código `.py`. Puedes repasarla cuando quieras sin depender del chat.

## Fase 0 — Python desde cero

| # | Lección | Carpeta | Tag para repasar |
|---|---------|---------|------------------|
| 00 | ¿Qué es ejecutar un programa? | [00-que-es-ejecutar-un-programa](00-que-es-ejecutar-un-programa/) | `leccion-00` |
| 01 | Variables y tipos | [01-variables-y-tipos](01-variables-y-tipos/) | `leccion-01` |
| 02 | Condicionales (if/else) | [02-condicionales](02-condicionales/) | `leccion-02` |

_(La lista crece a medida que avanzamos. El checklist completo está en [`../progreso/`](../progreso/).)_

## Cómo repasar una lección

1. **Lo más simple:** abre el `README.md` de la carpeta de la lección.
2. **Volver al estado exacto de una lección** (marcador con tag):
   ```bash
   git checkout leccion-01      # te deja el repo tal como quedó en la Lección 01
   git switch -                 # para volver a donde estabas
   ```
3. **Ver qué cambió en una lección** (su commit):
   ```bash
   git show leccion-02          # muestra los cambios de esa lección
   ```
