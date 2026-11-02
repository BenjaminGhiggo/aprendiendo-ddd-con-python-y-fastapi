# Ej1 — BUENA: el error se señala con una excepción con nombre.
class SinStock(Exception):
    pass

def asignar(disponible, pedido):
    if pedido > disponible:
        raise SinStock("No hay stock suficiente")
    return disponible - pedido

try:
    resto = asignar(10, 25)
    print("Quedan:", resto)
except SinStock as e:
    print("Hubo un problema:", e)
