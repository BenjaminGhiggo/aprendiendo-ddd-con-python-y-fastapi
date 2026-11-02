# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 07.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/07-excepciones/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: lanzar y atrapar un ValueError (fácil) ---")


def validar_cantidad(cantidad):
    if cantidad < 0:                                       # Paso 1: detectar el problema
        raise ValueError("la cantidad no puede ser negativa")   # Paso 2: lanzar (X1)
    return cantidad


try:                                                       # Paso 3: intentar (X2)
    validar_cantidad(-3)
except ValueError as e:                                    # Paso 4: atrapar y leer (X3)
    print("Error:", e)                                     # -> Error: la cantidad no puede ser negativa

print()
print("--- Ejemplo 2: atrapar un KeyError al leer el stock (fácil) ---")
stock = {"mesa": 10, "silla": 25}
for producto in ["mesa", "cama"]:                          # Paso 1: dos consultas
    try:
        print(producto, "->", stock[producto])             # Paso 2: puede fallar
    except KeyError:
        print(producto, "-> no existe")                    # Paso 3: reacción (X9)

print()
print("--- Ejemplo 3: error propio + else + finally (intermedio) ---")


class SinStock(Exception):                                 # Paso 1: error del negocio (X4)
    pass


def asignar(disponible, pedido):
    if pedido > disponible:
        raise SinStock("pedido de " + str(pedido) + " supera " + str(disponible))   # Paso 2 (X5)
    return disponible - pedido


for pedido in [4, 25]:
    try:
        resto = asignar(10, pedido)                        # Paso 3: intentar
    except SinStock as e:
        print("pedido", pedido, "-> sin stock:", e)        # Paso 4a: falló
    else:
        print("pedido", pedido, "-> quedan", resto)        # Paso 4b: salió bien (X7)
    finally:
        print("pedido", pedido, "-> revisado")             # Paso 5: siempre (X8)

print()
print("--- Ejemplo 4: un allocate como el del libro (avanzado) ---")


class Lote:
    def __init__(self, referencia, sku, cantidad):
        self.referencia = referencia
        self.sku = sku
        self.cantidad = cantidad

    def puede_asignar(self, sku, cantidad):
        return self.sku == sku and self.cantidad >= cantidad


def asignar_a_lotes(sku, cantidad, lotes):
    for lote in lotes:                                     # Paso 1: recorrer los lotes
        if lote.puede_asignar(sku, cantidad):
            lote.cantidad = lote.cantidad - cantidad
            return lote.referencia                         # Paso 2: el primero que puede
    raise SinStock("Sin stock para el sku " + sku)         # Paso 3: ninguno pudo (como OutOfStock)


lotes = [Lote("lote-1", "SMALL-FORK", 10), Lote("lote-2", "MESA", 5)]
for sku, cantidad in [("SMALL-FORK", 4), ("MESA", 9), ("MESA", 5)]:
    try:
        print(sku, cantidad, "-> asignado a", asignar_a_lotes(sku, cantidad, lotes))
    except SinStock as e:
        print(sku, cantidad, "->", e)                      # Paso 4: el programa sigue
