# Ej2 — BUENA: si no hay stock, lanza una excepción de dominio.
class SinStock(Exception):
    pass

class Lote:
    def __init__(self, ref, disponible):
        self.ref = ref
        self.disponible = disponible

def asignar(sku, cantidad, lotes):
    for lote in lotes:
        if lote.disponible >= cantidad:
            lote.disponible -= cantidad
            return lote.ref
    raise SinStock(f"Sin stock para el sku {sku}")

try:
    asignar("MESA", 100, [Lote("A", 10)])
except SinStock as e:
    print("bloqueado:", e)
