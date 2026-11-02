# test_paso3_tu_turno.py — los tests de tu turno (Lección 15 · LSP).
# Empiezan en ROJO a propósito (TDD): pasan a VERDE cuando completas los # TODO de paso3.
# Ejecuta:  uv run pytest lecciones/15-lsp -q
#
# Para ver la referencia en verde, cambia a `import paso4_tu_turno_solucion as modulo`.
import paso3_tu_turno as modulo


def probar_contrato(repo):
    """El MISMO test para cualquier repositorio: esto es un 'test de contrato'."""
    assert modulo.guardar_y_leer(repo, "L1") == "L1"
    assert repo.obtener("NO-EXISTE") is None


def test_la_referencia_cumple_el_contrato():
    probar_contrato(modulo.RepositorioEnMemoria())


def test_repositorio_lista_cumple_el_mismo_contrato():
    probar_contrato(modulo.RepositorioLista())


def test_repositorio_lista_sustituye_a_la_referencia():
    real = modulo.RepositorioEnMemoria()
    lista = modulo.RepositorioLista()
    for ref in ["A", "B"]:
        real.agregar(ref)
        lista.agregar(ref)
    for ref in ["A", "B", "C"]:
        assert lista.obtener(ref) == real.obtener(ref)


def test_cuadrado_calcula_su_area():
    assert modulo.Cuadrado(3).area() == 9


def test_cuadrado_es_figura_pero_no_rectangulo():
    cuadrado = modulo.Cuadrado(3)
    assert isinstance(cuadrado, modulo.Figura)
    assert not isinstance(cuadrado, modulo.Rectangulo)
