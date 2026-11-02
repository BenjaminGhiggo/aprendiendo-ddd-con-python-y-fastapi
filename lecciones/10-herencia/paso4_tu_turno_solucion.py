# paso4_tu_turno_solucion.py — PASO 4 de la Lección 10: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/10-herencia/paso3_tu_turno.py lecciones/10-herencia/paso4_tu_turno_solucion.py
# Si tu versión es distinta pero los tests pasan, también está bien.


# La clase PADRE ya está lista: no la cambies.
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad

    def descripcion(self):
        return f"Lote {self.referencia} con {self.cantidad} unidades"


class LoteFragil(Lote):
    def __init__(self, referencia, cantidad, max_apilable):
        super().__init__(referencia, cantidad)        # TODO 1 (H4)
        self.max_apilable = max_apilable              # TODO 2 (H5)

    def descripcion(self):                            # TODO 3 (H8): extender
        return super().descripcion() + f" ⚠️ frágil (máx. {self.max_apilable} apilados)"

    def puede_apilar(self, n):                        # TODO 4 (H6): método nuevo
        return n <= self.max_apilable


# Comprobación esperada:
#   uv run pytest lecciones/10-herencia -q   ->   5 passed
