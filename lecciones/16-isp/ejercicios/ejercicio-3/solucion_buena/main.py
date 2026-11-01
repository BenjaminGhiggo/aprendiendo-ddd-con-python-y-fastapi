# Ej3 — BUENA: separar las capacidades; cada quien implementa lo suyo.
from abc import ABC, abstractmethod

class Trabaja(ABC):
    @abstractmethod
    def trabajar(self): ...

class Cobra(ABC):
    @abstractmethod
    def cobrar_sueldo(self): ...

class Voluntario(Trabaja):
    def trabajar(self):
        return "trabajando"

class Empleado(Trabaja, Cobra):
    def trabajar(self):
        return "trabajando"
    def cobrar_sueldo(self):
        return "cobrando"

print(Voluntario().trabajar())
print(Empleado().cobrar_sueldo())
