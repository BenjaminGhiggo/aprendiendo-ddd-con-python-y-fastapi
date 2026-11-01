# Ejercicio 2 — Bus con cola (cascada)

> Cap. 9 · micro-paso 1 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala procesa un solo mensaje; la buena usa una cola que recoge eventos nuevos.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
