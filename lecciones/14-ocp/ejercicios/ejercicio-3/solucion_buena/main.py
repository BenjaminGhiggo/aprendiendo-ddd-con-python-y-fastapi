# Ej3 — BUENA: un diccionario de saludos; agregar uno no toca el código.
SALUDOS = {
    "lunes": "¡Ánimo, es lunes!",
    "viernes": "¡Por fin viernes!",
}

def saludo(dia):
    return SALUDOS.get(dia, "Hola")

print(saludo("lunes"))
print(saludo("viernes"))
print(saludo("martes"))
