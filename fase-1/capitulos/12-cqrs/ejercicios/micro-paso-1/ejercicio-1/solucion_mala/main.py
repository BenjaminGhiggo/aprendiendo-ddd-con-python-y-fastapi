# MALA: la función ESCRIBE y además DEVUELVE lo que escribió (viola CQS).
stock = {"MESA": 10}
def asignar(sku, cantidad):
    stock[sku] -= cantidad          # cambia estado
    return stock[sku]               # ...y además responde: dos cosas a la vez
restante = asignar("MESA", 3)
print("mala -> asignar devolvio:", restante, "| stock:", stock)
