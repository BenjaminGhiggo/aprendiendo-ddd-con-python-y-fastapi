# MALA: el servicio A LLAMA directo al servicio B (acoplado; si B cae, A falla).
def servicio_b(dato): print("B procesa", dato)
def servicio_a():
    servicio_b("pedido")        # llamada sincrona directa
servicio_a()
