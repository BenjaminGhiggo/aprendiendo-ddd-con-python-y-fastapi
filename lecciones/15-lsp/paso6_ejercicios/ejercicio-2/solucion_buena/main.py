# Ej2 — BUENA: no forzamos herencia que rompe; cada forma es su propia clase.
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return self.ancho * self.alto

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

# Ambas tienen area(); se usan por su interfaz común, sin sustituciones que engañen.
for figura in [Rectangulo(2, 3), Cuadrado(3)]:
    print(figura.area())
