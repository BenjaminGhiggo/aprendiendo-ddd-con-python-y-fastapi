# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/09-encapsulacion/paso5_solucionario/nivel_intermedio.py


# Problemas 5 y 6: reglas que se revisan ANTES de cambiar (E5).
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def retirar(self, monto):
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo = self._saldo - monto

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("Monto inválido")
        self._saldo = self._saldo + monto


cuenta = Cuenta(100)
cuenta.retirar(30)
print("P5:", cuenta.saldo)                         # 70
try:
    cuenta.retirar(500)
except ValueError as error:
    print("P5:", error, "| saldo:", cuenta.saldo)  # Saldo insuficiente | saldo: 70

try:
    cuenta.depositar(-10)
except ValueError as error:
    print("P6:", error, "| saldo:", cuenta.saldo)  # Monto inválido | saldo: 70


# Problema 7: un contador que SOLO sube: propiedad sin setter (P2).
class Contador:
    def __init__(self):
        self._valor = 0

    def incrementar(self):
        self._valor = self._valor + 1

    @property
    def valor(self):
        return self._valor


c = Contador()
c.incrementar()
c.incrementar()
c.incrementar()
print("P7:", c.valor)                              # 3
try:
    c.valor = 10
except AttributeError as error:
    print("P7:", error)


# Problema 8: setter con validación (P4).
class Termometro:
    def __init__(self, celsius):
        self.celsius = celsius                     # pasa por el setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Bajo el cero absoluto")
        self._celsius = valor


t = Termometro(20)
t.celsius = 25
print("P8:", t.celsius)                            # 25
try:
    t.celsius = -300
except ValueError as error:
    print("P8:", error, "| sigue en:", t.celsius)  # Bajo el cero absoluto | sigue en: 25
