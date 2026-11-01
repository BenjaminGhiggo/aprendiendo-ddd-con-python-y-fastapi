# Ej3 — MALA (funciona): para "extender" un saludo, reescribe el método entero.
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludo(self):
        return "Hola, soy " + self.nombre

class Gerente(Empleado):
    def saludo(self):
        return "Hola, soy " + self.nombre + " y soy gerente"  # repite el saludo base

print(Gerente("Ana").saludo())
