# Ejercicio 1 — Publicar, no llamar directo

> Cap. 11 · micro-paso 1 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala llama directo a otro servicio; la buena publica un evento (desacople temporal).

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
