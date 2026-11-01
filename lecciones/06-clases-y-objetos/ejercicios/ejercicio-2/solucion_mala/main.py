# Ej2 — MALA (funciona): el lote es un dict y la regla vive en una función aparte.
lote = {"cantidad": 20}

def puede_asignar(lote, pedido):
    return lote["cantidad"] >= pedido

print(puede_asignar(lote, 5))   # hay que pasar el dict y recordar la clave exacta
