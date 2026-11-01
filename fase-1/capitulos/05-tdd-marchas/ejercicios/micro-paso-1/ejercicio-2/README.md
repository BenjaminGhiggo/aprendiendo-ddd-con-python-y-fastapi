# Ejercicio 2 — Preparar con un servicio

> Cap. 5 · micro-paso 1 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala construye objetos de dominio en el test; la buena usa un servicio agregar.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
