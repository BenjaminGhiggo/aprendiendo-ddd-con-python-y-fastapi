# Ejercicio 1 — Bus estático vs bus configurable

> Cap. 13 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala tiene handlers fijos en un módulo; la buena es una clase que recibe sus handlers.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
