# Ej2 — MALA (funciona): si no hay stock, devuelve None (fácil de ignorar).
class Lote:
    def __init__(self, ref, disponible):
        self.ref = ref
        self.disponible = disponible

def asignar(cantidad, lotes):
    for lote in lotes:
        if lote.disponible >= cantidad:
            lote.disponible -= cantidad
            return lote.ref
    return None

ref = asignar(100, [Lote("A", 10)])
print("asignado a:", ref)        # None: el programa sigue como si nada
