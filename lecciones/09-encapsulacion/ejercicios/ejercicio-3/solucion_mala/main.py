# Ej3 — MALA (funciona): un contador público que cualquiera puede poner en negativo.
class Contador:
    def __init__(self):
        self.valor = 0

c = Contador()
c.valor = -5           # un contador no debería poder ser negativo
print(c.valor)
