# Ej2 — MALA (funciona): el saldo se modifica directo; puede quedar negativo.
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

cuenta = Cuenta(100)
cuenta.saldo = cuenta.saldo - 1000   # retira más de lo que hay, sin control
print(cuenta.saldo)
