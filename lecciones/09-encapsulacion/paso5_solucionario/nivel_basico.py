# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/09-encapsulacion/paso5_solucionario/nivel_basico.py


# Problemas 1 y 2: dato protegido (_saldo) + método lector + método que cambia.
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo               # E2 · protegido

    def saldo_actual(self):               # E3 · puerta para leer
        return self._saldo

    def depositar(self, monto):           # E4 · puerta para cambiar
        self._saldo = self._saldo + monto


cuenta = Cuenta("Ana", 100)
print("P1:", cuenta.saldo_actual())       # 100

cuenta.depositar(50)
print("P2:", cuenta.saldo_actual())       # 150

# Problema 3: Python NO impide tocar _saldo (es una convención). Funciona... y está mal.
otra = Cuenta("Luis", 100)
otra._saldo = -1
print("P3:", otra.saldo_actual(), "<- estado imposible: nadie revisó la regla")


# Problema 4: el método lector pasa a ser una PROPIEDAD (P1): se lee sin paréntesis.
class CuentaConPropiedad:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo


cuenta4 = CuentaConPropiedad("Ana", 100)
print("P4:", cuenta4.saldo)               # 100
