# Ejercicio 1 — Value object inmutable

> Cap. 1 · micro-paso 1 · refuerzo. Cita (regla 6): *"a value object ... we usually
> make them immutable."* — Cap. 1.

**Problema:**
1. Modela una `LineaPedido` (sku, cantidad). No debería poder cambiar tras crearse.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class LineaPedido:
    def __init__(self, sku, cantidad):
        self.sku = sku
        self.cantidad = cantidad

linea = LineaPedido("MESA", 2)
linea.cantidad = 999
```
🔴 **Qué hace mal:** la línea es mutable; cambiarle la cantidad la convierte en otra cosa
sin que nadie lo note. Un value object debería ser inmutable.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class LineaPedido:
    sku: str
    cantidad: int
```
🟢 **Qué mejoró:** `frozen=True` la hace inmutable; intentar mutarla lanza
`FrozenInstanceError`. Además da igualdad por valor gratis.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
