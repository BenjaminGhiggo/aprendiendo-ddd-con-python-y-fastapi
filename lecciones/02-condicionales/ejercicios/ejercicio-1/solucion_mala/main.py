# Ej1 — MALA (funciona): tres if separados, evalúa todos aunque uno ya acertó.
def clasificar(edad):
    resultado = ""
    if edad < 18:
        resultado = "menor"
    if edad >= 18 and edad < 65:
        resultado = "adulto"
    if edad >= 65:
        resultado = "adulto mayor"
    return resultado

print(clasificar(10))
print(clasificar(30))
print(clasificar(70))
