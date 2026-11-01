# Ejercicio 1 — frozen vs unsafe_hash (para el ORM)

> Cap. 2 · micro-paso 2 · refuerzo.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): `frozen=True`. 🔴 El ORM
necesita escribir atributos al cargar de la BD, y frozen lo impide (`FrozenInstanceError`).

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): `unsafe_hash=True`. 🟢
Mantiene igualdad por valor y hash, pero el ORM puede escribir.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
