# Ejercicio 1 — Agrupar los datos de un lote

> Lección 06 · refuerzo. Cita (regla 6): *"First cut of a domain model for batches
> (model.py)"* — Cap. 1.

**Problema:**
1. Guarda la referencia, el sku y la cantidad de un lote, y muéstralos.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
referencia = "LOTE-001"
sku = "MESA"
cantidad = 20
print(referencia, sku, cantidad)
```
🔴 **Qué hace mal:** los datos de un mismo lote están sueltos. Para un segundo lote
tendrías `referencia2`, `sku2`, `cantidad2`… no escala.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Lote:
    def __init__(self, referencia, sku, cantidad):
        self.referencia = referencia
        self.sku = sku
        self.cantidad = cantidad

lote = Lote("LOTE-001", "MESA", 20)
print(lote.referencia, lote.sku, lote.cantidad)
```
🟢 **Qué mejoró:** un objeto agrupa los datos del lote. Cada lote nuevo es otra instancia.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
