# BUENA: la regla vive en el dominio; el servicio solo coordina.
class Lote:
    def __init__(self, disponible): self.disponible = disponible
    def puede_asignar(self, pedido): return self.disponible >= pedido
def servicio(lote, pedido):
    if lote.puede_asignar(pedido):
        return "asignado"
    return "sin stock"
print(servicio(Lote(100), 10))
