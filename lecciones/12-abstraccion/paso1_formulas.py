# paso1_formulas.py — PASO 1 de la Lección 12 (Abstracción, clases abstractas con abc).
# Cada bloque es una "fórmula" de las tablas del README (§5 y §6), con su código (A1, C1...).
# Ejecuta:  uv run python lecciones/12-abstraccion/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.

# A1 · importar el módulo abc ("Abstract Base Classes"). Es la forma que usa el libro.
import abc


class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad


# A2 · una CLASE ABSTRACTA hereda de abc.ABC. Define el CONTRATO: QUÉ métodos deben existir.
class RepositorioAbstracto(abc.ABC):
    # A3 · un MÉTODO ABSTRACTO: se marca con @abc.abstractmethod y no dice CÓMO se hace.
    @abc.abstractmethod
    def agregar(self, lote):
        raise NotImplementedError

    @abc.abstractmethod
    def obtener(self, referencia):
        raise NotImplementedError

    # A8 · un método NORMAL (concreto) dentro de la abstracta: lo heredan todas las hijas
    #      y funciona porque se apoya en los métodos del contrato.
    def agregar_varios(self, lotes):
        for lote in lotes:
            self.agregar(lote)


# A5 · una implementación CONCRETA: hereda del contrato e implementa TODOS los métodos abstractos.
class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._lotes = {}

    def agregar(self, lote):
        self._lotes[lote.referencia] = lote

    def obtener(self, referencia):
        return self._lotes.get(referencia)


# A6 · una implementación INCOMPLETA: le falta obtener().
class RepositorioIncompleto(RepositorioAbstracto):
    def agregar(self, lote):
        pass


print("========== CLASES ABSTRACTAS ==========")
print("A1  import abc ->                ", abc.ABC)
print("A2  ¿hereda de abc.ABC?          ", issubclass(RepositorioAbstracto, abc.ABC))
# A3 · ¿qué métodos quedaron marcados como abstractos? Lo dice el mensaje de A4: 'agregar', 'obtener'.

# A4 · la abstracta NO se puede instanciar.
try:
    RepositorioAbstracto()
except TypeError as error:
    print("A4  RepositorioAbstracto():      ", error)

# A5 · la concreta sí, y se usa normalmente.
repo = RepositorioEnMemoria()
repo.agregar(Lote("L1", 10))
print("A5  repo.obtener('L1').cantidad: ", repo.obtener("L1").cantidad)

# A6 · a la incompleta le falta un método: Python no deja crearla.
try:
    RepositorioIncompleto()
except TypeError as error:
    print("A6  RepositorioIncompleto():     ", error)

# A7 · la concreta ES del tipo del contrato.
print("A7  isinstance(repo, RepositorioAbstracto):", isinstance(repo, RepositorioAbstracto))

# A8 · el método concreto de la abstracta funciona en la hija.
repo.agregar_varios([Lote("L2", 5), Lote("L3", 7)])
print("A8  agregar_varios -> L3:        ", repo.obtener("L3").cantidad)

# A9 · forma corta equivalente: from abc import ABC, abstractmethod
from abc import ABC, abstractmethod


class FiguraAbstracta(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError


try:
    FiguraAbstracta()
except TypeError as error:
    print("A9  forma corta, mismo efecto:   ", error)

print()
print("========== ¿QUIÉN REVISA EL CONTRATO? ==========")


# C1/C2 · con duck typing (Lección 11) nadie revisa nada hasta que se LLAMA al método.
class RepoDuckIncompleto:
    def agregar(self, lote):
        pass


duck = RepoDuckIncompleto()                    # se crea sin problema...
try:
    duck.obtener("L1")                         # ...y el error salta recién al usarlo
except AttributeError as error:
    print("C2  duck typing, al LLAMAR:      ", error)

# C2 · con ABC el error salta al CREAR el objeto, antes de usarlo.
try:
    RepositorioIncompleto()
except TypeError as error:
    print("C2  ABC, al CREAR:               ", error)

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Quita el # de UNA línea, ejecuta y lee el mensaje.
# RepositorioAbstracto()     # X1 -> TypeError: Can't instantiate abstract class RepositorioAbstracto
#                            #       without an implementation for abstract methods 'agregar', 'obtener'
# RepositorioIncompleto()    # X2 -> TypeError: Can't instantiate abstract class RepositorioIncompleto
#                            #       without an implementation for abstract method 'obtener'
# ---------------------------------------------------------------------------
