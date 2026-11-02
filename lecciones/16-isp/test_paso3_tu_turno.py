# test_paso3_tu_turno.py — los tests de tu turno (Lección 16 · ISP).
# Empiezan en ROJO a propósito (TDD): pasan a VERDE cuando completas los # TODO de paso3.
# Ejecuta:  uv run pytest lecciones/16-isp -q
#
# Para ver la referencia en verde, cambia a `import paso4_tu_turno_solucion as modulo`.
import paso3_tu_turno as modulo


def test_respaldo_solo_usa_agregar():
    repo = modulo.Repositorio()
    assert modulo.respaldo(repo, "L1") == "respaldado: L1"
    assert repo.obtener("L1") == "L1"


def test_repositorio_guarda_y_devuelve_y_none_si_no_esta():
    repo = modulo.Repositorio()
    repo.agregar("A")
    assert repo.obtener("A") == "A"
    assert repo.obtener("NO") is None


def test_solo_lectura_sirve_para_el_reporte():
    assert modulo.reporte(modulo.SoloLectura(), "X") == "Encontrado: solo-lectura:X"


def test_solo_lectura_no_carga_metodos_que_no_usa():
    solo = modulo.SoloLectura()
    assert isinstance(solo, modulo.Lector)
    assert not isinstance(solo, modulo.Escritor)
    assert not hasattr(solo, "agregar")


def test_repositorio_cumple_las_dos_interfaces():
    repo = modulo.Repositorio()
    assert isinstance(repo, modulo.Lector)
    assert isinstance(repo, modulo.Escritor)
