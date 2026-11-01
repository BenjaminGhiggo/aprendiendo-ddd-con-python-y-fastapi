# MALA: publicar objetos de dominio al exterior (acopla a otros servicios al modelo).
class Lote:
    def __init__(self, ref): self.ref=ref
def publicar(e): print("publicando objeto:", e)
publicar(Lote("l1"))              # otro servicio dependeria de nuestra clase Lote
