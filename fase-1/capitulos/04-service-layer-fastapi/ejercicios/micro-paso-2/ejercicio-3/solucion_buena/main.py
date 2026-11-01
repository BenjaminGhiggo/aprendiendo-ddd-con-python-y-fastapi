# BUENA: la dependencia se inyecta (en FastAPI, con Depends).
class RepoReal:
    def listar(self): return ["L1"]
def endpoint(repo):
    return repo.listar()
print(endpoint(RepoReal()))        # en test: endpoint(RepoFalso())
