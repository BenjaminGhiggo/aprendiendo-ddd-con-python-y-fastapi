# Ej1 — MALA: el repo FALSO no respeta el contrato (devuelve algo distinto al real).
class RepoReal:
    def __init__(self):
        self.datos = {}
    def obtener(self, ref):
        return self.datos.get(ref)   # devuelve None si no está

class RepoFalso:
    def obtener(self, ref):
        return "DUMMY"               # SIEMPRE devuelve "DUMMY": no imita al real

def existe(repo, ref):
    return repo.obtener(ref) is not None

print(existe(RepoReal(), "L1"))   # False (correcto: no está)
print(existe(RepoFalso(), "L1"))  # True  (MENTIRA: el falso rompe la lógica)
