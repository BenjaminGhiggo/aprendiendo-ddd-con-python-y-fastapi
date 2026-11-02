# Ej2 — MALA (funciona): un except GENÉRICO atrapa cualquier error y lo oculta.
def convertir_a_entero(texto):
    try:
        return int(texto)
    except:                    # atrapa TODO, incluso errores que no esperábamos
        return 0

print(convertir_a_entero("42"))
print(convertir_a_entero("hola"))
