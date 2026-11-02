# test_paso3_tu_turno.py — las pruebas de tu paso3 (Lección 10).
# Ejecuta:  uv run pytest lecciones/10-herencia -q
# ROJO al principio (los TODO están vacíos) -> VERDE cuando los completes.
#
# Para ver la referencia en verde, cambia la línea de abajo a:
#   import paso4_tu_turno_solucion as modulo
import paso3_tu_turno as modulo


def test_lote_fragil_es_un_lote():
    fragil = modulo.LoteFragil("F1", 8, 3)
    assert isinstance(fragil, modulo.Lote)        # la hija ES un Lote (T2)


def test_reutiliza_el_constructor_del_padre():
    fragil = modulo.LoteFragil("F1", 8, 3)
    assert fragil.referencia == "F1"
    assert fragil.cantidad == 8


def test_guarda_el_dato_nuevo():
    fragil = modulo.LoteFragil("F1", 8, 3)
    assert fragil.max_apilable == 3


def test_descripcion_extiende_la_del_padre():
    fragil = modulo.LoteFragil("F1", 8, 3)
    assert fragil.descripcion() == "Lote F1 con 8 unidades ⚠️ frágil (máx. 3 apilados)"


def test_puede_apilar():
    fragil = modulo.LoteFragil("F1", 8, 3)
    assert fragil.puede_apilar(3) is True
    assert fragil.puede_apilar(4) is False
