# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10, Lección 14 · OCP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/14-ocp/paso5_solucionario/nivel_intermedio.py


# Problema 5: impuesto por país: del if/elif a un registro; agregar Chile (19 %).
def igv_peru(monto):
    return monto * 18 / 100


def iva_mexico(monto):
    return monto * 16 / 100


IMPUESTOS = {"PE": igv_peru, "MX": iva_mexico}


def impuesto(pais, monto):                  # núcleo: no cambia
    return IMPUESTOS[pais](monto)


def iva_chile(monto):
    return monto * 19 / 100


IMPUESTOS["CL"] = iva_chile
print("P5:", impuesto("PE", 100), impuesto("MX", 100), impuesto("CL", 100))   # 18.0 16.0 19.0


# Problema 6: figuras con polimorfismo; agregar Triangulo sin tocar area_total (receta O2).
class Figura:
    def area(self):
        return 0


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


def area_total(figuras):                    # núcleo: no cambia
    total = 0
    for figura in figuras:
        total = total + figura.area()
    return total


class Triangulo(Figura):                    # NUEVO
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


print("P6:", area_total([Rectangulo(2, 3), Cuadrado(4), Triangulo(6, 2)]))   # 6 + 16 + 6.0 = 28.0


# Problema 7: lista de validaciones; agregar sin_espacios con append (receta O4).
def no_vacio(texto):
    return texto != ""


def max_10(texto):
    return len(texto) <= 10


VALIDACIONES = [no_vacio, max_10]


def es_valido(texto):
    for regla in VALIDACIONES:
        if not regla(texto):
            return False
    return True


def sin_espacios(texto):
    return " " not in texto


VALIDACIONES.append(sin_espacios)
print("P7:", es_valido("ana"), es_valido("ana lopez"))   # True False


# Problema 8: encontrar el error. precio_final(100, descuento_10()) LLAMA a la función
# en vez de PASARLA. Mensaje real:
def descuento_10(precio):
    return precio * 0.9


def precio_final(precio, regla):
    return regla(precio)


try:
    precio_final(100, descuento_10(100))
except TypeError as error:
    print("P8: error ->", error)
print("P8: corregido ->", precio_final(100, descuento_10))   # 90.0 (sin paréntesis)
