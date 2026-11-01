# Ejercicio 3 — SELECT N+1

> Cap. 12 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala hace 1+N consultas (una por item); la buena hace una sola consulta al modelo de lectura.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
