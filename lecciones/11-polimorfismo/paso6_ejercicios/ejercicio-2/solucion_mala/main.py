# Ej2 — MALA (funciona): elige el sonido con if según un campo "tipo".
class Animal:
    def __init__(self, tipo):
        self.tipo = tipo

def sonido(animal):
    if animal.tipo == "perro":
        return "Guau"
    elif animal.tipo == "gato":
        return "Miau"

print(sonido(Animal("perro")))
print(sonido(Animal("gato")))
