# MALA: el servicio calcula la regla de negocio (si cabe) el mismo.
def servicio(disponible, pedido):
    if disponible >= pedido:     # regla de negocio metida en el servicio
        return "asignado"
    return "sin stock"
print(servicio(100, 10))
