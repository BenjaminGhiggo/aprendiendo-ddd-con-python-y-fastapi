# BUENA: el repositorio rastrea 'vistos' para recoger sus eventos.
class Repo:
    def __init__(self): self.datos={"MESA":["evento1"]}; self.vistos=set()
    def obtener(self, sku): self.vistos.add(sku); return self.datos[sku]
r = Repo(); r.obtener("MESA"); print("vistos:", r.vistos)
