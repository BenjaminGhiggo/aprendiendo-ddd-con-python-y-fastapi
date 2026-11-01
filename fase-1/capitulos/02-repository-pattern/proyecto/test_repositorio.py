import pytest
from modelo import Lote
from repositorio import RepositorioAbstracto, RepositorioFalso, RepositorioSQLAlchemy


def test_el_repositorio_falso_agrega_y_obtiene_un_lote():
    lote = Lote("lote-001", "MESA", 20, eta=None)
    repo = RepositorioFalso([])
    repo.agregar(lote)
    assert repo.obtener("lote-001") == lote


def test_no_se_puede_instanciar_el_repositorio_abstracto():
    with pytest.raises(TypeError):
        RepositorioAbstracto()


def test_el_repositorio_sql_guarda_un_lote(sesion):
    from sqlalchemy import text
    repo = RepositorioSQLAlchemy(sesion)
    repo.agregar(Lote("lote-100", "MESA", 20, eta=None))
    sesion.commit()
    filas = list(sesion.execute(
        text('SELECT referencia, sku, _cantidad_comprada FROM lotes')
    ))
    assert filas == [("lote-100", "MESA", 20)]


def test_el_repositorio_sql_obtiene_un_lote(sesion):
    repo = RepositorioSQLAlchemy(sesion)
    repo.agregar(Lote("lote-200", "SILLA", 5, eta=None))
    sesion.commit()
    assert repo.obtener("lote-200") == Lote("lote-200", "SILLA", 5, eta=None)
