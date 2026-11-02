# test_paso3_tu_turno.py — los tests de tu turno (Lección 13 · SRP).
# Empiezan en ROJO a propósito (TDD): pasan a VERDE cuando completas los # TODO de paso3.
# Ejecuta:  uv run pytest lecciones/13-srp -q
#
# Para ver la referencia en verde, cambia a `import paso4_tu_turno_solucion as modulo`.
import paso3_tu_turno as modulo


def test_la_factura_calcula_su_total():
    assert modulo.Factura([10, 20, 30]).total() == 60


def test_formatear_factura_arma_el_texto():
    assert modulo.formatear_factura(modulo.Factura([10, 20, 30])) == "Total: 60"


def test_el_repositorio_guarda_y_cuenta():
    repo = modulo.RepositorioFacturas()
    repo.guardar(modulo.Factura([1]))
    repo.guardar(modulo.Factura([2]))
    assert repo.contar() == 2


def test_la_factura_no_tiene_otras_responsabilidades():
    # SRP: Factura NO debe saber imprimirse ni guardarse.
    factura = modulo.Factura([1])
    assert not hasattr(factura, "guardar")
    assert not hasattr(factura, "imprimir")
    assert not hasattr(factura, "formatear")
