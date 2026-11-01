# Ejercicio 3 — `obtener` devuelve uno, no una lista

> Cap. 2 · micro-paso 3 · refuerzo. Cita: *"self.session.query(model.Batch).filter_by(
> reference=reference).one()"* — Cap. 2.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): `obtener` devuelve una lista;
quien llama tiene que recordar el `[0]`. 🔴

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): `obtener` devuelve el lote
(como `.one()`). 🟢

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
