# Ej2 — BUENA: la clase junta el dato y la regla como un método.
class Lote:
    def __init__(self, cantidad):
        self.cantidad = cantidad
    def puede_asignar(self, pedido):
        return self.cantidad >= pedido

lote = Lote(20)
print(lote.puede_asignar(5))
