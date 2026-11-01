# Ejercicio 1 — Cambiar o responder, no ambos

> Cap. 12 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala escribe y devuelve a la vez; la buena separa command (escribe) de query (responde). CQS.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
