import pytest
from repositorio import RepositorioFalso
from unidad_de_trabajo import UnidadDeTrabajoAbstracta
import servicios


class UnidadDeTrabajoFalsa(UnidadDeTrabajoAbstracta):
    def __init__(self):
        self.productos = RepositorioFalso([])
        self.comprometido = False
    def comprometer(self):
        self.comprometido = True
    def deshacer(self):
        pass


def test_agregar_lote_crea_el_producto():
    uow = UnidadDeTrabajoFalsa()
    servicios.agregar_lote("lote-1", "LAMPARA", 100, None, uow)
    assert uow.productos.obtener("LAMPARA") is not None
    assert uow.comprometido is True


def test_asignar_devuelve_la_referencia():
    uow = UnidadDeTrabajoFalsa()
    servicios.agregar_lote("lote-1", "LAMPARA", 100, None, uow)
    assert servicios.asignar("o1", "LAMPARA", 10, uow) == "lote-1"


def test_asignar_error_si_sku_no_existe():
    uow = UnidadDeTrabajoFalsa()
    with pytest.raises(servicios.SkuInvalido, match="INEXISTENTE"):
        servicios.asignar("o1", "INEXISTENTE", 10, uow)
