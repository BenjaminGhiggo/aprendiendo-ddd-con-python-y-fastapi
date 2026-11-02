# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/07-excepciones/paso5_solucionario/nivel_basico.py

# Problema 1: atrapar el ValueError de int() (X12).
try:
    int("abc")
except ValueError:
    print("P1: no es un número")


# Problema 2: atrapar la división entre cero (X11).
def dividir(a, b):
    return a / b


try:
    dividir(10, 0)
except ZeroDivisionError:
    print("P2: no se puede dividir entre 0")


# Problema 3: lanzar un error con mensaje y leerlo con "as e" (X1 + X3).
def validar_edad(edad):
    if edad < 0:
        raise ValueError("edad negativa")
    return edad


try:
    validar_edad(-5)
except ValueError as e:
    print("P3:", e)

# Problema 4: atrapar el KeyError de un diccionario (X9).
stock = {"mesa": 10}
try:
    stock["cama"]
except KeyError:
    print("P4: no existe cama")
