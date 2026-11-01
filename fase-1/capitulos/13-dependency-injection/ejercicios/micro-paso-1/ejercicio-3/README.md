# Ejercicio 3 — Inyectar por la firma del handler

> Cap. 13 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala pasa todas las deps a todos (TypeError); la buena inspecciona la firma y pasa solo lo que pide.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
