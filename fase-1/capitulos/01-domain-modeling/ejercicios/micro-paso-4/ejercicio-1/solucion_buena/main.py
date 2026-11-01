# Ej1 — BUENA: "elegir entre varios lotes" es una FUNCIÓN de dominio.
class Lote:
    def __init__(self, ref, disponible):
        self.ref = ref
        self.disponible = disponible

def asignar(cantidad, lotes):
    for lote in lotes:
        if lote.disponible >= cantidad:
            lote.disponible -= cantidad
            return lote.ref

a = Lote("A", 0)
b = Lote("B", 10)
print(asignar(5, [a, b]))        # "B"
