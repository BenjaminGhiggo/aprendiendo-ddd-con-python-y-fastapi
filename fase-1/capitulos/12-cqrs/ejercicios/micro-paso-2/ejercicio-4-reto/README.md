# Ejercicio 4 (reto) — Cambiar el motor del read model

> Cap. 12 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)) vs **Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la mala lee atada al dominio; la buena habla con el almacén por una interfaz (dict→Redis) sin tocar el dominio.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
