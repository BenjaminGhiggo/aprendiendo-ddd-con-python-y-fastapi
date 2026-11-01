from datetime import date
from modelo import Lote, LineaPedido

def test_asignar_a_un_lote_reduce_la_cantidad_disponible():
    lote = Lote("lote-001", "MESA-PEQUEÑA", cantidad=20, eta=date.today())
    linea = LineaPedido("pedido-ref", "MESA-PEQUEÑA", 2)
    lote.asignar(linea)
    assert lote.cantidad_disponible == 18
