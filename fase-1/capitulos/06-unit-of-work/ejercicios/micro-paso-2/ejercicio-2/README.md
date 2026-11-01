# Ejercicio 2 — Cerrar la sesión

> Cap. 6 · micro-paso 2 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala no cierra la sesión; la buena la cierra en __exit__.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
