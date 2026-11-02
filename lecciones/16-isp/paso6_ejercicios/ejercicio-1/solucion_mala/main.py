# Ej1 — MALA (funciona): una interfaz gigante obliga a implementar métodos que no se usan.
from abc import ABC, abstractmethod

class Maquina(ABC):
    @abstractmethod
    def imprimir(self, doc): ...
    @abstractmethod
    def escanear(self, doc): ...
    @abstractmethod
    def enviar_fax(self, doc): ...

class ImpresoraSimple(Maquina):
    def imprimir(self, doc):
        return "imprimiendo " + doc
    def escanear(self, doc):
        raise NotImplementedError("no escaneo")   # obligada a implementar algo que no hace
    def enviar_fax(self, doc):
        raise NotImplementedError("no envío fax")

print(ImpresoraSimple().imprimir("hoja"))
