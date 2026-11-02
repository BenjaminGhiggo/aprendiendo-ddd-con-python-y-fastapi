# test_paso3_tu_turno.py — las pruebas de tu paso3 (Lección 11).
# Ejecuta:  uv run pytest lecciones/11-polimorfismo -q
# ROJO al principio (los TODO están vacíos) -> VERDE cuando los completes.
#
# Para ver la referencia en verde, cambia la línea de abajo a:
#   import paso4_tu_turno_solucion as modulo
import paso3_tu_turno as modulo


def test_triangulo_calcula_su_area():
    assert modulo.Triangulo(4, 3).area() == 6.0


def test_triangulo_dice_su_nombre():
    assert modulo.Triangulo(4, 3).nombre() == "triángulo"


def test_total_areas_mezcla_figuras_distintas():
    figuras = [modulo.Cuadrado(2), modulo.Triangulo(4, 3), modulo.Circulo(1)]
    assert modulo.total_areas(figuras) == 13.14          # 4 + 6 + 3.14


def test_total_areas_de_una_lista_vacia_es_cero():
    assert modulo.total_areas([]) == 0


def test_nombres_en_orden():
    figuras = [modulo.Cuadrado(1), modulo.Circulo(1), modulo.Triangulo(1, 1)]
    assert modulo.nombres(figuras) == ["cuadrado", "círculo", "triángulo"]
