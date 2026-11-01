# polimorfismo.py

# Dos clases distintas, cada una con un método con el MISMO nombre: area().
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

# Esta función no pregunta "¿qué tipo eres?". Solo exige que tengas area().
# (Eso es "duck typing": si sabe hacer area(), sirve.)
def mostrar_areas(figuras):
    for figura in figuras:
        print(figura.area())

mostrar_areas([Cuadrado(4), Circulo(3)])
