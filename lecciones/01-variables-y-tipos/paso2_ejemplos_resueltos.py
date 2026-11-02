# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 01.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/01-variables-y-tipos/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: un saludo que cambia en un solo lugar (fácil) ---")
nombre = "Benjamin"                      # Paso 1: crear la variable (V1)
print("Hola, " + nombre)                 # Paso 2: usarla uniendo textos (V2 + T10)
print(nombre + ", tu pedido está listo")
nombre = "Ana"                           # Paso 3: reasignar en UN solo lugar (V3)
print("Hola, " + nombre)                 # Paso 4: todo lo que la usa, cambia
print(nombre + ", tu pedido está listo")

print()
print("--- Ejemplo 2: precio total (fácil) ---")
precio = 100                             # Paso 1: datos en variables (V1)
cantidad = 3
total = precio * cantidad                # Paso 2: guardar el resultado de una cuenta (V6)
print("Total:", total)                   # -> Total: 300

print()
print("--- Ejemplo 3: unir texto y número (intermedio) ---")
edad = 25                                # Paso 1: edad es int (T2)
print(type(edad))                        # -> <class 'int'>
texto = "Tienes " + str(edad) + " años"  # Paso 2: str() convierte 25 en "25" (T12)
print(texto)                             # -> Tienes 25 años
print(f"Tienes {edad} años")             # Paso 3: lo mismo con f-string (T14)

print()
print("--- Ejemplo 4: stock disponible de un lote, como en el libro (avanzado) ---")
comprado = 20                            # Paso 1: el lote compró 20 unidades
asignado = 0                             # Paso 2: todavía no se asignó nada
asignado = asignado + 2                  # Paso 3: llega una línea de pedido de 2 (V5)
disponible = comprado - asignado         # Paso 4: disponible = comprado - asignado (V6)
print("Disponible:", disponible)         # -> 18 (lo mismo que espera el test del libro)
asignado = asignado + 5                  # Paso 5: llega otra línea de 5
disponible = comprado - asignado         # Paso 6: hay que RECALCULAR
print("Disponible:", disponible)         # -> 13
