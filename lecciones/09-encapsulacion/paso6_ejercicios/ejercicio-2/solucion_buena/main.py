# Ej2 — BUENA: retirar es un método que valida que haya fondos.
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo
    def saldo(self):
        return self._saldo
    def retirar(self, monto):
        if monto > self._saldo:
            raise ValueError("Fondos insuficientes")
        self._saldo = self._saldo - monto

cuenta = Cuenta(100)
try:
    cuenta.retirar(1000)
except ValueError as e:
    print(e)
print(cuenta.saldo())
