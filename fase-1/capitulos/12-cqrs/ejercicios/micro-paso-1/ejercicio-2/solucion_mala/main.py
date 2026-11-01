# MALA: el POST responde con los datos; "recargar" = reenviar el POST = asignar de nuevo.
pedidos = []
def post_asignar(pedido):
    pedidos.append(pedido)          # escribe
    return list(pedidos)            # devuelve datos tras un write
print("POST:", post_asignar("p1"))
print("RECARGA (reenvia POST):", post_asignar("p1"))   # se duplica
