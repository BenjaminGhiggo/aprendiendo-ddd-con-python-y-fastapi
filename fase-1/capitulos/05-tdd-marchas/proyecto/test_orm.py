from modelo import Lote, LineaPedido


def test_el_orm_guarda_y_carga_una_linea(sesion):
    sesion.add(LineaPedido("pedido-1", "MESA", 2))
    sesion.commit()
    assert sesion.query(LineaPedido).all() == [LineaPedido("pedido-1", "MESA", 2)]


def test_el_orm_guarda_y_carga_un_lote_con_sus_asignaciones(sesion):
    lote = Lote("lote-001", "SOFA", 100, eta=None)
    lote.asignar(LineaPedido("pedido-1", "SOFA", 12))
    sesion.add(lote)
    sesion.commit()
    cargado = sesion.query(Lote).one()
    assert cargado.referencia == "lote-001"
    assert cargado._cantidad_comprada == 100
    assert cargado._asignaciones == {LineaPedido("pedido-1", "SOFA", 12)}
