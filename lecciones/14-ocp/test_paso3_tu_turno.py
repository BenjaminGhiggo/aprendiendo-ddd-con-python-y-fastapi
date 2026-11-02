# test_paso3_tu_turno.py — los tests de tu turno (Lección 14 · OCP).
# Empiezan en ROJO a propósito (TDD): pasan a VERDE cuando completas los # TODO de paso3.
# Ejecuta:  uv run pytest lecciones/14-ocp -q
#
# Para ver la referencia en verde, cambia a `import paso4_tu_turno_solucion as modulo`.
import paso3_tu_turno as modulo


def test_descuento_vip_cobra_el_70_por_ciento():
    assert modulo.descuento_vip(100) == 70.0


def test_vip_esta_registrado_y_el_nucleo_lo_usa_sin_cambios():
    assert modulo.precio_con_codigo(100, "vip") == 70.0


def test_los_descuentos_viejos_siguen_funcionando():
    # Extender no debe romper lo que ya andaba.
    assert modulo.precio_con_codigo(100, "10") == 90.0
    assert modulo.precio_con_codigo(100, "ninguno") == 100


def test_envio_express_cuesta_20():
    assert modulo.EnvioExpress().costo() == 20


def test_el_nucleo_de_envios_acepta_el_tipo_nuevo():
    assert modulo.total_con_envio(100, modulo.EnvioExpress()) == 120
    assert modulo.total_con_envio(100, modulo.EnvioNormal()) == 110
