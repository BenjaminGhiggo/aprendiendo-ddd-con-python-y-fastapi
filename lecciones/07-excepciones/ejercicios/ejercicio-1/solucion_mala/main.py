# Ej1 — MALA (funciona): señala el error devolviendo -1 (un "valor mágico").
def asignar(disponible, pedido):
    if pedido > disponible:
        return -1          # ¿-1 es un error o un stock? quien llama tiene que adivinar
    return disponible - pedido

resto = asignar(10, 25)
if resto == -1:
    print("Hubo un problema")
else:
    print("Quedan:", resto)
