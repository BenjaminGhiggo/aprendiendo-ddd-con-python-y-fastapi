# paso1_formulas.py — PASO 1 de la Lección 11 (Polimorfismo).
# Cada bloque es una "fórmula" de las tablas del README (§5 y §6), con su código (P1, C1...).
# Ejecuta:  uv run python lecciones/11-polimorfismo/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.


# Tres clases DISTINTAS (no heredan entre sí), con métodos del MISMO nombre: area() y nombre().
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def nombre(self):
        return "cuadrado"


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        # round(x, 2) redondea a 2 decimales: los decimales de la computadora no son
        # exactos (3.14 * 3 * 3 da 28.259999999999998), así mostramos 28.26.
        return round(3.14 * self.radio * self.radio, 2)

    def nombre(self):
        return "círculo"


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def nombre(self):
        return "rectángulo"


# Esta función NO pregunta "¿qué tipo eres?": solo exige que cada figura tenga area().
def total_areas(figuras):
    total = 0
    for figura in figuras:
        total = total + figura.area()
    return round(total, 2)


print("========== POLIMORFISMO ==========")
print("P1  Cuadrado(4).area():   ", Cuadrado(4).area())
print("P1  Circulo(3).area():    ", Circulo(3).area())

print("P2  recorrer sin preguntar el tipo:")
for figura in [Cuadrado(4), Circulo(3)]:
    print("      ->", figura.nombre(), figura.area())

print("P3  total_areas([Cuadrado(4), Circulo(3)]):               ", total_areas([Cuadrado(4), Circulo(3)]))
print("P4  ...agregando Rectangulo(2, 3) SIN tocar la función:   ",
      total_areas([Cuadrado(4), Circulo(3), Rectangulo(2, 3)]))


# P5 · polimorfismo CON herencia: cada hija sobrescribe el mismo método (Lección 10).
class Animal:
    def sonido(self):
        return "..."


class Perro(Animal):
    def sonido(self):
        return "Guau"


class Gato(Animal):
    def sonido(self):
        return "Miau"


sonidos = []
for animal in [Perro(), Gato(), Animal()]:
    sonidos.append(animal.sonido())
print("P5  sonidos con herencia: ", sonidos)


# P6 · DUCK TYPING: clases SIN ningún parentesco; basta con tener el método.
#      "Si camina como pato y hace cuac como pato, es un pato."
class Pato:
    def hablar(self):
        return "Cuac"


class Robot:
    def hablar(self):
        return "Bip"


print("P6  duck typing:          ", Pato().hablar(), "|", Robot().hablar())

# P7 · Python mismo es polimórfico: len() funciona con textos, listas y diccionarios.
print("P7  len:                  ", len("mesa"), len([1, 2]), len({"a": 1}))

# P8 · ...y "+" hace cosas distintas según el tipo.
print("P8  +:                    ", 2 + 3, "a" + "b", [1] + [2])

print()
print("========== EL CONTRATO IMPLÍCITO (DUCK TYPING) ==========")
# C1 · lo único que se exige es TENER el método. hasattr(obj, "nombre") lo pregunta.
print("C1  hasattr(Cuadrado(1), 'area'):", hasattr(Cuadrado(1), "area"))
print("C1  hasattr(Pato(), 'area'):     ", hasattr(Pato(), "area"))


# C2 · si el método se llama distinto, no cumple el contrato.
class TrianguloMalo:
    def calcular_area(self):
        return 6


try:
    total_areas([TrianguloMalo()])
except AttributeError as error:
    print("C2  nombre distinto:             ", error)


# C3 · si pide otros argumentos, tampoco cumple.
class TrianguloConUnidades:
    def area(self, unidades):
        return 6


try:
    total_areas([TrianguloConUnidades()])
except TypeError as error:
    print("C3  argumentos distintos:        ", error)


# C4 · si no devuelve un número (olvidó el return), la suma falla.
class TrianguloSinReturn:
    def area(self):
        6 * 1


try:
    total_areas([TrianguloSinReturn()])
except TypeError as error:
    print("C4  sin return:                  ", error)

# C5 · con hasattr podemos saltar a quien no cumple, en vez de reventar.
for cosa in [Cuadrado(2), Pato(), Circulo(1)]:
    if hasattr(cosa, "area"):
        print("C5  ", type(cosa).__name__, "->", cosa.area())
    else:
        print("C5  ", type(cosa).__name__, "-> no sabe calcular su área")
