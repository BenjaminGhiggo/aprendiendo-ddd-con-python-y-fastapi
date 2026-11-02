# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10, Lección 16 · ISP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/16-isp/paso5_solucionario/nivel_intermedio.py
from abc import ABC, abstractmethod


# Problema 5: Trabajador(trabajar, comer) obligaba al Robot a "comer". Partimos por rol.
class Trabajable(ABC):
    @abstractmethod
    def trabajar(self): ...


class Alimentable(ABC):
    @abstractmethod
    def comer(self): ...


class Humano(Trabajable, Alimentable):
    def trabajar(self):
        return "trabaja"

    def comer(self):
        return "come"


class Robot(Trabajable):                    # ya no está obligado a comer
    def trabajar(self):
        return "trabaja sin parar"


print("P5:", Humano().trabajar(), Humano().comer(), "|", Robot().trabajar(), "| ¿robot come?", hasattr(Robot(), "comer"))


# Problema 6: Repositorio cumple Lector y Escritor.
class Lector(ABC):
    @abstractmethod
    def obtener(self, ref): ...


class Escritor(ABC):
    @abstractmethod
    def agregar(self, ref): ...


class Repositorio(Lector, Escritor):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


repo = Repositorio()
print("P6:", isinstance(repo, Lector), isinstance(repo, Escritor))   # True True


# Problema 7: olvidar el método de una de las interfaces -> Python no deja crear el objeto.
class RepoIncompleto(Lector, Escritor):
    def obtener(self, ref):
        return ref


try:
    RepoIncompleto()
except TypeError as error:
    print("P7: error ->", error)


# Problema 8: un falso mínimo para probar el reporte (solo obtener).
def reporte(lector, ref):
    return f"Encontrado: {lector.obtener(ref)}"


class LectorFalso(Lector):
    def obtener(self, ref):
        return "falso-" + ref


assert reporte(LectorFalso(), "L1") == "Encontrado: falso-L1"
print("P8: OK ->", reporte(LectorFalso(), "L1"))
