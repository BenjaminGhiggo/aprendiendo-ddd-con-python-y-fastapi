# Ej3 — BUENA: __gt__ hace que sorted() ponga el stock en almacén (sin eta) primero.
class Lote:
    def __init__(self, ref, eta, disponible):
        self.ref = ref
        self.eta = eta            # None = ya en almacén
        self.disponible = disponible
    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

def asignar(cantidad, lotes):
    for lote in sorted(lotes):
        if lote.disponible >= cantidad:
            lote.disponible -= cantidad
            return lote.ref

envio = Lote("envio", 1, 100)       # eta=1 (futuro)
almacen = Lote("almacen", None, 100)
print(asignar(10, [envio, almacen]))   # "almacen"
