# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 06.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/06-clases-y-objetos/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: clase -> instancia -> objeto -> uso (fácil) ---")


class Producto:                          # Paso 1: CLASE = el molde (C1)
    def __init__(self, nombre, precio):  # Paso 2: __init__ recibe los datos (C2)
        self.nombre = nombre             # Paso 3: guardarlos DENTRO (C3)
        self.precio = precio


mesa = Producto("mesa", 120)             # Paso 4: INSTANCIA concreta (C4)
print(mesa.nombre)                       # Paso 5: OBJETO en uso: leer (C5) -> mesa
print(mesa.precio)                       #                                -> 120

print()
print("--- Ejemplo 2: un método que usa los datos del objeto (fácil) ---")


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):                      # Paso 1: método; usa self.base y self.altura (C7)
        return self.base * self.altura


r = Rectangulo(3, 4)                     # Paso 2: crear
print(r.area())                          # Paso 3: llamar al método (C8) -> 12

print()
print("--- Ejemplo 3: un método que cambia el estado (intermedio) ---")


class Lote:
    def __init__(self, referencia, cantidad):
        self.referencia = referencia
        self.cantidad = cantidad

    def puede_asignar(self, pedido):
        return self.cantidad >= pedido

    def asignar(self, pedido):                   # usa OTRO método (C11)
        if self.puede_asignar(pedido):
            self.cantidad = self.cantidad - pedido   # cambia el estado (C9)


lote = Lote("LOTE-001", 20)
for pedido in [5, 30, 15]:
    lote.asignar(pedido)
    print("pedido", pedido, "-> queda", lote.cantidad)
# -> pedido 5 -> queda 15 / pedido 30 -> queda 15 / pedido 15 -> queda 0

print()
print("--- Ejemplo 4: dos clases como en la Figura 1-3 del libro (avanzado) ---")


class LineaPedido:                       # = OrderLine: orderid, sku, qty
    def __init__(self, id_pedido, sku, cantidad):
        self.id_pedido = id_pedido
        self.sku = sku
        self.cantidad = cantidad


class LoteConAsignaciones:               # = Batch: reference, sku, _purchased_quantity, _allocations
    def __init__(self, referencia, sku, cantidad_comprada):
        self.referencia = referencia
        self.sku = sku
        self.cantidad_comprada = cantidad_comprada
        self.asignaciones = []           # Paso 1: una LISTA de LineaPedido (el rombo de la figura)

    def cantidad_disponible(self):       # Paso 2: se CALCULA recorriendo las asignaciones
        asignado = 0
        for linea in self.asignaciones:
            asignado = asignado + linea.cantidad
        return self.cantidad_comprada - asignado

    def puede_asignar(self, linea):      # Paso 3: mismo sku Y alcanza (como can_allocate)
        return self.sku == linea.sku and self.cantidad_disponible() >= linea.cantidad

    def asignar(self, linea):            # Paso 4: si puede, guarda la línea dentro del lote
        if self.puede_asignar(linea):
            self.asignaciones.append(linea)


lote = LoteConAsignaciones("LOTE-001", "MESA", 20)
lote.asignar(LineaPedido("pedido-1", "MESA", 8))
lote.asignar(LineaPedido("pedido-2", "SILLA", 3))   # otro sku: no se asigna
lote.asignar(LineaPedido("pedido-3", "MESA", 5))
print("líneas asignadas:", len(lote.asignaciones))  # -> 2
print("disponible:", lote.cantidad_disponible())     # -> 7
