# Ejercicio 1 — Dependencia implícita vs explícita

> Cap. 13 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala importa y llama directo (hay que mockear); la buena recibe la dependencia como argumento (DIP).

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
