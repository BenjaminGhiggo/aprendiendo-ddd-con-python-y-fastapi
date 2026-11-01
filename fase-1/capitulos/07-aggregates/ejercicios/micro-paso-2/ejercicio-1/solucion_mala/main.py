# MALA: el repositorio guarda y busca LOTES sueltos (partes internas del agregado).
class RepoLotes:
    def __init__(self): self._lotes=[]
    def agregar(self, lote): self._lotes.append(lote)
    def obtener(self, ref): return next(l for l in self._lotes if l["ref"]==ref)
r = RepoLotes(); r.agregar({"ref":"l1","sku":"MESA"}); print(r.obtener("l1"))
