# BUENA: el servicio recibe PRIMITIVOS; arma el objeto adentro. Tests sin dominio.
class LineaPedido:
    def __init__(self, sku, cantidad): self.sku=sku; self.cantidad=cantidad
def servicio(sku, cantidad, lotes):
    linea = LineaPedido(sku, cantidad)
    return any(l == linea.sku for l in lotes)
print(servicio("MESA", 2, ["MESA"]))
