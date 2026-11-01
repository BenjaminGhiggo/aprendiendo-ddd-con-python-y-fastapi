# Ej3 — BUENA: una ABC con @abstractmethod no se puede instanciar sin implementar.
from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, lote): ...

try:
    RepositorioAbstracto()
except TypeError as e:
    print("no se puede instanciar la abstracta:", e)
