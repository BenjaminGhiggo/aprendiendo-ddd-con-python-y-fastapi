# paso3_tu_turno.py — PASO 3 de la Lección 08 (pair programming, con TDD).
#
# Este archivo es un MÓDULO: lo importa test_paso3_tu_turno.py. Las pruebas YA están
# escritas (como en el libro: "tests first"). Al principio fallan (ROJO) a propósito.
# Completa cada # TODO (reemplaza el "pass") hasta que TODAS pasen (VERDE):
#
#   uv run pytest lecciones/08-modulos-y-pytest/test_paso3_tu_turno.py -v
#
# Al empezar verás "5 failed"; al terminar, "5 passed".
# Cuando termines, compara con paso4_tu_turno_solucion.py.


class SinStock(Exception):        # ya está hecho: lo usa la prueba de asignar
    pass


def total(precio, cantidad):
    # TODO 1: devuelve precio * cantidad (F5 de la Lección 04).
    pass


def puede_asignar(disponible, pedido):
    # TODO 2: devuelve True si disponible >= pedido; si no, False.
    pass


def asignar(disponible, pedido):
    # TODO 3: si pedido > disponible, LANZA SinStock("Sin stock para " + str(pedido)).
    # TODO 4: si alcanza, devuelve disponible - pedido.
    pass


# Este bloque solo corre si ejecutas el archivo directamente (M7), no cuando pytest lo importa.
if __name__ == "__main__":
    print(total(15, 4))
    print(puede_asignar(20, 5))
    print(asignar(20, 5))
    try:
        asignar(10, 25)
    except SinStock as e:
        print("SinStock:", e)

# Salida esperada (con python, cuando completes los TODO):
# 60
# True
# 15
# SinStock: Sin stock para 25
