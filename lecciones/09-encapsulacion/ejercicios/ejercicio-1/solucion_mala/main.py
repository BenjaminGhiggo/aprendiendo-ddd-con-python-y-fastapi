# Ej1 — MALA (funciona): la cantidad es pública; cualquiera la deja inválida.
class Lote:
    def __init__(self, cantidad):
        self.cantidad = cantidad

lote = Lote(20)
lote.cantidad = -999   # nada lo impide: el lote queda en un estado imposible
print(lote.cantidad)
