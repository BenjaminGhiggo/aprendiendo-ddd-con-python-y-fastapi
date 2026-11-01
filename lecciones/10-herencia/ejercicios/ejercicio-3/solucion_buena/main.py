# Ej3 — BUENA: super().saludo() reutiliza el saludo del padre y le añade lo nuevo.
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludo(self):
        return "Hola, soy " + self.nombre

class Gerente(Empleado):
    def saludo(self):
        return super().saludo() + " y soy gerente"

print(Gerente("Ana").saludo())
