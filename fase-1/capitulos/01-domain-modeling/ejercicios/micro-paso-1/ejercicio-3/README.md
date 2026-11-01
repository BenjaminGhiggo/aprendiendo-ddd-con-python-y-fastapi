# Ejercicio 3 — Nombres del dominio

> Cap. 1 · micro-paso 1 · refuerzo. Cita (regla 6): *"the names ... are taken from the
> business jargon."* — Cap. 1.

**Problema:**
1. Modela una línea de pedido con nombres claros.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
@dataclass(frozen=True)
class Datos:
    a: str
    b: int
```
🔴 **Qué hace mal:** `Datos`, `a`, `b` no dicen nada. Un no-programador no entendería
qué modela.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
@dataclass(frozen=True)
class LineaPedido:
    sku: str
    cantidad: int
```
🟢 **Qué mejoró:** los nombres vienen del lenguaje del negocio; el código se lee como el
dominio.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
