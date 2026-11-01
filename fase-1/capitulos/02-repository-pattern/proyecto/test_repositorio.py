import pytest
from modelo import Lote
from repositorio import RepositorioAbstracto, RepositorioFalso


def test_el_repositorio_falso_agrega_y_obtiene_un_lote():
    lote = Lote("lote-001", "MESA", 20, eta=None)
    repo = RepositorioFalso([])
    repo.agregar(lote)
    assert repo.obtener("lote-001") == lote


def test_no_se_puede_instanciar_el_repositorio_abstracto():
    with pytest.raises(TypeError):
        RepositorioAbstracto()
