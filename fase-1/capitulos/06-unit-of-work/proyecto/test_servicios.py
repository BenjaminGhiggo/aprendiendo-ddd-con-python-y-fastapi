import pytest
from repositorio import RepositorioFalso
from unidad_de_trabajo import UnidadDeTrabajoAbstracta
import servicios


class UnidadDeTrabajoFalsa(UnidadDeTrabajoAbstracta):
    def __init__(self):
        self.lotes = RepositorioFalso([])
        self.comprometido = False
    def comprometer(self):
        self.comprometido = True
    def deshacer(self):
        pass


def test_agregar_lote():
    uow = UnidadDeTrabajoFalsa()
    servicios.agregar_lote("lote-1", "LAMPARA", 100, None, uow)
    assert uow.lotes.obtener("lote-1") is not None
    assert uow.comprometido is True


def test_asignar_devuelve_la_referencia():
    uow = UnidadDeTrabajoFalsa()
    servicios.agregar_lote("lote-1", "LAMPARA", 100, None, uow)
    assert servicios.asignar("o1", "LAMPARA", 10, uow) == "lote-1"


def test_asignar_error_si_sku_invalido():
    uow = UnidadDeTrabajoFalsa()
    servicios.agregar_lote("lote-1", "LAMPARA", 100, None, uow)
    with pytest.raises(servicios.SkuInvalido, match="INEXISTENTE"):
        servicios.asignar("o1", "INEXISTENTE", 10, uow)
