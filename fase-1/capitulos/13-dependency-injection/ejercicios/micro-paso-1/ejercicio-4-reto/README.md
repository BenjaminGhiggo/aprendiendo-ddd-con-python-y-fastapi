# Ejercicio 4 (reto) — Closure vs partial

> Cap. 13 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala usa late binding en un bucle (todos capturan el último valor); la buena usa functools.partial.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
