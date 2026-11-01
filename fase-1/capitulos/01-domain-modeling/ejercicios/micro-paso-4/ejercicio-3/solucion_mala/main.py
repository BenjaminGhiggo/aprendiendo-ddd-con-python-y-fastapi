# Ej3 — MALA (funciona): asigna en el ORDEN recibido; puede usar un envío antes
# que el stock que ya está en almacén.
class Lote:
    def __init__(self, ref, disponible):
        self.ref = ref
        self.disponible = disponible

def asignar(cantidad, lotes):
    for lote in lotes:
        if lote.disponible >= cantidad:
            lote.disponible -= cantidad
            return lote.ref

envio = Lote("envio", 100)       # llega en el futuro
almacen = Lote("almacen", 100)   # ya está aquí
print(asignar(10, [envio, almacen]))   # "envio" -> MAL: debería usar el almacén
