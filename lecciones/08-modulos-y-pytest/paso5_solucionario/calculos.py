# calculos.py — módulo de apoyo de los problemas 1–9 (README §10).


def doble(n):
    return n * 2


def es_par(n):
    return n % 2 == 0


def dividir(a, b):
    return a / b


def total(precio, cantidad, descuento=0):
    return precio * cantidad - descuento


# Problema 8: este bloque SOLO corre al ejecutar calculos.py directamente,
# no cuando otro archivo lo importa.
if __name__ == "__main__":
    print("probando calculos")
