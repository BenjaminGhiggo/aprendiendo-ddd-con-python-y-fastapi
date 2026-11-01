# Ej3 — BUENA: obtener devuelve UN lote (como .one() de SQLAlchemy).
class RepoFalso:
    def __init__(self, lotes):
        self._lotes = list(lotes)
    def obtener(self, referencia):
        return next(l for l in self._lotes if l == referencia)

repo = RepoFalso(["L1", "L2"])
print(repo.obtener("L1"))
