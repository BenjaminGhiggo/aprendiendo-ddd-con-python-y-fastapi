# Ej1 — BUENA: el falso respeta el MISMO contrato que el real (es sustituible).
class RepoReal:
    def __init__(self):
        self.datos = {}
    def obtener(self, ref):
        return self.datos.get(ref)

class RepoFalso:
    def __init__(self):
        self.datos = {}
    def obtener(self, ref):
        return self.datos.get(ref)   # mismo comportamiento: None si no está

def existe(repo, ref):
    return repo.obtener(ref) is not None

print(existe(RepoReal(), "L1"))   # False
print(existe(RepoFalso(), "L1"))  # False (igual que el real)
