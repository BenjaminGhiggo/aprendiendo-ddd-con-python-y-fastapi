# Ejercicio 2 — Un saldo que no puede quedar negativo

> Lección 09 · refuerzo.

**Problema:**
1. Una cuenta con saldo. Retirar más de lo que hay no debe permitirse.

**Solución mala (funciona)** — [`solucion_mala/main.py`](solucion_mala/main.py):
```python
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

cuenta = Cuenta(100)
cuenta.saldo = cuenta.saldo - 1000
print(cuenta.saldo)   # -900
```
🔴 **Qué hace mal:** el saldo se modifica directo desde afuera, sin ninguna validación.
Queda en `-900`, un estado inválido.

**Solución buena** — [`solucion_buena/main.py`](solucion_buena/main.py):
```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo
    def saldo(self):
        return self._saldo
    def retirar(self, monto):
        if monto > self._saldo:
            raise ValueError("Fondos insuficientes")
        self._saldo = self._saldo - monto
```
🟢 **Qué mejoró:** `retirar` valida antes de tocar el saldo. El saldo nunca queda negativo.

**Ver la mejora línea por línea** (desde esta carpeta):
```bash
git diff --no-index solucion_mala/main.py solucion_buena/main.py
```
