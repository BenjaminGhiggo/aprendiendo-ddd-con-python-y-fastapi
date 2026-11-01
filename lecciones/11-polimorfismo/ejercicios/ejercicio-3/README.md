# Ejercicio 3 — Medios de pago

> Lección 11 · refuerzo.

**Problema:**
1. Pagar en efectivo o con tarjeta, con mensajes distintos.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
def pagar(metodo, monto):
    if metodo == "efectivo":
        return "Pagaste " + str(monto) + " en efectivo"
    elif metodo == "tarjeta":
        return "Pagaste " + str(monto) + " con tarjeta"
```
🔴 **Qué hace mal:** para agregar un medio nuevo (Yape, transferencia…) hay que editar
este `if`, arriesgando romper lo que ya andaba.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Efectivo:
    def pagar(self, monto):
        return "Pagaste " + str(monto) + " en efectivo"
class Tarjeta:
    def pagar(self, monto):
        return "Pagaste " + str(monto) + " con tarjeta"

for metodo in [Efectivo(), Tarjeta()]:
    print(metodo.pagar(100))
```
🟢 **Qué mejoró:** cada medio de pago es una clase con `pagar()`. Agregar uno nuevo no
toca el código existente (esto conecta con el OCP, lección 14).

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
