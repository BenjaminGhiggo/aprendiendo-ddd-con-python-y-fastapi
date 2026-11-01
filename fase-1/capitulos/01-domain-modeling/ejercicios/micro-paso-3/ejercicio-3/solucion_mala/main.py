# Ej3 — MALA (funciona): puede_asignar solo mira la cantidad, ignora el sku.
class Lote:
    def __init__(self, sku, cantidad):
        self.sku = sku
        self.disponible = cantidad
    def puede_asignar(self, sku_linea, cantidad_linea):
        return self.disponible >= cantidad_linea   # ¡no compara sku!

lote = Lote("MESA", 20)
print(lote.puede_asignar("TOSTADORA", 2))   # True -> MAL (producto distinto)
