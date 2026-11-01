# Ej3 — MALA: obtener devuelve una LISTA; quien llama tiene que sacar [0].
class RepoFalso:
    def __init__(self, lotes):
        self._lotes = list(lotes)
    def obtener(self, referencia):
        return [l for l in self._lotes if l == referencia]   # lista

repo = RepoFalso(["L1", "L2"])
print(repo.obtener("L1")[0])   # el que llama debe recordar el [0]
