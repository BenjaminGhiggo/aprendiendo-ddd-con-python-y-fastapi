# paso4_tu_turno_solucion.py — PASO 4 de la Lección 08: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index paso3_tu_turno.py paso4_tu_turno_solucion.py
# Para ver las pruebas en verde con esta solución, en test_paso3_tu_turno.py cambia
# "import paso3_tu_turno as modulo" por "import paso4_tu_turno_solucion as modulo".


class SinStock(Exception):        # ya está hecho: lo usa la prueba de asignar
    pass


def total(precio, cantidad):
    # TODO 1: devuelve precio * cantidad (F5 de la Lección 04).
    return precio * cantidad


def puede_asignar(disponible, pedido):
    # TODO 2: devuelve True si disponible >= pedido; si no, False.
    return disponible >= pedido


def asignar(disponible, pedido):
    # TODO 3: si pedido > disponible, LANZA SinStock("Sin stock para " + str(pedido)).
    if pedido > disponible:
        raise SinStock("Sin stock para " + str(pedido))
    # TODO 4: si alcanza, devuelve disponible - pedido.
    return disponible - pedido


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
