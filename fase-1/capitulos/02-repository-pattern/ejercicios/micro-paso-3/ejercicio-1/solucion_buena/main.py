# Ej1 — BUENA: el adaptador implementa el contrato (agregar), intercambiable.
from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, lote): ...

class RepoSQL(RepositorioAbstracto):
    def __init__(self):
        self._datos = []
    def agregar(self, lote):
        self._datos.append(lote)

def registrar(repo, lote):          # funciona con CUALQUIER repositorio del contrato
    repo.agregar(lote)

repo = RepoSQL()
registrar(repo, "L1")
print(repo._datos)
