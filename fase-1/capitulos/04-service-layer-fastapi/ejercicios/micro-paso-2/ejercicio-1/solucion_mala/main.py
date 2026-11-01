# MALA: el "endpoint" tiene lógica de negocio adentro.
def endpoint(sku, cantidad, lotes):
    total = sum(c for s, c in lotes if s == sku)   # calcula stock aqui mismo
    return "ok" if total >= cantidad else "sin stock"
print(endpoint("MESA", 10, [("MESA", 100)]))
