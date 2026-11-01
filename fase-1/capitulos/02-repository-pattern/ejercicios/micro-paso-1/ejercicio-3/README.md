# Ejercicio 3 — ABC evita repos a medio hacer

> Cap. 2 · micro-paso 1 · refuerzo. Cita: *"Python will refuse to let you instantiate a
> class that does not implement all the abstractmethods."* — Cap. 2.

**Mala** ([`solucion_mala/main.py`](solucion_mala/main.py)): un "repo base" con métodos
vacíos, instanciable. 🔴 Se puede usar y no guardar nada (bug silencioso).

**Buena** ([`solucion_buena/main.py`](solucion_buena/main.py)): `ABC` + `@abstractmethod`.
🟢 Python impide instanciarla sin implementar.

```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
