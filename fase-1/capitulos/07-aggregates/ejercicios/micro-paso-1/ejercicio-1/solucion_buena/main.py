# BUENA: el agregado Producto es la unica puerta para asignar.
class Producto:
    def __init__(self, sku, lotes): self.sku=sku; self.lotes=lotes; self.version=0
    def asignar(self, cantidad):
        for l in self.lotes:
            if l["disp"] >= cantidad:
                l["disp"] -= cantidad
                self.version += 1
                return l["ref"]
p = Producto("MESA", [{"ref": "l1", "disp": 100}])
print(p.asignar(10), "version", p.version)
