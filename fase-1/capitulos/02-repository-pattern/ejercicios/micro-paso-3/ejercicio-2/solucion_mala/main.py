# Ej2 — MALA: el servicio CREA el repositorio concreto adentro (no testeable).
class RepoSQL:
    def __init__(self):
        self._datos = []
    def agregar(self, lote):
        self._datos.append(lote)

def registrar_lote(lote):
    repo = RepoSQL()      # atado al repo SQL; no puedo inyectar un fake para probar
    repo.agregar(lote)
    return repo

print(registrar_lote("L1")._datos)
