# Ej2 — MALA (funciona): una función valida, calcula y formatea, todo junto.
def procesar_edad(texto):
    if not texto.isdigit():
        return "Edad inválida"
    edad = int(texto)
    return "Tienes " + str(edad) + " años"

print(procesar_edad("30"))
print(procesar_edad("abc"))
