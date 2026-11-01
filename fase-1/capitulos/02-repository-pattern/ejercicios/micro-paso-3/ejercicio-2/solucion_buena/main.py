# Ej2 — BUENA: el repositorio se inyecta; en pruebas uso un fake, en prod el real.
class RepoFalso:
    def __init__(self):
        self._datos = []
    def agregar(self, lote):
        self._datos.append(lote)

def registrar_lote(repo, lote):
    repo.agregar(lote)

repo = RepoFalso()
registrar_lote(repo, "L1")
print(repo._datos)
