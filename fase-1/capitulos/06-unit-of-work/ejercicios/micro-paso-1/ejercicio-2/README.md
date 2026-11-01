# Ejercicio 2 — Deshacer al salir

> Cap. 6 · micro-paso 1 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala no deshace lo no confirmado; la buena hace rollback en __exit__.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
