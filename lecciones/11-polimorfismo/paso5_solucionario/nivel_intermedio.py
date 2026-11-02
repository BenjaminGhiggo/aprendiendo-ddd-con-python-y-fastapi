# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/11-polimorfismo/paso5_solucionario/nivel_intermedio.py


class Perro:
    def sonido(self):
        return "Guau"


class Gato:
    def sonido(self):
        return "Miau"


class Vaca:
    def sonido(self):
        return "Muu"


# Problema 5: una función que no pregunta el tipo y junta los resultados (P3).
def hacer_sonar(animales):
    sonidos = []
    for animal in animales:
        sonidos.append(animal.sonido())
    return sonidos


print("P5:", hacer_sonar([Perro(), Gato(), Vaca()]))   # ['Guau', 'Miau', 'Muu']


# Problema 6: métodos de pago con la misma interfaz pagar(monto).
class Efectivo:
    def pagar(self, monto):
        return f"Pagó {monto} en efectivo"


class Tarjeta:
    def pagar(self, monto):
        comision = monto * 0.03
        return f"Pagó {monto} con tarjeta (comisión {comision})"


class Transferencia:
    def pagar(self, monto):
        return f"Pagó {monto} por transferencia"


def procesar(metodo, monto):
    return metodo.pagar(monto)


for metodo in [Efectivo(), Tarjeta(), Transferencia()]:
    print("P6:", procesar(metodo, 100))


# Problema 7: duck typing con clases que no tienen nada que ver (P6).
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

    def describir(self):
        return f"Libro: {self.titulo}"


class Pelicula:
    def __init__(self, titulo):
        self.titulo = titulo

    def describir(self):
        return f"Película: {self.titulo}"


def describir_todo(cosas):
    for cosa in cosas:
        print("P7:", cosa.describir())


describir_todo([Libro("Cien años de soledad"), Pelicula("Coco")])

# Problema 8: con hasattr saltamos a quien NO cumple el contrato (C5).
for cosa in [Libro("Rayuela"), 42, Pelicula("Up")]:
    if hasattr(cosa, "describir"):
        print("P8:", cosa.describir())
    else:
        print("P8:", cosa, "no sabe describirse")
