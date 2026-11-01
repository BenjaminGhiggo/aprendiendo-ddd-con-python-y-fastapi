# abstraccion.py
from abc import ABC, abstractmethod

# Una CLASE ABSTRACTA define el CONTRATO (qué métodos deben existir),
# pero no cómo se hacen. Es como un molde obligatorio.
class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, lote):
        ...
    @abstractmethod
    def obtener(self, referencia):
        ...

# Una implementación CONCRETA cumple el contrato (implementa TODOS los métodos).
class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._lotes = {}
    def agregar(self, lote):
        self._lotes[lote] = lote
    def obtener(self, referencia):
        return self._lotes.get(referencia)

repo = RepositorioEnMemoria()
repo.agregar("LOTE-001")
print(repo.obtener("LOTE-001"))     # LOTE-001

# No se puede crear un objeto de la clase abstracta (le faltan implementaciones):
try:
    RepositorioAbstracto()
except TypeError as e:
    print("No se puede instanciar la abstracta:", e)
