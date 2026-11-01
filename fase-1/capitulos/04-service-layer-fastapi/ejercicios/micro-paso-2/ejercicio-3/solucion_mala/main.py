# MALA: el endpoint crea su dependencia adentro (no testeable con un fake).
class RepoReal:
    def listar(self): return ["L1"]
def endpoint():
    repo = RepoReal()        # atado al real
    return repo.listar()
print(endpoint())
