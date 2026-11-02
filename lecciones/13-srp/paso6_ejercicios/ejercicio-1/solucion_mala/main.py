# Ej1 — MALA (funciona): Pedido calcula, formatea y "guarda": tres razones de cambio.
class Pedido:
    def __init__(self, precios):
        self.precios = precios
    def total(self):
        return sum(self.precios)
    def imprimir_recibo(self):
        print("Total: " + str(self.total()))
    def guardar(self):
        print("(guardando en la base de datos...)")

p = Pedido([10, 20, 30])
p.imprimir_recibo()
p.guardar()
