# Ej3 — BUENA: puede_asignar comprueba sku Y cantidad.
class Lote:
    def __init__(self, sku, cantidad):
        self.sku = sku
        self.disponible = cantidad
    def puede_asignar(self, sku_linea, cantidad_linea):
        return self.sku == sku_linea and self.disponible >= cantidad_linea

lote = Lote("MESA", 20)
print(lote.puede_asignar("TOSTADORA", 2))   # False
print(lote.puede_asignar("MESA", 2))        # True
