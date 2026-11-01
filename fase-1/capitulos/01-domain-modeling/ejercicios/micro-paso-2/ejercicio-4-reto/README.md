# Ejercicio 4 (opcional) — Reto para ti ✍️

> Cap. 1 · micro-paso 2 · refuerzo. Lo resuelves tú.

**Problema:**
1. Un `Cliente` es la misma persona si comparte su `id`, aunque cambie su `nombre`.

**Tu turno:**
- Mala en [`solucion_mala/main.py`](solucion_mala/main.py) (dataclass que compara por todos los campos).
- Buena en [`solucion_buena/main.py`](solucion_buena/main.py) (`__eq__`/`__hash__` por `id`).

**Para compararlas** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
