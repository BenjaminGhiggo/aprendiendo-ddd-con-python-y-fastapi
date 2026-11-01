# Ejercicio 1 — Agrupar en una UoW

> Cap. 6 · micro-paso 1 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala maneja repo+commit sueltos; la buena los agrupa en una UoW context manager.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
