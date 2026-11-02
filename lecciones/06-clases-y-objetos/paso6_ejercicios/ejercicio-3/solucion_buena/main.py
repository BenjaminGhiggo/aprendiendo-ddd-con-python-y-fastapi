# Ej3 — BUENA: los datos viven en el objeto; los métodos ya los conocen (self).
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad
    def descripcion(self):
        return "Lote " + self.referencia + " con " + str(self.cantidad)
    def esta_vacio(self):
        return self.cantidad == 0

lote = Lote("LOTE-001", 20)
print(lote.descripcion())
print(lote.esta_vacio())
