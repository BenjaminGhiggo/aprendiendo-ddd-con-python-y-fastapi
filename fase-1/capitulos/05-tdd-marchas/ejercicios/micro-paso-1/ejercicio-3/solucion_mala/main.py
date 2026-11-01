# MALA: el servicio devuelve el objeto de dominio (expone el dominio al cliente).
class Lote:
    def __init__(self, ref): self.ref=ref
def servicio(lotes):
    return lotes[0]                        # devuelve un Lote
print(servicio([Lote("L1")]).ref)
