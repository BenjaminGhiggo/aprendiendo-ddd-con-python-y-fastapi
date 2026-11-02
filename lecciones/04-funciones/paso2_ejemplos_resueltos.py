# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 04.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/04-funciones/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: saludo reutilizable (fácil) ---")


def saludar(nombre):                  # Paso 1: definir con un parámetro (F3)
    return "Hola, " + nombre          # Paso 2: devolver el texto armado (F5)


print(saludar("Ana"))                 # Paso 3: llamar y mostrar (F2)  -> Hola, Ana
print(saludar("Luis"))                # Paso 4: reutilizar             -> Hola, Luis

print()
print("--- Ejemplo 2: total de una compra (fácil) ---")


def calcular_total(precio, cantidad):  # Paso 1: dos parámetros (F4)
    total = precio * cantidad          # Paso 2: calcular (variable local, F14)
    return total                       # Paso 3: devolver (F5)


compra = calcular_total(15, 4)         # Paso 4: guardar lo devuelto (F6)
print(compra)                          # -> 60

print()
print("--- Ejemplo 3: ¿puedo asignar? (intermedio) ---")


def puede_asignar(disponible, pedido):  # Paso 1: la pregunta como función
    return disponible >= pedido         # Paso 2: devolver True/False (F10)


for pedido in [5, 20, 25]:              # Paso 3: probarla con varios pedidos (F15)
    print("pedido", pedido, "->", puede_asignar(20, pedido))
# -> pedido 5 -> True / pedido 20 -> True / pedido 25 -> False

print()
print("--- Ejemplo 4: funciones que se llaman entre sí, con anotaciones (avanzado) ---")


def puede(disponible: int, pedido: int) -> bool:           # Paso 1: pregunta (F10 + F13)
    return disponible >= pedido


def asignar(disponible: int, pedido: int) -> int:          # Paso 2: usa a la otra (F12)
    if puede(disponible, pedido):                          # Paso 3: si alcanza...
        return disponible - pedido                         #   ...resta y TERMINA (F11)
    return disponible                                      # Paso 4: no alcanzó: no cambia


print(asignar(20, 5))     # -> 15
print(asignar(20, 25))    # -> 20 (no alcanzaba)
