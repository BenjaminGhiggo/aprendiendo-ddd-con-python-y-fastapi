# paso3_tu_turno.py — PASO 3 de la Lección 14 (OCP · pair programming).
# La comprobación es con PYTEST (TDD): los tests ya están en test_paso3_tu_turno.py y
# empiezan en ROJO. Completa los # TODO hasta verlos en VERDE:
#   uv run pytest lecciones/14-ocp -q
# REGLA DE ESTE EJERCICIO: NO edites las funciones marcadas "NÚCLEO (cerrado)".
# Todo lo nuevo se agrega con código NUEVO (eso es el OCP).


def sin_descuento(precio):
    return precio


def descuento_10(precio):
    return precio * 0.9


DESCUENTOS = {"ninguno": sin_descuento, "10": descuento_10}


def precio_con_codigo(precio, codigo):
    """NÚCLEO (cerrado): no lo edites."""
    return DESCUENTOS[codigo](precio)


def descuento_vip(precio):
    # TODO 1: devuelve el precio con 30 % de descuento (paga el 70 %): precio * 70 / 100.
    return None


# TODO 2: registra descuento_vip en DESCUENTOS con la clave "vip" (receta O3).
#         (una sola línea, debajo de este comentario)


class Envio:
    def costo(self):
        return 0


class EnvioNormal(Envio):
    def costo(self):
        return 10


class EnvioExpress(Envio):
    def costo(self):
        # TODO 3: el envío express cuesta 20 (receta O2).
        return None


def total_con_envio(precio, envio):
    """NÚCLEO (cerrado): no lo edites."""
    return precio + envio.costo()
