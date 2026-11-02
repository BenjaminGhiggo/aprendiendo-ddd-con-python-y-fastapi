# Ej3 — BUENA: cada medio de pago es una clase con pagar(); agregar uno no toca lo demás.
class Efectivo:
    def pagar(self, monto):
        return "Pagaste " + str(monto) + " en efectivo"

class Tarjeta:
    def pagar(self, monto):
        return "Pagaste " + str(monto) + " con tarjeta"

for metodo in [Efectivo(), Tarjeta()]:
    print(metodo.pagar(100))
