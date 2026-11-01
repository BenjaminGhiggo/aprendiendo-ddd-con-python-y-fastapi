# BUENA: ante un error devuelve el codigo HTTP adecuado (400).
def endpoint(sku):
    if sku not in ("MESA", "SILLA"):
        return (400, "sku invalido")
    return (201, "asignado")
print(endpoint("XXX"))
