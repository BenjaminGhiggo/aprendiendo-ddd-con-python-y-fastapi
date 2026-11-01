# Ejercicio 1 — Aislar handlers de evento

> Cap. 10 · micro-paso 2 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala deja que un fallo rompa el flujo; la buena aísla cada handler de evento.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
