# Ej1 — BUENA: lo común vive en Animal; Perro y Gato heredan.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def describir(self):
        return self.nombre + " es un animal"

class Perro(Animal):
    pass

class Gato(Animal):
    pass

print(Perro("Fido").describir())
print(Gato("Michi").describir())
