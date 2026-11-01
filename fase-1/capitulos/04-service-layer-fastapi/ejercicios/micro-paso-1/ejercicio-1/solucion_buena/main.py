# BUENA: la orquestación vive en un servicio; el endpoint solo delega.
def servicio_asignar(sku, cantidad, lotes):
    disponibles = [l for l in lotes if l[1] == sku]
    if not disponibles:
        raise ValueError(f"sku invalido {sku}")
    return disponibles[0][0]
def endpoint(sku, cantidad):
    return servicio_asignar(sku, cantidad, [("L1", "MESA", 100)])
print(endpoint("MESA", 10))
