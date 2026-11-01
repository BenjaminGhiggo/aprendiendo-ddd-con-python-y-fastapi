import abc
from modelo import Producto


class RepositorioAbstracto(abc.ABC):
    @abc.abstractmethod
    def agregar(self, producto: Producto):
        raise NotImplementedError

    @abc.abstractmethod
    def obtener(self, sku) -> Producto:
        raise NotImplementedError


class RepositorioFalso(RepositorioAbstracto):
    def __init__(self, productos):
        self._productos = list(productos)

    def agregar(self, producto):
        self._productos.append(producto)

    def obtener(self, sku):
        return next((p for p in self._productos if p.sku == sku), None)

    def listar(self):
        return list(self._productos)


class RepositorioSQLAlchemy(RepositorioAbstracto):
    def __init__(self, sesion):
        self.sesion = sesion

    def agregar(self, producto):
        self.sesion.add(producto)

    def obtener(self, sku):
        return self.sesion.query(Producto).filter_by(sku=sku).first()

    def listar(self):
        return self.sesion.query(Producto).all()
