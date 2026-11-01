# Ejercicio 2 — Un bootstrap, no armar deps en cada sitio

> Cap. 13 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala arma la UoW en cada entrypoint; la buena la arma una vez y devuelve algo listo.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
