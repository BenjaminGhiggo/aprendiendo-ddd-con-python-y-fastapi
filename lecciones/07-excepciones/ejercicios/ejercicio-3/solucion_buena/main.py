# Ej3 — BUENA: la función lanza la excepción; es imposible ignorar el error.
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as e:
    print(e)
