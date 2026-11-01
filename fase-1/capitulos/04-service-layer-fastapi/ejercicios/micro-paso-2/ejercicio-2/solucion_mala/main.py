# MALA: ante un error, responde 200 con un texto (el cliente no distingue).
def endpoint(sku):
    if sku not in ("MESA", "SILLA"):
        return (200, "error: sku invalido")   # codigo de exito con mensaje de error
    return (201, "asignado")
print(endpoint("XXX"))
