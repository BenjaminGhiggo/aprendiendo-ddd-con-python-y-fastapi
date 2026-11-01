# Ejercicio 1 — Inyectar el repositorio

> Cap. 2 · micro-paso 1 · refuerzo. Cita: *"This self-imposed simplicity stops us from
> coupling our domain model to the database."* — Cap. 2.

**Problema:** registrar un lote sin acoplar el servicio al almacenamiento.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): guarda en una lista global
dentro de la función. 🔴 No se puede cambiar el almacenamiento ni probar sin tocarla.

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): la función recibe un
`repo` con `agregar`. 🟢 El servicio no sabe cómo se guarda (DIP).

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
