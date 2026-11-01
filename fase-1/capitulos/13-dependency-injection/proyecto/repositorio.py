import abc
from modelo import Producto


class RepositorioAbstracto(abc.ABC):
    def __init__(self):
        self.vistos = set()                 # productos tocados (para recolectar eventos)

    def agregar(self, producto):
        self._agregar(producto)
        self.vistos.add(producto)

    def obtener(self, sku):
        producto = self._obtener(sku)
        if producto:
            self.vistos.add(producto)
        return producto

    @abc.abstractmethod
    def _agregar(self, producto):
        raise NotImplementedError

    @abc.abstractmethod
    def _obtener(self, sku):
        raise NotImplementedError


class RepositorioFalso(RepositorioAbstracto):
    def __init__(self, productos):
        super().__init__()
        self._productos = list(productos)

    def _agregar(self, producto):
        self._productos.append(producto)

    def _obtener(self, sku):
        return next((p for p in self._productos if p.sku == sku), None)


class RepositorioSQLAlchemy(RepositorioAbstracto):
    def __init__(self, sesion):
        super().__init__()
        self.sesion = sesion

    def _agregar(self, producto):
        self.sesion.add(producto)

    def _obtener(self, sku):
        return self.sesion.query(Producto).filter_by(sku=sku).first()
