# Ejercicio 1 — Igualdad por valor

> Cap. 1 · micro-paso 2 · refuerzo. Cita (regla 6): *"Two lines with the same orderid,
> sku, and qty are equal."* — Cap. 1.

**Problema:** dos líneas con los mismos datos deberían ser iguales.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class LineaPedido:
    def __init__(self, sku, cantidad): ...
print(LineaPedido("MESA",2) == LineaPedido("MESA",2))   # False
```
🔴 **Qué hace mal:** sin `dataclass`, Python compara por objeto en memoria; dos líneas
iguales dan `False`.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
@dataclass(frozen=True)
class LineaPedido:
    sku: str
    cantidad: int
```
🟢 **Qué mejoró:** `@dataclass` da igualdad por valor: mismos datos → iguales.

**Ver la mejora** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
