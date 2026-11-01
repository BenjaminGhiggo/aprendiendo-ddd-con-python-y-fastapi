# repositorio.py — el patrón Repository: una abstracción para guardar/recuperar
# el modelo de dominio, sin que el dominio sepa CÓMO se almacena (memoria, SQL, etc.).
import abc

from modelo import Lote


class RepositorioAbstracto(abc.ABC):
    # El contrato: solo dos métodos. Agregar un lote y obtenerlo por su referencia.
    @abc.abstractmethod
    def agregar(self, lote: Lote):
        raise NotImplementedError

    @abc.abstractmethod
    def obtener(self, referencia) -> Lote:
        raise NotImplementedError


class RepositorioFalso(RepositorioAbstracto):
    # Implementación "falsa" para pruebas: un simple envoltorio sobre un set.
    def __init__(self, lotes):
        self._lotes = set(lotes)

    def agregar(self, lote):
        self._lotes.add(lote)

    def obtener(self, referencia):
        return next(l for l in self._lotes if l.referencia == referencia)

    def listar(self):
        return list(self._lotes)


class RepositorioSQLAlchemy(RepositorioAbstracto):
    # Adaptador REAL: envuelve una sesión de SQLAlchemy.
    def __init__(self, sesion):
        self.sesion = sesion

    def agregar(self, lote):
        self.sesion.add(lote)

    def obtener(self, referencia):
        return self.sesion.query(Lote).filter_by(referencia=referencia).one()

    def listar(self):
        return self.sesion.query(Lote).all()
