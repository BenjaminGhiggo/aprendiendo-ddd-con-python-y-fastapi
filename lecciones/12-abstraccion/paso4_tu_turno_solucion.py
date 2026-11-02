# paso4_tu_turno_solucion.py — PASO 4 de la Lección 12: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/12-abstraccion/paso3_tu_turno.py lecciones/12-abstraccion/paso4_tu_turno_solucion.py
# Si tu versión es distinta pero los tests pasan, también está bien.
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


class RepositorioLista(RepositorioAbstracto):     # TODO 1: hereda del contrato (A5)
    def __init__(self):
        self._lotes = []                          # TODO 2

    def agregar(self, lote):                      # TODO 3
        self._lotes.append(lote)

    def obtener(self, referencia):                # TODO 4
        for lote in self._lotes:
            if lote.referencia == referencia:
                return lote
        return None

    def listar(self):                             # TODO 5
        referencias = []
        for lote in self._lotes:
            referencias.append(lote.referencia)
        return referencias


# Comprobación esperada:
#   uv run pytest lecciones/12-abstraccion -q   ->   5 passed
