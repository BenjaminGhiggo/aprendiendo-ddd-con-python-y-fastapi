# paso1_formulas.py — PASO 1 de la Lección 10 (Herencia).
# Cada bloque es una "fórmula" de las tablas del README (§5 y §6), con su código (H1, T1...).
# Ejecuta:  uv run python lecciones/10-herencia/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.


# H1 · clase PADRE (también se dice "madre" o "base").
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad

    def descripcion(self):
        return f"Lote {self.referencia} con {self.cantidad} unidades"

    def etiqueta(self):
        return "NORMAL"


# H2 · clase HIJA: el padre va entre paréntesis. Con "pass" no agrega nada:
#      igual tiene TODO lo del padre (H3).
class LoteSimple(Lote):
    pass


# Una hija que SÍ agrega cosas:
class LoteRefrigerado(Lote):
    def __init__(self, referencia, cantidad, temperatura):
        super().__init__(referencia, cantidad)    # H4 · reutiliza el __init__ del padre
        self.temperatura = temperatura            # H5 · agrega un atributo nuevo

    def esta_congelado(self):                     # H6 · método NUEVO (solo la hija lo tiene)
        return self.temperatura < 0

    def etiqueta(self):                           # H7 · SOBRESCRIBE: reemplaza al del padre
        return "FRÍO"

    def descripcion(self):                        # H8 · EXTIENDE: usa el del padre y agrega
        return super().descripcion() + f" (a {self.temperatura}°C)"


normal = Lote("L1", 10)
simple = LoteSimple("L0", 3)
frio = LoteRefrigerado("L2", 5, -18)

print("========== CREAR UNA CLASE HIJA ==========")
print("H1  normal.descripcion():       ", normal.descripcion())
print("H2  LoteSimple(Lote): pass ->   ", type(simple).__name__)
print("H3  simple.descripcion():       ", simple.descripcion())
print("H4  frio.referencia:            ", frio.referencia)
print("H5  frio.temperatura:           ", frio.temperatura)
print("H6  frio.esta_congelado():      ", frio.esta_congelado())
print("H7  normal.etiqueta():          ", normal.etiqueta())
print("H7  frio.etiqueta():            ", frio.etiqueta())
print("H8  frio.descripcion():         ", frio.descripcion())
try:
    normal.esta_congelado()                       # H9 · el padre NO recibe lo de la hija
except AttributeError as error:
    print("H9  normal.esta_congelado():    ", error)

print()
print("========== PREGUNTAR POR EL TIPO ==========")
print("T1  isinstance(frio, LoteRefrigerado):  ", isinstance(frio, LoteRefrigerado))
print("T2  isinstance(frio, Lote):             ", isinstance(frio, Lote))
print("T3  isinstance(normal, LoteRefrigerado):", isinstance(normal, LoteRefrigerado))
print("T4  issubclass(LoteRefrigerado, Lote):  ", issubclass(LoteRefrigerado, Lote))
print("T5  type(frio).__name__:                ", type(frio).__name__)

# T6 · una lista puede mezclar padre e hijas; cada una usa SU versión del método.
print("T6  recorrer una lista mixta:")
for lote in [normal, simple, frio]:
    print("      ->", lote.etiqueta(), "|", lote.descripcion())

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están en paso1 como comentarios porque DETIENEN el programa.
# Copia UNA de estas clases a un archivo tuyo, ejecútala y lee el mensaje.
#
# X1 · olvidar super().__init__  -> AttributeError: 'SinSuper' object has no attribute 'referencia'
# class SinSuper(Lote):
#     def __init__(self, referencia, cantidad, temperatura):
#         self.temperatura = temperatura
# SinSuper("L", 1, 2).descripcion()
#
# X2 · pasar argumentos de menos -> TypeError: Lote.__init__() missing 1 required positional argument: 'cantidad'
# class Menos(Lote):
#     def __init__(self, referencia, cantidad, temperatura):
#         super().__init__(referencia)
# Menos("L", 1, 2)
#
# X3 · super sin paréntesis -> TypeError: descriptor '__init__' requires a 'super' object but received a 'str'
# class SinParentesis(Lote):
#     def __init__(self, referencia, cantidad, temperatura):
#         super.__init__(referencia, cantidad)
# SinParentesis("L", 1, 2)
# ---------------------------------------------------------------------------
