# Ej2 — BUENA: cada responsabilidad en su función (validar, convertir, formatear).
def es_numero(texto):
    return texto.isdigit()

def mensaje_edad(edad):
    return "Tienes " + str(edad) + " años"

entrada = "30"
if es_numero(entrada):
    print(mensaje_edad(int(entrada)))
else:
    print("Edad inválida")
