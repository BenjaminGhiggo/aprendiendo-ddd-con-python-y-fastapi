# BUENA: la regla vive dentro del agregado; no se puede violar desde afuera.
class SinStock(Exception): pass
class Producto:
    def __init__(self): self._stock=5
    def asignar(self, c):
        if c > self._stock: raise SinStock()
        self._stock -= c
p = Producto()
try: p.asignar(10)
except SinStock: print("bloqueado")
