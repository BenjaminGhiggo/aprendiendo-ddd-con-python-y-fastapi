# Ej1 — MALA (funciona): "disponible" es un número que se resta a mano.
class Lote:
    def __init__(self, cantidad):
        self.disponible = cantidad
    def asignar(self, cantidad_linea):
        self.disponible -= cantidad_linea

lote = Lote(20)
lote.asignar(2)
lote.asignar(2)        # la MISMA línea otra vez: resta igual (no lo sabe)
print(lote.disponible) # 16 -> MAL si era la misma línea
