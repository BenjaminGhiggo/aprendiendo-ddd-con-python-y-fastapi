# Ejercicio 1 — Endpoint gordo vs servicio

> Cap. 4 · micro-paso 1 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena**
([`solucion_buena/main.py`](solucion_buena/main.py)): la mala mezcla todo en el endpoint; la buena separa un servicio y el endpoint solo delega.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
