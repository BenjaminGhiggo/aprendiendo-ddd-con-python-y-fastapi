# Ej3 — MALA (funciona): "Trabajador" obliga a todos a tener trabajar() Y cobrar_sueldo().
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self): ...
    @abstractmethod
    def cobrar_sueldo(self): ...

class Voluntario(Trabajador):
    def trabajar(self):
        return "trabajando"
    def cobrar_sueldo(self):
        raise NotImplementedError("no cobro")   # un voluntario no cobra: método forzado

print(Voluntario().trabajar())
