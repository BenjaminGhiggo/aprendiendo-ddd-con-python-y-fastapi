# MALA: una función "endpoint" hace TODO (buscar, validar, asignar).
LOTES = [("L1", "MESA", 100)]
def endpoint(sku, cantidad):
    disponibles = [l for l in LOTES if l[1] == sku]
    if not disponibles:
        return "error: sku invalido"
    return disponibles[0][0]
print(endpoint("MESA", 10))
