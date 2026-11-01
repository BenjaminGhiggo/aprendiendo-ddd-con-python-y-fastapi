# MALA: todo mezclado; no se ve que cambia estado y que solo lee.
datos = {}
def manejar(accion, clave, valor=None):
    if accion == "guardar":
        datos[clave] = valor        # escribe
    return datos.get(clave)         # y lee, siempre
manejar("guardar", "a", 1)
print("mala:", manejar("leer", "a"))
