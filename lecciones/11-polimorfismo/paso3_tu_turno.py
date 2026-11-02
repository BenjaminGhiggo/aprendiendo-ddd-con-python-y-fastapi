# paso3_tu_turno.py — PASO 3 de la Lección 11 (pair programming).
# Completa cada # TODO reemplazando el "pass". Luego comprueba con pytest:
#   uv run pytest lecciones/11-polimorfismo -q
# Al principio los tests salen en ROJO (fallan): es a propósito. Cuando completes
# los TODO deben salir en VERDE: "5 passed".
# Si te trabas, mira la fórmula indicada entre paréntesis en el README (§5 y §6).
# Cuando termines, compara con paso4_tu_turno_solucion.py.


# Estas dos figuras ya están listas: no las cambies.
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def nombre(self):
        return "cuadrado"


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(3.14 * self.radio * self.radio, 2)

    def nombre(self):
        return "círculo"


# TODO 1: completa Triangulo para que cumpla el MISMO contrato que las otras (P1, C1):
#         - __init__ guarda base y altura,
#         - area() devuelve base * altura / 2,
#         - nombre() devuelve "triángulo".
class Triangulo:
    def __init__(self, base, altura):
        pass

    def area(self):
        pass

    def nombre(self):
        pass


# TODO 2: total_areas(figuras) suma el area() de TODAS las figuras SIN preguntar su tipo
#         (P3) y devuelve round(total, 2). Con una lista vacía debe devolver 0.
def total_areas(figuras):
    pass


# TODO 3: nombres(figuras) devuelve una LISTA con el nombre() de cada figura, en orden.
#         Ej.: nombres([Cuadrado(1), Circulo(1)]) -> ["cuadrado", "círculo"]
def nombres(figuras):
    pass


# Comprobación esperada (cuando completes los TODO):
#   uv run pytest lecciones/11-polimorfismo -q   ->   5 passed
