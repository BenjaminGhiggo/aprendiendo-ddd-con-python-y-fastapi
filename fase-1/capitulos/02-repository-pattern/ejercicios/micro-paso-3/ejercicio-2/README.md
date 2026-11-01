# Ejercicio 2 — Inyectar el repositorio

> Cap. 2 · micro-paso 3 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): el servicio crea `RepoSQL()`
adentro. 🔴 No se puede probar con un fake ni cambiar el almacenamiento.

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): el repo se inyecta por
parámetro. 🟢 Fake en pruebas, real en producción (DIP, Lección 17).

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
