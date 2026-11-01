# BUENA: el endpoint es fino: traduce entrada y delega en el servicio.
def servicio(sku, cantidad, lotes):
    total = sum(c for s, c in lotes if s == sku)
    return total >= cantidad
def endpoint(sku, cantidad, lotes):
    return "ok" if servicio(sku, cantidad, lotes) else "sin stock"
print(endpoint("MESA", 10, [("MESA", 100)]))
