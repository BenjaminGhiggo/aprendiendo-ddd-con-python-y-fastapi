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


def make_lote_y_linea(sku, cantidad_lote, cantidad_linea):
    return (
        Lote("lote-001", sku, cantidad_lote, eta=date.today()),
        LineaPedido("pedido-123", sku, cantidad_linea),
    )


def test_puede_asignar_si_lo_disponible_es_mayor_que_lo_requerido():
    lote, linea = make_lote_y_linea("LAMPARA-ELEGANTE", 20, 2)
    assert lote.puede_asignar(linea)


def test_no_puede_asignar_si_lo_disponible_es_menor_que_lo_requerido():
    lote, linea = make_lote_y_linea("LAMPARA-ELEGANTE", 2, 20)
    assert lote.puede_asignar(linea) is False


def test_puede_asignar_si_lo_disponible_es_igual_que_lo_requerido():
    lote, linea = make_lote_y_linea("LAMPARA-ELEGANTE", 2, 2)
    assert lote.puede_asignar(linea)


def test_no_puede_asignar_si_los_skus_no_coinciden():
    lote = Lote("lote-001", "SILLA-INCOMODA", 100, eta=None)
    linea = LineaPedido("pedido-123", "TOSTADORA-CARA", 10)
    assert lote.puede_asignar(linea) is False


def test_asignar_la_misma_linea_dos_veces_no_descuenta_doble():
    lote, linea = make_lote_y_linea("MESA", 20, 2)
    lote.asignar(linea)
    lote.asignar(linea)
    assert lote.cantidad_disponible == 18


def test_desasignar_una_linea_no_asignada_no_cambia_nada():
    lote, linea = make_lote_y_linea("MESA", 20, 2)
    lote.desasignar(linea)
    assert lote.cantidad_disponible == 20
