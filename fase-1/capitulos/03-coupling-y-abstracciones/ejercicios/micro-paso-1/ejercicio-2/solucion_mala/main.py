# Ej2 — MALA: el núcleo lee del "mundo" (aquí una variable global) en vez de recibirlo.
INVENTARIO = {"MESA": 2, "SILLA": 0}
def sin_stock():
    return [sku for sku, cant in INVENTARIO.items() if cant == 0]   # depende del global

print(sin_stock())
