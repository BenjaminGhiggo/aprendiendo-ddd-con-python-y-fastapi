# Ej2 — BUENA: el núcleo recibe sus entradas por parámetro (puro y testeable).
def sin_stock(inventario):
    return [sku for sku, cant in inventario.items() if cant == 0]

print(sin_stock({"MESA": 2, "SILLA": 0}))
