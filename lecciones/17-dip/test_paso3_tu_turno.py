# test_paso3_tu_turno.py — los tests de tu turno (Lección 17 · DIP ⭐).
# Empiezan en ROJO a propósito (TDD): pasan a VERDE cuando completas los # TODO de paso3.
# Ejecuta:  uv run pytest lecciones/17-dip -q
#
# Para ver la referencia en verde, cambia a `import paso4_tu_turno_solucion as modulo`.
import paso3_tu_turno as modulo


def test_el_notificador_falso_guarda_lo_que_se_envia():
    falso = modulo.NotificadorFalso()
    falso.enviar("hola")
    assert falso.enviados == ["hola"]


def test_avisar_sin_stock_usa_el_notificador_inyectado():
    falso = modulo.NotificadorFalso()
    modulo.avisar_sin_stock("MESA", falso)
    assert falso.enviados == ["Sin stock: MESA"]


def test_el_servicio_usa_el_repositorio_que_le_inyectan():
    repo = modulo.RepositorioEnMemoria()
    servicio = modulo.ServicioPedidos(repo)
    assert servicio.repo is repo            # el MISMO objeto: no creó otro adentro


def test_el_servicio_registra_con_cualquier_repositorio():
    class RepositorioFalso(modulo.RepositorioAbstracto):
        def __init__(self):
            self._datos = set()

        def agregar(self, ref):
            self._datos.add(ref)

        def obtener(self, ref):
            return ref if ref in self._datos else None

    assert modulo.ServicioPedidos(modulo.RepositorioEnMemoria()).registrar("L1") == "L1"
    assert modulo.ServicioPedidos(RepositorioFalso()).registrar("L2") == "L2"
