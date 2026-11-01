# MALA: el test prepara datos construyendo objetos de dominio a mano.
class Lote:
    def __init__(self, ref, sku): self.ref=ref; self.sku=sku
repo = [Lote("L1", "MESA")]               # setup acoplado al dominio
print([l.ref for l in repo])
