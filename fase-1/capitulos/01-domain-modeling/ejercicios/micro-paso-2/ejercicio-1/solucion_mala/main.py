# Ej1 — MALA (funciona): sin dataclass, dos líneas iguales NO son ==.
class LineaPedido:
    def __init__(self, sku, cantidad):
        self.sku = sku
        self.cantidad = cantidad

print(LineaPedido("MESA", 2) == LineaPedido("MESA", 2))   # False
