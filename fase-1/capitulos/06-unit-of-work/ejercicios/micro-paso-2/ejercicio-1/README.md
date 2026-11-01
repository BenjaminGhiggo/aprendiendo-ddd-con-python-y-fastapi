# Ejercicio 1 — Atomicidad

> Cap. 6 · micro-paso 2 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala confirma operación por operación; la buena agrupa todo en una UoW (un commit).

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
