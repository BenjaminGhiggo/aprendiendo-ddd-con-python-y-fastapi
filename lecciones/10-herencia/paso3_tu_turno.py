# paso3_tu_turno.py — PASO 3 de la Lección 10 (pair programming).
# Completa cada # TODO reemplazando el "pass". Luego comprueba con pytest:
#   uv run pytest lecciones/10-herencia -q
# Al principio los tests salen en ROJO (fallan): es a propósito. Cuando completes
# los TODO deben salir en VERDE: "5 passed".
# Si te trabas, mira la fórmula indicada entre paréntesis en el README (§5 y §6).
# Cuando termines, compara con paso4_tu_turno_solucion.py.


# La clase PADRE ya está lista: no la cambies.
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad

    def descripcion(self):
        return f"Lote {self.referencia} con {self.cantidad} unidades"


# La clase HIJA ya hereda de Lote (fíjate en el paréntesis). Complétala.
class LoteFragil(Lote):
    def __init__(self, referencia, cantidad, max_apilable):
        # TODO 1: reutiliza el constructor del padre con super().__init__(...) (fórmula H4).
        # TODO 2: guarda max_apilable en self.max_apilable (H5).
        pass

    # TODO 3: EXTIENDE la descripción del padre (H8). Debe devolver, por ejemplo:
    #         "Lote F1 con 8 unidades ⚠️ frágil (máx. 3 apilados)"
    def descripcion(self):
        pass

    # TODO 4: método NUEVO (H6): devuelve True si n es menor o igual a self.max_apilable,
    #         y False si no.
    def puede_apilar(self, n):
        pass


# Comprobación esperada (cuando completes los TODO):
#   uv run pytest lecciones/10-herencia -q   ->   5 passed
