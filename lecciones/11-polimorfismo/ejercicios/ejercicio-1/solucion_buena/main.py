# Ej1 — BUENA: cada figura sabe calcular su propia área (polimorfismo).
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio * self.radio

for figura in [Cuadrado(4), Circulo(3)]:
    print(figura.area())
