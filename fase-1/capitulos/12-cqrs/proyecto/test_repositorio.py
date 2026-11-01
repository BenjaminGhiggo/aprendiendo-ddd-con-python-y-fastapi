from sqlalchemy import text
from modelo import Producto, Lote
from repositorio import RepositorioAbstracto, RepositorioFalso, RepositorioSQLAlchemy
import pytest


def test_repo_falso_agrega_y_obtiene_un_producto():
    producto = Producto("MESA", [])
    repo = RepositorioFalso([])
    repo.agregar(producto)
    assert repo.obtener("MESA") is producto


def test_no_se_puede_instanciar_el_repositorio_abstracto():
    with pytest.raises(TypeError):
        RepositorioAbstracto()


def test_repo_sql_guarda_un_producto(sesion):
    repo = RepositorioSQLAlchemy(sesion)
    repo.agregar(Producto("MESA", [Lote("l1", "MESA", 20, eta=None)]))
    sesion.commit()
    assert list(sesion.execute(text("SELECT sku FROM productos"))) == [("MESA",)]
