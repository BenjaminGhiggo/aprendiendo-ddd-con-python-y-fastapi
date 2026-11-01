# Ej1 — MALA: el adaptador usa un método con OTRO nombre (no cumple el contrato).
from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, lote): ...

class RepoSQL(RepositorioAbstracto):
    def __init__(self):
        self._datos = []
    def guardar(self, lote):        # se llama "guardar", no "agregar"
        self._datos.append(lote)
    def agregar(self, lote):        # obligado por la ABC, pero vacio
        pass

repo = RepoSQL()
repo.guardar("L1")                  # el codigo que espera "agregar" no funcionaria
print(repo._datos)
