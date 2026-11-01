# BUENA: un servicio agregar_lote prepara los datos (sin tocar el dominio en el test).
class Lote:
    def __init__(self, ref, sku): self.ref=ref; self.sku=sku
def agregar_lote(ref, sku, repo):
    repo.append(Lote(ref, sku))
repo = []
agregar_lote("L1", "MESA", repo)          # setup con primitivos
print([l.ref for l in repo])
