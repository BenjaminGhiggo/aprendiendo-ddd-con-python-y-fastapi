from sqlalchemy import text
from modelo import Lote
from unidad_de_trabajo import UnidadDeTrabajoSQLAlchemy


def test_la_uow_guarda_y_confirma(fabrica_sesion):
    uow = UnidadDeTrabajoSQLAlchemy(fabrica_sesion)
    with uow:
        uow.lotes.agregar(Lote("lote-uow", "MESA", 20, eta=None))
        uow.comprometer()
    filas = list(fabrica_sesion().execute(text("SELECT referencia FROM lotes")))
    assert filas == [("lote-uow",)]


def test_la_uow_deshace_si_no_se_confirma(fabrica_sesion):
    uow = UnidadDeTrabajoSQLAlchemy(fabrica_sesion)
    with uow:
        uow.lotes.agregar(Lote("lote-no-confirmado", "MESA", 20, eta=None))
        # NO llamamos comprometer() -> al salir del with, se deshace (rollback)
    filas = list(fabrica_sesion().execute(text("SELECT referencia FROM lotes")))
    assert filas == []
