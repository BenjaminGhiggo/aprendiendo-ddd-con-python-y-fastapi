# Ejercicio 2 — Post/Redirect/Get

> Cap. 12 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala devuelve datos tras el POST (recargar duplica); la buena responde 202 y un GET aparte lee.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
