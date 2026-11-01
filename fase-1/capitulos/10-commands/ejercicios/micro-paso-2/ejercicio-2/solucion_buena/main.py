# BUENA: el error de un comando PROPAGA (la API puede devolver 400).
def handler_comando(c): raise ValueError("sku invalido")
def manejar_comando(c):
    return handler_comando(c)   # propaga
try:
    manejar_comando("Asignar")
except ValueError as e:
    print("error propagado:", e)
