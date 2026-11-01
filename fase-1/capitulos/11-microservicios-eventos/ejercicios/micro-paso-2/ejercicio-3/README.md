# Ejercicio 3 — El dominio no conoce Redis

> Cap. 11 · micro-paso 2 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala publica desde el dominio; la buena registra evento y un handler publica.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
