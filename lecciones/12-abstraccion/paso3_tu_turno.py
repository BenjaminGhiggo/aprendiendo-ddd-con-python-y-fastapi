# paso3_tu_turno.py — PASO 3 de la Lección 12 (pair programming).
# Completa cada # TODO. Luego comprueba con pytest:
#   uv run pytest lecciones/12-abstraccion -q
# Al principio los tests salen en ROJO (fallan): es a propósito. Cuando completes
# los TODO deben salir en VERDE: "5 passed".
# Si te trabas, mira la fórmula indicada entre paréntesis en el README (§5 y §6).
# Cuando termines, compara con paso4_tu_turno_solucion.py.
import abc


# Esto ya está listo: no lo cambies.
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad


# El CONTRATO ya está listo: no lo cambies.
class RepositorioAbstracto(abc.ABC):
    @abc.abstractmethod
    def agregar(self, lote):
        raise NotImplementedError

    @abc.abstractmethod
    def obtener(self, referencia):
        raise NotImplementedError

    @abc.abstractmethod
    def listar(self):
        raise NotImplementedError


# TODO 1: haz que RepositorioLista HEREDE del contrato (fórmula A5):
#         escribe (RepositorioAbstracto) entre "RepositorioLista" y los dos puntos.
class RepositorioLista:
    def __init__(self):
        # TODO 2: crea una lista vacía en self._lotes.
        pass

    # TODO 3: agregar(lote) guarda el lote al final de self._lotes.
    def agregar(self, lote):
        pass

    # TODO 4: obtener(referencia) recorre self._lotes y devuelve el lote con esa referencia;
    #         si no lo encuentra, devuelve None.
    def obtener(self, referencia):
        pass

    # TODO 5: listar() devuelve una lista con las REFERENCIAS de los lotes, en orden.
    #         Ej.: después de agregar L1 y L2 -> ["L1", "L2"]
    def listar(self):
        pass


# Comprobación esperada (cuando completes los TODO):
#   uv run pytest lecciones/12-abstraccion -q   ->   5 passed
