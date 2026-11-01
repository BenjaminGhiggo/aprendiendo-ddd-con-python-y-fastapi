# Ejercicio 3 — unsafe_hash conserva igualdad y set

> Cap. 2 · micro-paso 2 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): clase sin igualdad; dos
líneas iguales son objetos distintos y no deduplican. 🔴

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): `unsafe_hash` → igualdad
por valor y hash → el `set` deduplica. 🟢

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
