# paso1_formulas.py — PASO 1 de la Lección 09 (Encapsulación).
# Cada bloque es una "fórmula" de las tablas del README (§5 y §6), con su código (E1, P1...).
# Ejecuta:  uv run python lecciones/09-encapsulacion/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.


# ---- La clase de la lección: un Lote que PROTEGE su cantidad -------------------------
class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia      # E1 · atributo PÚBLICO: se puede leer desde afuera
        self._cantidad = cantidad         # E2 · atributo PROTEGIDO: el "_" avisa "no tocar"

    # E3 · método LECTOR: la puerta para LEER el dato protegido.
    def cantidad_disponible(self):
        return self._cantidad

    # E4 · método que CAMBIA el dato aplicando la regla.
    # E5 · la regla se revisa ANTES de cambiar: si no se cumple, se lanza un error
    #      y el dato queda como estaba (la "invariante" se protege).
    def asignar(self, pedido):
        if pedido > self._cantidad:
            raise ValueError("No hay stock suficiente")
        self._cantidad = self._cantidad - pedido

    # P1 · PROPIEDAD de solo lectura: se usa como un atributo (SIN paréntesis),
    #      pero por dentro es un método. Así lo hace el libro con available_quantity.
    @property
    def disponible(self):
        return self._cantidad


print("========== ATRIBUTOS Y MÉTODOS ==========")
lote = Lote("L1", 20)

print("E1  lote.referencia:            ", lote.referencia)
print("E2  lote._cantidad (no se toca):", lote._cantidad)
print("E3  lote.cantidad_disponible(): ", lote.cantidad_disponible())

lote.asignar(5)
print("E4  asignar(5) -> disponible:   ", lote.cantidad_disponible())

try:
    lote.asignar(999)
except ValueError as error:
    print("E5  asignar(999) bloqueado:     ", error)
print("E5  ...y el dato sigue en:      ", lote.cantidad_disponible())

# E6 · Python NO impide tocar "_cantidad": es solo una CONVENCIÓN (un acuerdo entre
#      programadores). Lo mostramos en una copia para no romper "lote".
otro = Lote("L2", 20)
otro._cantidad = -999
print("E6  otro._cantidad = -999:      ", otro.cantidad_disponible(), "<- ¡estado imposible!")

print()
print("========== @property Y SETTER ==========")

# P1 · leer una propiedad: SIN paréntesis.
print("P1  lote.disponible:            ", lote.disponible)

# P2 · una propiedad sin setter NO se puede asignar.
try:
    lote.disponible = 100
except AttributeError as error:
    print("P2  lote.disponible = 100:      ", error)


# P3 · propiedad CALCULADA: no guarda nada, calcula al momento (como el libro:
#      available_quantity = _purchased_quantity - allocated_quantity).
class LoteConAsignado:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self._comprada = cantidad
        self._asignada = 0

    def asignar(self, pedido):
        if pedido > self.disponible:
            raise ValueError("No hay stock suficiente")
        self._asignada = self._asignada + pedido

    @property
    def disponible(self):
        return self._comprada - self._asignada


calc = LoteConAsignado("L3", 20)
calc.asignar(5)
calc.asignar(3)
print("P3  comprada 20, asignada 8 ->  ", calc.disponible)


# P4 · SETTER con validación: permite ASIGNAR (=) pero revisando la regla.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio          # ¡esto ya pasa por el setter de abajo!

    @property
    def precio(self):                 # lector
        return self._precio

    @precio.setter
    def precio(self, valor):          # escritor con regla
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor          # se guarda en _precio (con guion bajo)


mesa = Producto("mesa", 100)
mesa.precio = 120
print("P4  mesa.precio = 120:          ", mesa.precio)

# P5 · el setter rechaza un valor inválido.
try:
    mesa.precio = -5
except ValueError as error:
    print("P5  mesa.precio = -5:           ", error)
print("P5  ...y el precio sigue en:    ", mesa.precio)

# P6 · el setter también protege al CREAR el objeto (porque __init__ usa self.precio = ...).
try:
    Producto("silla", -1)
except ValueError as error:
    print("P6  Producto('silla', -1):      ", error)

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Quita el # de UNA línea, ejecuta y lee el mensaje.
# print(lote.disponible())   # X2 -> TypeError: 'int' object is not callable
# lote.disponible = 100      # X3 -> AttributeError: property 'disponible' of 'Lote' object has no setter
# ---------------------------------------------------------------------------
