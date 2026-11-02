# Ej1 — BUENA: un contrato (ABC) obliga a ambos a tener el mismo método.
from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

class RepoMemoria(RepositorioAbstracto):
    def __init__(self):
        self.datos = {}
    def agregar(self, ref):
        self.datos[ref] = ref

class RepoLista(RepositorioAbstracto):
    def __init__(self):
        self.datos = []
    def agregar(self, ref):
        self.datos.append(ref)

for repo in [RepoMemoria(), RepoLista()]:
    repo.agregar("L1")
print("mismo contrato: agregar()")
