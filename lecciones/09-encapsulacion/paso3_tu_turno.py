# paso3_tu_turno.py — PASO 3 de la Lección 09 (pair programming).
# Completa cada # TODO reemplazando el "pass". Luego comprueba con pytest:
#   uv run pytest lecciones/09-encapsulacion -q
# Al principio los tests salen en ROJO (fallan): es a propósito. Cuando completes
# los TODO deben salir en VERDE: "5 passed".
# Si te trabas, mira la fórmula indicada entre paréntesis en el README (§5 y §6).
# Cuando termines, compara con paso4_tu_turno_solucion.py.


class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self._cantidad = cantidad          # protegido: solo se cambia por los métodos

    # TODO 1: convierte este método en una PROPIEDAD de solo lectura (fórmula P1):
    #         escribe @property en la línea de arriba del "def" y devuelve self._cantidad.
    #         Uso esperado: Lote("L1", 20).disponible  -> 20   (sin paréntesis)
    def disponible(self):
        pass

    # TODO 2: asignar(pedido) (fórmulas E4 y E5):
    #         - si pedido es MAYOR que self._cantidad, lanza ValueError("No hay stock suficiente")
    #           ANTES de cambiar nada;
    #         - si no, resta pedido de self._cantidad.
    def asignar(self, pedido):
        pass

    # TODO 3: reponer(cantidad):
    #         - si cantidad es menor o igual a 0, lanza ValueError("La cantidad debe ser positiva");
    #         - si no, suma cantidad a self._cantidad.
    def reponer(self, cantidad):
        pass


# Comprobación esperada (cuando completes los TODO):
#   uv run pytest lecciones/09-encapsulacion -q   ->   5 passed
