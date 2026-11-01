# unidad_de_trabajo.py — la Unidad de Trabajo (UoW): agrupa repositorio + sesión
# y da una frontera atómica (todo se confirma junto, o nada) con un context manager.
import abc

import repositorio


class UnidadDeTrabajoAbstracta(abc.ABC):
    lotes: repositorio.RepositorioAbstracto

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.deshacer()      # por defecto, al salir se deshace lo no confirmado

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
        self.lotes = repositorio.RepositorioSQLAlchemy(self.sesion)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.sesion.close()

    def comprometer(self):
        self.sesion.commit()

    def deshacer(self):
        self.sesion.rollback()
