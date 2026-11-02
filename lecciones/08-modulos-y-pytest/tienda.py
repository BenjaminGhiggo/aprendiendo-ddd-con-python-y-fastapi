# tienda.py  -> un MÓDULO: un archivo .py con código reutilizable.
# Otros archivos lo usan con "import tienda" o "from tienda import asignar".
# (Es el "módulo de apoyo" de la Lección 08: lo importan paso1_formulas.py y test_tienda.py.)


class SinStock(Exception):
    pass


def asignar(disponible, pedido):
    """Devuelve el stock restante después de asignar un pedido."""
    return disponible - pedido


def puede_asignar(disponible, pedido):
    """Responde si hay stock suficiente para el pedido."""
    return disponible >= pedido


def asignar_estricto(disponible, pedido):
    """Como asignar, pero lanza SinStock si no alcanza (Lección 07)."""
    if pedido > disponible:
        raise SinStock("Sin stock: piden " + str(pedido) + " y hay " + str(disponible))
    return disponible - pedido


# M7 · Este bloque SOLO corre si ejecutas este archivo directamente:
#        uv run python lecciones/08-modulos-y-pytest/tienda.py
#      Cuando otro archivo hace "import tienda", este bloque NO corre.
if __name__ == "__main__":
    print("probando tienda.py directamente:", asignar(20, 5))
