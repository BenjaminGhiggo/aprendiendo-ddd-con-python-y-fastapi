# Ej3 — BUENA: el valor es privado; solo sube con incrementar().
class Contador:
    def __init__(self):
        self._valor = 0
    def valor(self):
        return self._valor
    def incrementar(self):
        self._valor = self._valor + 1

c = Contador()
c.incrementar()
c.incrementar()
print(c.valor())
