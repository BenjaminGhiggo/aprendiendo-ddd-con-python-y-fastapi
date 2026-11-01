# BUENA: se carga el AGREGADO y el cambio pasa por el (mantiene invariantes/version).
class Producto:
    def __init__(self, sku, lotes): self.sku=sku; self.lotes=lotes; self.version=0
    def asignar(self, c): self.lotes[0]["disp"] -= c; self.version += 1
p = Producto("MESA", [{"ref":"l1","disp":100}])
p.asignar(10)
print(p.lotes, "version", p.version)
