# Ejercicio 1 — Leer sin recorrer el dominio

> Cap. 12 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala recorre productos→lotes→líneas con bucles; la buena hace un SELECT sobre una tabla desnormalizada.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
