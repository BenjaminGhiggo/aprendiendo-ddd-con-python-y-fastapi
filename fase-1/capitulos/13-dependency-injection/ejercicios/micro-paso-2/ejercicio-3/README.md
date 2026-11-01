# Ejercicio 3 — Fake inyectada vs monkeypatch

> Cap. 13 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala parchea la función global para testear; la buena inyecta una implementación falsa.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
