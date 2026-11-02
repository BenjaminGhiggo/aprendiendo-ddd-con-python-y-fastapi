# Ej1 — BUENA: interfaces pequeñas; cada máquina implementa solo lo que hace.
from abc import ABC, abstractmethod

class Impresora(ABC):
    @abstractmethod
    def imprimir(self, doc): ...

class Escaner(ABC):
    @abstractmethod
    def escanear(self, doc): ...

class ImpresoraSimple(Impresora):
    def imprimir(self, doc):
        return "imprimiendo " + doc

class Multifuncional(Impresora, Escaner):
    def imprimir(self, doc):
        return "imprimiendo " + doc
    def escanear(self, doc):
        return "escaneando " + doc

print(ImpresoraSimple().imprimir("hoja"))
print(Multifuncional().escanear("hoja"))
