# Ej1 — MALA (funciona): un if por cada tipo para calcular el área.
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

class Circulo:
    def __init__(self, radio):
        self.radio = radio

def area(figura):
    if isinstance(figura, Cuadrado):
        return figura.lado * figura.lado
    elif isinstance(figura, Circulo):
        return 3.14 * figura.radio * figura.radio

print(area(Cuadrado(4)))
print(area(Circulo(3)))
