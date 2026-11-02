# Ej3 — MALA (funciona): elige el saludo del día con un if gigante.
def saludo(dia):
    if dia == "lunes":
        return "¡Ánimo, es lunes!"
    elif dia == "viernes":
        return "¡Por fin viernes!"
    else:
        return "Hola"

print(saludo("lunes"))
print(saludo("viernes"))
print(saludo("martes"))
