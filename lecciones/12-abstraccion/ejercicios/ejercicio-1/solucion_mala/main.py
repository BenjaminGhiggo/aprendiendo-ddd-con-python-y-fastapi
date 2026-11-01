# Ej1 — MALA (funciona): dos "repositorios" sin contrato; cada uno nombra distinto.
class RepoMemoria:
    def __init__(self):
        self.datos = {}
    def guardar(self, ref):           # aquí se llama "guardar"
        self.datos[ref] = ref

class RepoLista:
    def __init__(self):
        self.datos = []
    def add(self, ref):               # aquí se llama "add": nadie garantiza el nombre
        self.datos.append(ref)

RepoMemoria().guardar("L1")
RepoLista().add("L2")
print("sin contrato común")
