import abc
import repositorio


class UnidadDeTrabajoAbstracta(abc.ABC):
    productos: repositorio.RepositorioAbstracto

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.deshacer()

    def recolectar_eventos_nuevos(self):
        for producto in self.productos.vistos:
            while producto.eventos:
                yield producto.eventos.pop(0)

    @abc.abstractmethod
    def comprometer(self):
        raise NotImplementedError

    @abc.abstractmethod
    def deshacer(self):
        raise NotImplementedError


class UnidadDeTrabajoSQLAlchemy(UnidadDeTrabajoAbstracta):
    def __init__(self, fabrica_sesion):
        self.fabrica_sesion = fabrica_sesion

    def __enter__(self):
        self.sesion = self.fabrica_sesion()
        self.productos = repositorio.RepositorioSQLAlchemy(self.sesion)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.sesion.close()

    def comprometer(self):
        self.sesion.commit()

    def deshacer(self):
        self.sesion.rollback()
