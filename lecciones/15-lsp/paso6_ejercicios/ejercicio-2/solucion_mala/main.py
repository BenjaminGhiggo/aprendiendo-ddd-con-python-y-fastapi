# Ej2 — MALA: una subclase "rompe" lo que promete la base (rectángulo vs cuadrado).
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return self.ancho * self.alto

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    # Si alguien hace cuadrado.ancho = 5 esperando un rectángulo, el alto no cambia:
    # el Cuadrado NO se comporta como un Rectangulo sustituible.

def ensanchar_y_medir(rect):
    rect.ancho = 5            # espero que solo cambie el ancho
    return rect.area()

print(ensanchar_y_medir(Rectangulo(2, 3)))  # 5*3 = 15 (esperado)
print(ensanchar_y_medir(Cuadrado(3)))       # 5*3 = 15, pero era un "cuadrado": incoherente
