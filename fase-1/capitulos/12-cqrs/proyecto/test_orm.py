from modelo import Producto, Lote, LineaPedido


def test_el_orm_guarda_y_carga_una_linea(sesion):
    sesion.add(LineaPedido("pedido-1", "MESA", 2))
    sesion.commit()
    assert sesion.query(LineaPedido).all() == [LineaPedido("pedido-1", "MESA", 2)]


def test_el_orm_guarda_y_carga_un_producto_con_lotes(sesion):
    sesion.add(Producto("MESA", [Lote("l1", "MESA", 20, eta=None)]))
    sesion.commit()
    cargado = sesion.query(Producto).one()
    assert cargado.sku == "MESA"
    assert len(cargado.lotes) == 1
