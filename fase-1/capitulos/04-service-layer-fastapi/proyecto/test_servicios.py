import pytest
from modelo import Lote, LineaPedido
from repositorio import RepositorioFalso
import servicios


class SesionFalsa:
    comprometida = False
    def commit(self):
        self.comprometida = True


def test_asignar_devuelve_la_referencia_del_lote():
    linea = LineaPedido("o1", "LAMPARA", 10)
    repo = RepositorioFalso([Lote("lote-1", "LAMPARA", 100, eta=None)])
    assert servicios.asignar(linea, repo, SesionFalsa()) == "lote-1"


def test_asignar_lanza_error_si_el_sku_no_existe():
    linea = LineaPedido("o1", "INEXISTENTE", 10)
    repo = RepositorioFalso([Lote("lote-1", "LAMPARA", 100, eta=None)])
    with pytest.raises(servicios.SkuInvalido, match="INEXISTENTE"):
        servicios.asignar(linea, repo, SesionFalsa())


def test_asignar_hace_commit():
    linea = LineaPedido("o1", "LAMPARA", 10)
    repo = RepositorioFalso([Lote("lote-1", "LAMPARA", 100, eta=None)])
    sesion = SesionFalsa()
    servicios.asignar(linea, repo, sesion)
    assert sesion.comprometida is True
