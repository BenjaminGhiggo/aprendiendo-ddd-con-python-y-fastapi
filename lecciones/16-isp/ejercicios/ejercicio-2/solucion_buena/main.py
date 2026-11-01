# Ej2 — BUENA: el reporte depende solo de una interfaz pequeña de lectura.
from abc import ABC, abstractmethod

class Lector(ABC):
    @abstractmethod
    def obtener(self, ref): ...

class Repositorio(Lector):
    def __init__(self):
        self.datos = {"L1": "Lote 1"}
    def obtener(self, ref):
        return self.datos.get(ref)

def reporte(lector: Lector):
    return "Reporte: " + str(lector.obtener("L1"))

print(reporte(Repositorio()))
