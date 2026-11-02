# paso4_tu_turno_solucion.py — PASO 4 de la Lección 11: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/11-polimorfismo/paso3_tu_turno.py lecciones/11-polimorfismo/paso4_tu_turno_solucion.py
# Si tu versión es distinta pero los tests pasan, también está bien.


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


# TODO 1: el mismo contrato (area y nombre), su propia fórmula.
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

    def nombre(self):
        return "triángulo"


# TODO 2: no pregunta el tipo; solo exige area().
def total_areas(figuras):
    total = 0
    for figura in figuras:
        total = total + figura.area()
    return round(total, 2)


# TODO 3: junta los nombres en una lista.
def nombres(figuras):
    resultado = []
    for figura in figuras:
        resultado.append(figura.nombre())
    return resultado


# Comprobación esperada:
#   uv run pytest lecciones/11-polimorfismo -q   ->   5 passed
