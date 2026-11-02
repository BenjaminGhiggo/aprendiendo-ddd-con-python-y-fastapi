# test_paso3_tu_turno.py — las pruebas de tu paso3 (Lección 12).
# Ejecuta:  uv run pytest lecciones/12-abstraccion -q
# ROJO al principio (los TODO están vacíos) -> VERDE cuando los completes.
#
# Para ver la referencia en verde, cambia la línea de abajo a:
#   import paso4_tu_turno_solucion as modulo
import pytest

import paso3_tu_turno as modulo


def test_el_contrato_no_se_puede_instanciar():
    # Esta ya pasa: el contrato viene escrito. Te muestra cómo se prueba un TypeError.
    with pytest.raises(TypeError):
        modulo.RepositorioAbstracto()


def test_repositorio_lista_cumple_el_contrato():
    assert isinstance(modulo.RepositorioLista(), modulo.RepositorioAbstracto)


def test_agregar_y_obtener():
    repo = modulo.RepositorioLista()
    lote = modulo.Lote("L1", 10)
    repo.agregar(lote)
    assert repo.obtener("L1") is lote


def test_obtener_una_referencia_que_no_existe():
    repo = modulo.RepositorioLista()
    repo.agregar(modulo.Lote("L1", 10))
    assert repo.obtener("L1").cantidad == 10
    assert repo.obtener("NO-EXISTE") is None


def test_listar_devuelve_las_referencias_en_orden():
    repo = modulo.RepositorioLista()
    repo.agregar(modulo.Lote("L1", 10))
    repo.agregar(modulo.Lote("L2", 5))
    assert repo.listar() == ["L1", "L2"]
