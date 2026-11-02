# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta con python (imprime las respuestas):
#   uv run python lecciones/08-modulos-y-pytest/paso5_solucionario/nivel_avanzado.py
# o con pytest (corre las funciones test_...):
#   uv run pytest lecciones/08-modulos-y-pytest/paso5_solucionario/nivel_avanzado.py -v
import pytest

from calculos import total
from inventario import SinStock, asignar_sku, LineaPedido, Lote


# Problema 9: TDD. Primero se escribió esta prueba, después total() con descuento.
def test_total_con_descuento():
    assert total(100, 2, descuento=10) == 190


# Problema 10: pytest.raises con match (T6 + T7).
def test_sin_stock_menciona_el_sku():
    with pytest.raises(SinStock, match="MESA"):
        asignar_sku("MESA", 3, 10)


# Problema 11: probar el método de una clase que vive en otro módulo.
def test_lote_puede_asignar_mismo_sku():
    lote = Lote("L1", "MESA", 20)
    assert lote.puede_asignar(LineaPedido("o1", "MESA", 5)) is True


def test_lote_no_puede_asignar_otro_sku():
    lote = Lote("L1", "MESA", 20)
    assert lote.puede_asignar(LineaPedido("o1", "SILLA", 5)) is False


# Problema 12 (puente al libro): la primera prueba del cap. 1,
# "test_allocating_to_a_batch_reduces_the_available_quantity" ... "assert batch.available_quantity == 18"
def test_asignar_a_un_lote_reduce_la_cantidad_disponible():
    lote = Lote("batch-001", "SMALL-TABLE", 20)
    linea = LineaPedido("order-ref", "SMALL-TABLE", 2)
    lote.asignar(linea)
    assert lote.cantidad_disponible == 18


if __name__ == "__main__":
    test_total_con_descuento()
    print("P9: test_total_con_descuento pasó ->", total(100, 2, descuento=10))      # 190
    test_sin_stock_menciona_el_sku()
    print("P10: test_sin_stock_menciona_el_sku pasó")
    test_lote_puede_asignar_mismo_sku()
    test_lote_no_puede_asignar_otro_sku()
    print("P11: las 2 pruebas del Lote pasaron")
    test_asignar_a_un_lote_reduce_la_cantidad_disponible()
    print("P12: test_asignar_a_un_lote_reduce_la_cantidad_disponible pasó (20 - 2 = 18)")
