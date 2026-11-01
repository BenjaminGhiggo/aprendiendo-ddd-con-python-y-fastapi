# Ej3 — MALA: clase normal; dos líneas con los mismos datos cuentan DOBLE en un set.
class Linea:
    def __init__(self, sku, cantidad):
        self.sku = sku
        self.cantidad = cantidad

lineas = {Linea("MESA", 2), Linea("MESA", 2)}   # objetos distintos
print(len(lineas))   # 2 -> MAL (deberian ser la misma linea)
