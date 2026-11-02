# paso4_tu_turno_solucion.py — PASO 4 de la Lección 13: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/13-srp/paso3_tu_turno.py lecciones/13-srp/paso4_tu_turno_solucion.py
# Si tu versión es distinta pero los tests pasan, también está bien.


class Factura:
    """Regla de negocio: SOLO sabe calcular su total."""

    def __init__(self, precios):
        self.precios = precios

    def total(self):
        # TODO 1: devuelve la suma de self.precios (receta S1).
        return sum(self.precios)


def formatear_factura(factura):
    """Presentación: SOLO arma el texto. Debe devolver, por ejemplo, "Total: 60"."""
    # TODO 2: devuelve el texto "Total: " seguido del total de la factura.
    return f"Total: {factura.total()}"


class RepositorioFacturas:
    """Persistencia: SOLO guarda y cuenta facturas (receta S2)."""

    def __init__(self):
        # TODO 3: crea una lista vacía en self._facturas.
        self._facturas = []

    def guardar(self, factura):
        # TODO 4: agrega la factura a self._facturas.
        self._facturas.append(factura)

    def contar(self):
        # TODO 5: devuelve cuántas facturas hay guardadas.
        return len(self._facturas)
