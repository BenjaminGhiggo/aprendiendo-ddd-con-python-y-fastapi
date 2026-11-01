# Ejercicio 2 — Datos sueltos vs objeto

> Cap. 1 · micro-paso 1 · refuerzo.

**Problema:**
1. Varias funciones necesitan el sku y la cantidad de una línea.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def describir(sku, cantidad): ...
def es_grande(sku, cantidad): ...
```
🔴 **Qué hace mal:** el sku y la cantidad viajan sueltos por cada función; es fácil
pasar un sku que no corresponde a esa cantidad.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
@dataclass(frozen=True)
class LineaPedido:
    sku: str
    cantidad: int

def describir(linea): ...
def es_grande(linea): ...
```
🟢 **Qué mejoró:** una `LineaPedido` agrupa los datos; las funciones reciben el objeto
coherente.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
