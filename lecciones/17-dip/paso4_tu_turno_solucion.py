# paso4_tu_turno_solucion.py — PASO 4 de la Lección 17: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/17-dip/paso3_tu_turno.py lecciones/17-dip/paso4_tu_turno_solucion.py
# Si tu versión es distinta pero los tests pasan, también está bien.
from abc import ABC, abstractmethod


class Notificador(ABC):
    """La abstracción para avisar (email, SMS... da igual)."""

    @abstractmethod
    def enviar(self, mensaje): ...


class NotificadorFalso(Notificador):
    """Un falso para tests: en vez de enviar, GUARDA los mensajes en una lista."""

    def __init__(self):
        # TODO 1: crea una lista vacía en self.enviados.
        self.enviados = []

    def enviar(self, mensaje):
        # TODO 2: agrega el mensaje a self.enviados.
        self.enviados.append(mensaje)


def avisar_sin_stock(sku, notificador):
    # TODO 3: usa el notificador RECIBIDO para enviar el texto "Sin stock: " + sku.
    #         (no crees ningún notificador aquí adentro: receta DIP1)
    notificador.enviar("Sin stock: " + sku)


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
        self.repo = repo

    def registrar(self, ref):
        # TODO 5: agrega ref al repositorio y devuelve lo que dé obtener(ref).
        self.repo.agregar(ref)
        return self.repo.obtener(ref)
