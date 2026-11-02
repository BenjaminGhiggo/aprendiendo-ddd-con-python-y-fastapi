# Ejercicio 1 — Proteger la cantidad de un lote

> Lección 09 · refuerzo. Cita (regla 6): *"Encapsulation ... hiding details and
> protecting the consistency of our data."* — Introducción.

**Problema:**
1. Un lote tiene una cantidad que **nunca** debería quedar en un valor imposible.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Lote:
    def __init__(self, cantidad):
        self.cantidad = cantidad

lote = Lote(20)
lote.cantidad = -999
print(lote.cantidad)
```
🔴 **Qué hace mal:** `cantidad` es pública, así que cualquier parte del programa la deja
en `-999` y el lote queda en un estado imposible.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Lote:
    def __init__(self, cantidad):
        self._cantidad = cantidad
    def cantidad_disponible(self):
        return self._cantidad
    def asignar(self, pedido):
        if pedido > self._cantidad:
            raise ValueError("No hay stock suficiente")
        self._cantidad = self._cantidad - pedido
```
🟢 **Qué mejoró:** el dato es privado (`_cantidad`) y solo cambia por `asignar`, que
aplica la regla. El objeto cuida su propio estado.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
