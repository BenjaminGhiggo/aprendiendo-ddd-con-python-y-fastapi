# test_paso3_tu_turno.py — las PRUEBAS de paso3_tu_turno.py (escritas ANTES, TDD).
#
# Corre:  uv run pytest lecciones/08-modulos-y-pytest/test_paso3_tu_turno.py -v
# Al principio: 5 failed (ROJO, a propósito). Cuando completes los TODO: 5 passed (VERDE).
#
# Para ver la referencia en verde, cambia la línea de abajo a:
#   import paso4_tu_turno_solucion as modulo
import pytest

import paso3_tu_turno as modulo


def test_total_multiplica_precio_por_cantidad():
    assert modulo.total(15, 4) == 60


def test_puede_asignar_si_alcanza():
    assert modulo.puede_asignar(20, 5) is True


def test_no_puede_asignar_si_no_alcanza():
    assert modulo.puede_asignar(10, 25) is False


def test_asignar_resta_del_stock():
    assert modulo.asignar(20, 5) == 15


def test_asignar_sin_stock_lanza_error():
    with pytest.raises(modulo.SinStock, match="Sin stock para 25"):
        modulo.asignar(10, 25)
