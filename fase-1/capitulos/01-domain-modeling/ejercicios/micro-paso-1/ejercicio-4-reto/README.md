# Ejercicio 4 (opcional) — Reto para ti ✍️

> Cap. 1 · micro-paso 1 · refuerzo. Lo resuelves tú.

**Problema:**
1. Un value object `Dinero` con `moneda` y `cantidad`.
2. No debería poder mutarse tras crearse.

**Tu turno:**
- Versión mala en [`solucion_mala/main.py`](solucion_mala/main.py) (clase mutable).
- Versión buena en [`solucion_buena/main.py`](solucion_buena/main.py) (`@dataclass(frozen=True)`).

**Para compararlas** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
