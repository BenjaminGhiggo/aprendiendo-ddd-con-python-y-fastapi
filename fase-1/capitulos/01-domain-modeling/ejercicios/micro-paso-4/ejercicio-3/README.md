# Ejercicio 3 — Orden de lotes con `__gt__`

> Cap. 1 · micro-paso 4 · refuerzo. Cita (regla 6): *"being able to use sorted() on our
> list of batches is nice ... we implement __gt__."* — Cap. 1.

**Problema:** preferir el stock que ya está en almacén antes que los envíos.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def asignar(cantidad, lotes):
    for lote in lotes:   # en el orden recibido
        ...
```
🔴 **Qué hace mal:** asigna según el orden en que llegan los lotes; puede usar un envío
futuro antes que el stock que ya está en almacén.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
def __gt__(self, other):
    if self.eta is None: return False
    if other.eta is None: return True
    return self.eta > other.eta

for lote in sorted(lotes):
    ...
```
🟢 **Qué mejoró:** `__gt__` hace que `sorted()` ponga el stock en almacén (sin eta)
primero, y luego los envíos por fecha.

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
