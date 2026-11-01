# Ej2 — BUENA: con @abstractmethod no se puede instanciar sin implementar.
from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

try:
    RepositorioAbstracto()          # Python lo impide
except TypeError as e:
    print("No se puede instanciar la abstracta:", e)
