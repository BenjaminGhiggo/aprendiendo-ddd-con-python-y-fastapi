# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 09.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/09-encapsulacion/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: esconder el dato y abrir puertas (fácil) ---")


class Lote:                                    # Paso 1: la clase (el molde)
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self._cantidad = cantidad              # Paso 2: el dato protegido (E2)

    def cantidad_disponible(self):             # Paso 3: puerta para leer (E3)
        return self._cantidad

    def asignar(self, pedido):                 # Paso 4: puerta para cambiar (E4)
        if pedido > self._cantidad:
            raise ValueError("No hay stock suficiente")
        self._cantidad = self._cantidad - pedido


lote = Lote("LOTE-001", 20)                    # Paso 5: la instancia (el objeto)
print(lote.cantidad_disponible())              # -> 20
lote.asignar(5)                                # Paso 6: usarlo solo por sus puertas
print(lote.cantidad_disponible())              # -> 15

print()
print("--- Ejemplo 2: la regla protege el estado (fácil) ---")
lote = Lote("LOTE-002", 10)
try:
    lote.asignar(25)                           # Paso 1: pedido imposible
except ValueError as error:                    # Paso 2: atrapamos el error (Lección 07)
    print("Bloqueado:", error)                 # -> Bloqueado: No hay stock suficiente
print(lote.cantidad_disponible())              # Paso 3: sigue en 10: NO se corrompió

print()
print("--- Ejemplo 3: de método lector a @property calculada (intermedio) ---")


class LoteConAsignado:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self._comprada = cantidad              # Paso 1: lo que se compró
        self._asignada = 0                     # Paso 2: lo asignado empieza en 0

    def asignar(self, pedido):
        if pedido > self.disponible:           # Paso 4: la regla usa la propiedad
            raise ValueError("No hay stock suficiente")
        self._asignada = self._asignada + pedido

    @property
    def disponible(self):                      # Paso 3: se CALCULA, no se guarda
        return self._comprada - self._asignada


lote = LoteConAsignado("LOTE-003", 20)
lote.asignar(5)
lote.asignar(3)
print(lote.disponible)                         # Paso 5: SIN paréntesis -> 12

print()
print("--- Ejemplo 4: setter que valida al asignar y al crear (avanzado) ---")


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio                   # Paso 3: hasta el __init__ pasa por el setter

    @property
    def precio(self):                          # Paso 1: el lector
        return self._precio

    @precio.setter
    def precio(self, valor):                   # Paso 2: el escritor con regla
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor


mesa = Producto("mesa", 100)
mesa.precio = 120                              # Paso 4: cambio válido
print(mesa.precio)                             # -> 120
try:
    mesa.precio = -5                           # Paso 5: cambio inválido
except ValueError as error:
    print("Bloqueado:", error)                 # -> Bloqueado: El precio no puede ser negativo
print(mesa.precio)                             # -> 120 (no cambió)
try:
    Producto("silla", -1)                      # Paso 6: también protege al crear
except ValueError as error:
    print("Bloqueado al crear:", error)
