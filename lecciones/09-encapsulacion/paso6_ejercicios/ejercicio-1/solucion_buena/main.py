# Ej1 — BUENA: dato privado; solo se cambia por un método que respeta la regla.
class Lote:
    def __init__(self, cantidad):
        self._cantidad = cantidad
    def cantidad_disponible(self):
        return self._cantidad
    def asignar(self, pedido):
        if pedido > self._cantidad:
            raise ValueError("No hay stock suficiente")
        self._cantidad = self._cantidad - pedido

lote = Lote(20)
lote.asignar(5)
print(lote.cantidad_disponible())
