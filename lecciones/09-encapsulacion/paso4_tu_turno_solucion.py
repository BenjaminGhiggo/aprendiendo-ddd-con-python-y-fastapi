# paso4_tu_turno_solucion.py — PASO 4 de la Lección 09: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index lecciones/09-encapsulacion/paso3_tu_turno.py lecciones/09-encapsulacion/paso4_tu_turno_solucion.py
# Si tu versión es distinta pero los tests pasan, también está bien.


class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self._cantidad = cantidad          # protegido: solo se cambia por los métodos

    # TODO 1: propiedad de solo lectura (P1).
    @property
    def disponible(self):
        return self._cantidad

    # TODO 2: la regla se revisa ANTES de cambiar (E4, E5).
    def asignar(self, pedido):
        if pedido > self._cantidad:
            raise ValueError("No hay stock suficiente")
        self._cantidad = self._cantidad - pedido

    # TODO 3: reponer solo cantidades positivas.
    def reponer(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._cantidad = self._cantidad + cantidad


# Comprobación esperada:
#   uv run pytest lecciones/09-encapsulacion -q   ->   5 passed
