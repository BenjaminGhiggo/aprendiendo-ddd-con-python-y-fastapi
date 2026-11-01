from datetime import date
from modelo import Lote, LineaPedido

def test_asignar_a_un_lote_reduce_la_cantidad_disponible():
    lote = Lote("lote-001", "MESA-PEQUEÑA", cantidad=20, eta=date.today())
    linea = LineaPedido("pedido-ref", "MESA-PEQUEÑA", 2)
    lote.asignar(linea)
    assert lote.cantidad_disponible == 18


def test_dos_lineas_con_los_mismos_datos_son_iguales():
    # VALUE OBJECT: se identifican por sus datos. Mismos datos => iguales.
    assert LineaPedido("pedido-1", "MESA", 2) == LineaPedido("pedido-1", "MESA", 2)


def test_dos_lotes_con_la_misma_referencia_son_el_mismo():
    # ENTIDAD: se identifica por su referencia. Misma referencia => el mismo lote,
    # aunque el resto de datos cambie.
    lote_a = Lote("lote-001", "MESA", 20, eta=None)
    lote_b = Lote("lote-001", "SILLA", 5, eta=date.today())
    assert lote_a == lote_b
