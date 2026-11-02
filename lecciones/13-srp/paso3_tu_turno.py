# paso3_tu_turno.py — PASO 3 de la Lección 13 (SRP · pair programming).
# Hoy la comprobación es con PYTEST (TDD): los tests ya están escritos en
# test_paso3_tu_turno.py y empiezan en ROJO. Completa los # TODO hasta que pasen a VERDE:
#   uv run pytest lecciones/13-srp -q
# Pista: cada pieza debe tener UNA sola razón para cambiar (README §5, recetas S1 y S2).


class Factura:
    """Regla de negocio: SOLO sabe calcular su total."""

    def __init__(self, precios):
        self.precios = precios

    def total(self):
        # TODO 1: devuelve la suma de self.precios (receta S1).
        return None


def formatear_factura(factura):
    """Presentación: SOLO arma el texto. Debe devolver, por ejemplo, "Total: 60"."""
    # TODO 2: devuelve el texto "Total: " seguido del total de la factura.
    return None


class RepositorioFacturas:
    """Persistencia: SOLO guarda y cuenta facturas (receta S2)."""

    def __init__(self):
        # TODO 3: crea una lista vacía en self._facturas.
        pass

    def guardar(self, factura):
        # TODO 4: agrega la factura a self._facturas.
        pass

    def contar(self):
        # TODO 5: devuelve cuántas facturas hay guardadas.
        return None


# ¡OJO! No agregues métodos para imprimir ni para guardar dentro de Factura:
# los tests comprueban que Factura NO los tenga (eso sería violar el SRP).
