# Ejercicio 1 — Pedido que hace demasiado

> Lección 13 · refuerzo (SRP). Cita (regla 6): *"SOLID ... single responsibility ..."* — Cap. 1.

**Problema:**
1. Un pedido calcula su total, imprime un recibo y se guarda.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Pedido:
    def total(self): ...
    def imprimir_recibo(self): ...
    def guardar(self): ...
```
🔴 **Qué hace mal:** `Pedido` tiene **tres razones** para cambiar (la regla del total, el
formato del recibo, la forma de guardar). Un cambio en cualquiera toca la misma clase.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Pedido:
    def total(self):
        return sum(self.precios)

def imprimir_recibo(pedido): ...
def guardar(pedido): ...
```
🟢 **Qué mejoró:** `Pedido` solo conoce la regla del negocio; recibo y guardado son
responsabilidades aparte. Cada una cambia por su cuenta.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
