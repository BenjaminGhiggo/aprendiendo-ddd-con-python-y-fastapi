# paso3_tu_turno.py — PASO 3 de la Lección 17 (DIP ⭐ · pair programming).
# La comprobación es con PYTEST (TDD): los tests ya están en test_paso3_tu_turno.py y
# empiezan en ROJO. Completa los # TODO hasta verlos en VERDE:
#   uv run pytest lecciones/17-dip -q
# Meta: la lógica NO crea sus detalles; los RECIBE. Y en los tests le pasamos falsos.
from abc import ABC, abstractmethod


class Notificador(ABC):
    """La abstracción para avisar (email, SMS... da igual)."""

    @abstractmethod
    def enviar(self, mensaje): ...


class NotificadorFalso(Notificador):
    """Un falso para tests: en vez de enviar, GUARDA los mensajes en una lista."""

    def __init__(self):
        # TODO 1: crea una lista vacía en self.enviados.
        pass

    def enviar(self, mensaje):
        # TODO 2: agrega el mensaje a self.enviados.
        pass


def avisar_sin_stock(sku, notificador):
    # TODO 3: usa el notificador RECIBIDO para enviar el texto "Sin stock: " + sku.
    #         (no crees ningún notificador aquí adentro: receta DIP1)
    pass


class RepositorioAbstracto(ABC):
    @abstractmethod
    def agregar(self, ref): ...

    @abstractmethod
    def obtener(self, ref): ...


class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self._datos = {}

    def agregar(self, ref):
        self._datos[ref] = ref

    def obtener(self, ref):
        return self._datos.get(ref)


class ServicioPedidos:
    """Alto nivel: recibe su repositorio por el constructor (receta DIP4)."""

    def __init__(self, repo):
        # TODO 4: guarda el repositorio recibido en self.repo (NO crees uno nuevo).
        pass

    def registrar(self, ref):
        # TODO 5: agrega ref al repositorio y devuelve lo que dé obtener(ref).
        return None
