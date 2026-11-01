# Ejercicio 1 — Emitir, no llamar al siguiente

> Cap. 9 · micro-paso 1 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala encadena handlers a mano; la buena emite eventos y el bus los despacha.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
