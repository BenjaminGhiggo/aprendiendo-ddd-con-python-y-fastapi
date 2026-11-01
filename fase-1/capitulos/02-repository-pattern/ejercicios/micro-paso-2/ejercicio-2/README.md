# Ejercicio 2 — Esquema aparte del modelo

> Cap. 2 · micro-paso 2 · refuerzo. Cita: *"The ORM ... knows about the domain model,
> and not the other way around."* — Cap. 2.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): el `Lote` lleva dentro
`tabla`/`columnas`. 🔴 El dominio "sabe" de la base de datos.

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): el modelo es puro; el
esquema vive aparte. 🟢 El dominio no sabe de BD.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
