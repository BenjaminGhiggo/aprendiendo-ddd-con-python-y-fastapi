# lsp.py  -> LSP: una subclase debe poder USARSE en lugar de su base, sin romper nada.
from abc import ABC, abstractmethod

class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...
    @abstractmethod
    def obtener(self, ref): ...

# Implementación REAL (en memoria).
class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self): self._datos = {}
    def agregar(self, ref): self._datos[ref] = ref
    def obtener(self, ref): return self._datos.get(ref)

# Implementación FALSA para pruebas (mismo contrato).
class RepositorioFalso(RepositorioAbstracto):
    def __init__(self): self._datos = set()
    def agregar(self, ref): self._datos.add(ref)
    def obtener(self, ref): return ref if ref in self._datos else None

# Código de alto nivel: funciona con CUALQUIER repositorio que cumpla el contrato.
def guardar_y_leer(repo, ref):
    repo.agregar(ref)
    return repo.obtener(ref)

# El real y el falso son INTERCAMBIABLES: ambos dan el mismo resultado.
print(guardar_y_leer(RepositorioEnMemoria(), "LOTE-001"))
print(guardar_y_leer(RepositorioFalso(), "LOTE-001"))
