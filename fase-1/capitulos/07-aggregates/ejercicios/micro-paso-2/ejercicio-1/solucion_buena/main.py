# BUENA: el repositorio guarda y busca el AGREGADO (Producto) por su sku.
class Producto:
    def __init__(self, sku, lotes): self.sku=sku; self.lotes=lotes
class RepoProductos:
    def __init__(self): self._productos=[]
    def agregar(self, p): self._productos.append(p)
    def obtener(self, sku): return next(p for p in self._productos if p.sku==sku)
r = RepoProductos(); r.agregar(Producto("MESA", [{"ref":"l1"}])); print(r.obtener("MESA").sku)
