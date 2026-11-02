# Ej1 — BUENA: un objeto agrupa los datos de un lote.
class Lote:
    def __init__(self, referencia, sku, cantidad):
        self.referencia = referencia
        self.sku = sku
        self.cantidad = cantidad

lote = Lote("LOTE-001", "MESA", 20)
print(lote.referencia, lote.sku, lote.cantidad)
