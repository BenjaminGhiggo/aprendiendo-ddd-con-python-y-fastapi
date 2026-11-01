# Ej3 — BUENA: __eq__ y __hash__ por referencia; el set lo cuenta una vez.
class Lote:
    def __init__(self, referencia, stock):
        self.referencia = referencia
        self.stock = stock
    def __eq__(self, other):
        return isinstance(other, Lote) and other.referencia == self.referencia
    def __hash__(self):
        return hash(self.referencia)

lotes = {Lote("L1", 20), Lote("L1", 5)}
print(len(lotes))     # 1
