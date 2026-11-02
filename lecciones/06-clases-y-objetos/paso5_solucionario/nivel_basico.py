# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/06-clases-y-objetos/paso5_solucionario/nivel_basico.py


# Problema 1: clase con un atributo, una instancia y leer el dato (C1–C5).
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre


firulais = Perro("Firulais")
print("P1:", firulais.nombre)                    # Firulais


# Problema 2: un método que calcula con los datos del objeto (C7 + C8).
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


print("P2:", Rectangulo(3, 4).area())            # 12


# Problema 3: dos instancias de la misma clase, cada una con sus datos (C10).
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


lapiz = Producto("lápiz", 2)
cuaderno = Producto("cuaderno", 8)
print("P3:", lapiz.precio, cuaderno.precio)      # 2 8

# Problema 4: cambiar un atributo desde afuera (C6).
lapiz.precio = 3
print("P4:", lapiz.precio)                       # 3
