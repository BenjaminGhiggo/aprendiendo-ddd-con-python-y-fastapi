# Ej2 — BUENA: cada animal define su propio sonido(); sin if por tipo.
class Perro:
    def sonido(self):
        return "Guau"

class Gato:
    def sonido(self):
        return "Miau"

for animal in [Perro(), Gato()]:
    print(animal.sonido())
