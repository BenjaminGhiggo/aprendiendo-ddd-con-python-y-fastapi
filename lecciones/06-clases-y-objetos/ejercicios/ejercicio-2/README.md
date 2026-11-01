# Ejercicio 2 — Juntar dato y regla

> Lección 06 · refuerzo.

**Problema:**
1. Un lote con cantidad 20 debe poder decir si puede asignar un pedido.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
lote = {"cantidad": 20}

def puede_asignar(lote, pedido):
    return lote["cantidad"] >= pedido

print(puede_asignar(lote, 5))
```
🔴 **Qué hace mal:** el dato (dict) y la regla (función) viven separados. Hay que pasar
el dict y recordar la clave exacta `"cantidad"`.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Lote:
    def __init__(self, cantidad):
        self.cantidad = cantidad
    def puede_asignar(self, pedido):
        return self.cantidad >= pedido

lote = Lote(20)
print(lote.puede_asignar(5))
```
🟢 **Qué mejoró:** la clase junta el dato y la regla. El objeto sabe responder por sí mismo.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
