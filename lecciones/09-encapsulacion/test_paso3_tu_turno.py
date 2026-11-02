# test_paso3_tu_turno.py — las pruebas de tu paso3 (Lección 09).
# Ejecuta:  uv run pytest lecciones/09-encapsulacion -q
# ROJO al principio (los TODO están vacíos) -> VERDE cuando los completes.
#
# Para ver la referencia en verde, cambia la línea de abajo a:
#   import paso4_tu_turno_solucion as modulo
import pytest

import paso3_tu_turno as modulo


def test_disponible_es_una_propiedad():
    lote = modulo.Lote("L1", 20)
    assert lote.disponible == 20          # sin paréntesis: es una propiedad


def test_asignar_resta_del_stock():
    lote = modulo.Lote("L1", 20)
    lote.asignar(5)
    assert lote.disponible == 15


def test_asignar_de_mas_lanza_error_y_no_cambia():
    lote = modulo.Lote("L1", 20)
    # pytest.raises(ValueError) afirma: "el bloque de adentro DEBE lanzar ValueError".
    with pytest.raises(ValueError):
        lote.asignar(999)
    assert lote.disponible == 20          # el estado no se corrompió


def test_reponer_suma_al_stock():
    lote = modulo.Lote("L1", 20)
    lote.reponer(10)
    assert lote.disponible == 30


def test_reponer_cero_o_negativo_lanza_error():
    lote = modulo.Lote("L1", 20)
    with pytest.raises(ValueError):
        lote.reponer(0)
    with pytest.raises(ValueError):
        lote.reponer(-3)
    assert lote.disponible == 20
