# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/06-clases-y-objetos/paso5_solucionario/nivel_intermedio.py


# Problemas 5 y 6: métodos que CAMBIAN el estado (C9), uno de ellos devolviendo True/False.
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo = self.saldo + monto

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            return True
        return False


cuenta = Cuenta(100)
cuenta.depositar(50)
print("P5:", cuenta.saldo)                               # 150

print("P6:", cuenta.retirar(30), cuenta.saldo)          # True 120
print("P6:", cuenta.retirar(500), cuenta.saldo)         # False 120


# Problema 7: objetos dentro de una lista y recorrerlos (C14).
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


productos = [Producto("pan", 1), Producto("leche", 4), Producto("queso", 9)]
total = 0
for p in productos:
    print("P7:", p.nombre, p.precio)
    total = total + p.precio
print("P7: total", total)                               # 14

# Problema 8: isinstance (C12).
print("P8:", isinstance(productos[0], Producto), isinstance("pan", Producto))   # True False
