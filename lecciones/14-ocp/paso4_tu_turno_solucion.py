# paso4_tu_turno_solucion.py — PASO 4 de la Lección 14: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/14-ocp/paso3_tu_turno.py lecciones/14-ocp/paso4_tu_turno_solucion.py
# Fíjate: las funciones "NÚCLEO (cerrado)" son IDÉNTICAS en ambos archivos.


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
    return precio * 70 / 100


# TODO 2: registra descuento_vip en DESCUENTOS con la clave "vip" (receta O3).
#         (una sola línea, debajo de este comentario)
DESCUENTOS["vip"] = descuento_vip


class Envio:
    def costo(self):
        return 0


class EnvioNormal(Envio):
    def costo(self):
        return 10


class EnvioExpress(Envio):
    def costo(self):
        # TODO 3: el envío express cuesta 20 (receta O2).
        return 20


def total_con_envio(precio, envio):
    """NÚCLEO (cerrado): no lo edites."""
    return precio + envio.costo()
