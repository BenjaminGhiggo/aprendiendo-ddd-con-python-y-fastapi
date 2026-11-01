# MALA: el servicio recibe un objeto de dominio -> el test debe construirlo.
class LineaPedido:
    def __init__(self, sku, cantidad): self.sku=sku; self.cantidad=cantidad
def servicio(linea, lotes):
    return any(l == linea.sku for l in lotes)
print(servicio(LineaPedido("MESA", 2), ["MESA"]))
