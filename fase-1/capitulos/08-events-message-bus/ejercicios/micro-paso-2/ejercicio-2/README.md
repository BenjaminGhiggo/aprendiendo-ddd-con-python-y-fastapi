# Ejercicio 2 — Emitir, no llamar

> Cap. 8 · micro-paso 2 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala llama al manejador a mano; la buena emite el evento al bus.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
