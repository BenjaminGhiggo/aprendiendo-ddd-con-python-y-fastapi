# Ej2 — MALA (funciona): el repo falso NO cumple el contrato: obtener devuelve el primero.
class RepoFalso:
    def __init__(self, lotes):
        self._lotes = list(lotes)
    def obtener(self, referencia):
        return self._lotes[0]   # ignora la referencia

print(RepoFalso(["L1", "L2"]).obtener("L2"))   # L1 -> MAL
