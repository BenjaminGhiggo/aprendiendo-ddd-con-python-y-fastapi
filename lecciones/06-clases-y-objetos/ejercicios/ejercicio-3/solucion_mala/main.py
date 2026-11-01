# Ej3 — MALA (funciona): dos funciones que reciben los mismos datos una y otra vez.
def descripcion(referencia, cantidad):
    return "Lote " + referencia + " con " + str(cantidad)

def esta_vacio(referencia, cantidad):
    return cantidad == 0

print(descripcion("LOTE-001", 20))
print(esta_vacio("LOTE-001", 20))
