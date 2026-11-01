# Lecciones

Cada lección es **autocontenida**: su clase completa está en el `README.md` de su
carpeta, junto a su código `.py`. Puedes repasarla cuando quieras sin depender del chat.

## Fase 0 — Python desde cero

| # | Lección | Carpeta | Rama de repaso |
|---|---------|---------|----------------|
| 00 | ¿Qué es ejecutar un programa? | [00-que-es-ejecutar-un-programa](00-que-es-ejecutar-un-programa/) | `repaso/leccion-00` |
| 01 | Variables y tipos | [01-variables-y-tipos](01-variables-y-tipos/) | `repaso/leccion-01` |
| 02 | Condicionales (if/else) | [02-condicionales](02-condicionales/) | `repaso/leccion-02` |
| 03 | Bucles (for/while) | [03-bucles](03-bucles/) | `repaso/leccion-03` |
| 04 | Funciones | [04-funciones](04-funciones/) | `repaso/leccion-04` |
| 05 | Listas y diccionarios | [05-listas-y-diccionarios](05-listas-y-diccionarios/) | `repaso/leccion-05` |
| 06 | Clases y objetos | [06-clases-y-objetos](06-clases-y-objetos/) | `repaso/leccion-06` |
| 07 | Excepciones | [07-excepciones](07-excepciones/) | `repaso/leccion-07` |
| 08 | Módulos, entorno con uv y primer pytest | [08-modulos-y-pytest](08-modulos-y-pytest/) | `repaso/leccion-08` |

### POO (a fondo) y SOLID
| # | Lección | Carpeta | Rama de repaso |
|---|---------|---------|----------------|
| 09 | Encapsulación | [09-encapsulacion](09-encapsulacion/) | `repaso/leccion-09` |
| 10 | Herencia | [10-herencia](10-herencia/) | `repaso/leccion-10` |
| 11 | Polimorfismo | [11-polimorfismo](11-polimorfismo/) | `repaso/leccion-11` |
| 12 | Abstracción (ABC) | [12-abstraccion](12-abstraccion/) | `repaso/leccion-12` |
| 13 | SOLID · SRP | [13-srp](13-srp/) | `repaso/leccion-13` |
| 14 | SOLID · OCP | [14-ocp](14-ocp/) | `repaso/leccion-14` |
| 15 | SOLID · LSP | [15-lsp](15-lsp/) | `repaso/leccion-15` |

_(La lista crece a medida que avanzamos. El checklist completo está en [`../progreso/`](../progreso/).)_

## Cómo repasar una lección

1. **Lo más simple:** abre el `README.md` de la carpeta de la lección (aquí en GitHub
   o en tu editor). Es la clase completa.
2. **Volver al estado exacto de una lección** (marcador con rama):
   ```bash
   git switch repaso/leccion-01   # el repo tal como quedó en la Lección 01
   git switch -                   # volver a donde estabas
   ```
3. **Ver qué cambió en una lección** (su commit):
   ```bash
   git show repaso/leccion-02     # muestra los cambios de esa lección
   ```

> Nota: usamos **ramas** (`repaso/leccion-NN`) en vez de tags porque la integración
> de GitHub de esta sesión permite subir ramas pero no etiquetas.
