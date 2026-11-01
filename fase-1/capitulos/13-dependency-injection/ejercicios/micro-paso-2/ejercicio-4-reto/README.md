# Ejercicio 4 (reto) — Cambiar el canal en un solo sitio

> Cap. 13 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): en la mala el canal está regado por los handlers; en la buena se elige en el bootstrap y se inyecta.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
