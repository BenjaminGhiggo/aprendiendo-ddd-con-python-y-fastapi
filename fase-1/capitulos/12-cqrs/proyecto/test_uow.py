from sqlalchemy import text
from modelo import Producto, Lote
from unidad_de_trabajo import UnidadDeTrabajoSQLAlchemy


def test_la_uow_guarda_y_confirma(fabrica_sesion):
    uow = UnidadDeTrabajoSQLAlchemy(fabrica_sesion)
    with uow:
        uow.productos.agregar(Producto("MESA", [Lote("l1", "MESA", 20, eta=None)]))
        uow.comprometer()
    assert list(fabrica_sesion().execute(text("SELECT sku FROM productos"))) == [("MESA",)]


def test_la_uow_deshace_si_no_se_confirma(fabrica_sesion):
    uow = UnidadDeTrabajoSQLAlchemy(fabrica_sesion)
    with uow:
        uow.productos.agregar(Producto("NO", []))
    assert list(fabrica_sesion().execute(text("SELECT sku FROM productos"))) == []
