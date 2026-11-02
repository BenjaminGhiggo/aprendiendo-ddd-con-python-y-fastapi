# Ej1 — BUENA: Pedido solo calcula; recibo y guardado son responsabilidades aparte.
class Pedido:
    def __init__(self, precios):
        self.precios = precios
    def total(self):
        return sum(self.precios)

def imprimir_recibo(pedido):
    print("Total: " + str(pedido.total()))

def guardar(pedido):
    print("(guardando en la base de datos...)")

p = Pedido([10, 20, 30])
imprimir_recibo(p)
guardar(p)
