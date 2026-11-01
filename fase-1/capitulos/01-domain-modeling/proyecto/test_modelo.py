from datetime import date, timedelta
import pytest
from modelo import Lote, LineaPedido, asignar, SinStock

hoy = date.today()
manana = hoy + timedelta(days=1)
mas_tarde = hoy + timedelta(days=10)

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


def test_prefiere_lotes_en_stock_a_los_de_envio():
    lote_en_stock = Lote("lote-en-stock", "RELOJ-RETRO", 100, eta=None)
    lote_de_envio = Lote("lote-de-envio", "RELOJ-RETRO", 100, eta=manana)
    linea = LineaPedido("pedido-ref", "RELOJ-RETRO", 10)
    asignar(linea, [lote_en_stock, lote_de_envio])
    assert lote_en_stock.cantidad_disponible == 90
    assert lote_de_envio.cantidad_disponible == 100


def test_prefiere_los_lotes_mas_tempranos():
    mas_temprano = Lote("lote-rapido", "CUCHARA-MINIMALISTA", 100, eta=hoy)
    intermedio = Lote("lote-normal", "CUCHARA-MINIMALISTA", 100, eta=manana)
    ultimo = Lote("lote-lento", "CUCHARA-MINIMALISTA", 100, eta=mas_tarde)
    linea = LineaPedido("pedido-1", "CUCHARA-MINIMALISTA", 10)
    asignar(linea, [intermedio, mas_temprano, ultimo])
    assert mas_temprano.cantidad_disponible == 90
    assert intermedio.cantidad_disponible == 100
    assert ultimo.cantidad_disponible == 100


def test_devuelve_la_referencia_del_lote_asignado():
    lote_en_stock = Lote("lote-en-stock-ref", "POSTER-CULTO", 100, eta=None)
    lote_de_envio = Lote("lote-de-envio-ref", "POSTER-CULTO", 100, eta=manana)
    linea = LineaPedido("pedido-ref", "POSTER-CULTO", 10)
    referencia = asignar(linea, [lote_en_stock, lote_de_envio])
    assert referencia == lote_en_stock.referencia


def test_lanza_sin_stock_si_no_se_puede_asignar():
    lote = Lote("lote-1", "TENEDOR-PEQUENO", 10, eta=hoy)
    asignar(LineaPedido("pedido-1", "TENEDOR-PEQUENO", 10), [lote])
    with pytest.raises(SinStock, match="TENEDOR-PEQUENO"):
        asignar(LineaPedido("pedido-2", "TENEDOR-PEQUENO", 1), [lote])
