# Ej2 — BUENA: obtener busca por la referencia (como el repo real).
class RepoFalso:
    def __init__(self, lotes):
        self._lotes = list(lotes)
    def obtener(self, referencia):
        return next(l for l in self._lotes if l == referencia)

print(RepoFalso(["L1", "L2"]).obtener("L2"))   # L2
