# BUENA: el servicio devuelve un primitivo (la referencia).
class Lote:
    def __init__(self, ref): self.ref=ref
def servicio(lotes):
    return lotes[0].ref                    # devuelve la referencia (str)
print(servicio([Lote("L1")]))
