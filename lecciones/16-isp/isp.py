# isp.py  -> ISP: interfaces PEQUEÑAS y específicas.
# Nadie debe depender de métodos que no usa.
from abc import ABC, abstractmethod

# En vez de UNA interfaz gigante, separamos en dos pequeñas:
class Lector(ABC):
    @abstractmethod
    def obtener(self, ref): ...

class Escritor(ABC):
    @abstractmethod
    def agregar(self, ref): ...

# Un repositorio concreto puede cumplir AMBAS si las necesita.
class Repositorio(Lector, Escritor):
    def __init__(self): self._datos = {}
    def agregar(self, ref): self._datos[ref] = ref
    def obtener(self, ref): return self._datos.get(ref)

# Un REPORTE solo necesita LEER -> depende solo de Lector (interfaz pequeña),
# no le obligamos a conocer 'agregar'.
def reporte(lector: Lector, ref):
    return f"Encontrado: {lector.obtener(ref)}"

repo = Repositorio()
repo.agregar("LOTE-001")
print(reporte(repo, "LOTE-001"))   # el reporte solo usó obtener()
