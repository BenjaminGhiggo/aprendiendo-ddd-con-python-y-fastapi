# Ej1 — MALA (funciona): dos clases casi idénticas, con el código duplicado.
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    def describir(self):
        return self.nombre + " es un animal"

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
    def describir(self):
        return self.nombre + " es un animal"

print(Perro("Fido").describir())
print(Gato("Michi").describir())
