import pytest
from repositorio import RepositorioFalso
import servicios


class SesionFalsa:
    comprometida = False
    def commit(self):
        self.comprometida = True


def test_agregar_lote():
    repo, sesion = RepositorioFalso([]), SesionFalsa()
    servicios.agregar_lote("lote-1", "LAMPARA", 100, None, repo, sesion)
    assert repo.obtener("lote-1") is not None
    assert sesion.comprometida is True


def test_asignar_devuelve_la_referencia():
    repo, sesion = RepositorioFalso([]), SesionFalsa()
    servicios.agregar_lote("lote-1", "LAMPARA", 100, None, repo, sesion)
    assert servicios.asignar("o1", "LAMPARA", 10, repo, sesion) == "lote-1"


def test_asignar_error_si_sku_invalido():
    repo, sesion = RepositorioFalso([]), SesionFalsa()
    servicios.agregar_lote("lote-1", "LAMPARA", 100, None, repo, sesion)
    with pytest.raises(servicios.SkuInvalido, match="INEXISTENTE"):
        servicios.asignar("o1", "INEXISTENTE", 10, repo, sesion)
