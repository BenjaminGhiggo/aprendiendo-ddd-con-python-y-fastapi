# Ej2 — BUENA: atrapa SOLO el error esperado (ValueError); el resto sale a la luz.
def convertir_a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return 0

print(convertir_a_entero("42"))
print(convertir_a_entero("hola"))
