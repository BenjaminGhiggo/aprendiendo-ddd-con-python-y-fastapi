# Ej2 — BUENA: una ENTIDAD compara por su identidad (la referencia).
class Lote:
    def __init__(self, referencia, stock):
        self.referencia = referencia
        self.stock = stock
    def __eq__(self, other):
        if not isinstance(other, Lote):
            return False
        return other.referencia == self.referencia
    def __hash__(self):
        return hash(self.referencia)

a = Lote("L1", 20)
b = Lote("L1", 5)
print(a == b)         # True
