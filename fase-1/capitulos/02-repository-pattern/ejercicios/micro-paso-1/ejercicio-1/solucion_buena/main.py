# Ej1 — BUENA: el servicio recibe un repositorio (no sabe cómo se guarda).
class RepositorioFalso:
    def __init__(self):
        self._lotes = []
    def agregar(self, referencia):
        self._lotes.append(referencia)
    def listar(self):
        return list(self._lotes)

def registrar_lote(repo, referencia):
    repo.agregar(referencia)

repo = RepositorioFalso()
registrar_lote(repo, "L1")
print(repo.listar())
