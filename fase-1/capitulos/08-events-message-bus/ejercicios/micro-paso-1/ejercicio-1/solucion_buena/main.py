# BUENA: el dominio REGISTRA un evento; otro decide qué hacer.
from dataclasses import dataclass
@dataclass
class SinStock: sku: str
class Producto:
    def __init__(self, sku): self.sku=sku; self.eventos=[]
    def asignar(self, hay_stock):
        if not hay_stock:
            self.eventos.append(SinStock(self.sku))
p = Producto("MESA"); p.asignar(False); print(p.eventos)
