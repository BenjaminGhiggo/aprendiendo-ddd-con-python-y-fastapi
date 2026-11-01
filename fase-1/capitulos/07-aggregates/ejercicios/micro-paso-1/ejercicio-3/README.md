# Ejercicio 3 — Reglas dentro del agregado

> Cap. 7 · micro-paso 1 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala deja la regla afuera (se viola); la buena la encapsula en el agregado.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
