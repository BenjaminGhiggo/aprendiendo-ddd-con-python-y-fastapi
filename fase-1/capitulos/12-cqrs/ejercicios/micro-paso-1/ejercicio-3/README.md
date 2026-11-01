# Ejercicio 3 — Separar lecturas de escrituras

> Cap. 12 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala mezcla todo en una función; la buena separa handlers (escriben) de vistas (leen).

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
