# dip.py  -> DIP: el código de ALTO NIVEL (la lógica) depende de una ABSTRACCIÓN,
# no de un detalle concreto (una base de datos, un archivo, etc.).
from abc import ABC, abstractmethod

# La ABSTRACCIÓN (contrato). El alto nivel dependerá de ESTO, no de un detalle.
class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...
    @abstractmethod
    def obtener(self, ref): ...

# Detalle de BAJO NIVEL: una implementación concreta (hoy en memoria).
class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self): self._datos = {}
    def agregar(self, ref): self._datos[ref] = ref
    def obtener(self, ref): return self._datos.get(ref)

# ALTO NIVEL: la lógica de negocio. NO crea el repositorio adentro;
# lo RECIBE (se lo "inyectamos"). Así no depende de una implementación concreta.
def registrar_lote(repo: RepositorioAbstracto, referencia):
    repo.agregar(referencia)
    return repo.obtener(referencia)

# Nosotros decidimos AFUERA qué implementación usar y se la pasamos.
repo = RepositorioEnMemoria()
print(registrar_lote(repo, "LOTE-001"))   # LOTE-001
