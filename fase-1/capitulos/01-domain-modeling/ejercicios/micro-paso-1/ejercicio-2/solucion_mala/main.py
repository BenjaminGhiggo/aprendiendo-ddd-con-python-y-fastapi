# Ej2 — MALA (funciona): el sku y la cantidad viajan sueltos por todas las funciones.
def describir(sku, cantidad):
    return "Pedido de " + str(cantidad) + " x " + sku

def es_grande(sku, cantidad):
    return cantidad >= 100

print(describir("MESA", 2))
print(es_grande("MESA", 2))
