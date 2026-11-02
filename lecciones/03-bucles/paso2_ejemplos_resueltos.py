# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 03.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/03-bucles/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: saludar a varias personas (fácil) ---")
nombres = ["Ana", "Benjamin", "Carla"]   # Paso 1: los datos, en una lista
for nombre in nombres:                   # Paso 2: una vuelta por nombre (R1)
    print("Hola, " + nombre)             # Paso 3: lo que se repite (con sangría)
print("Fin")                             # Paso 4: sin sangría -> corre UNA vez, al final

print()
print("--- Ejemplo 2: cuenta regresiva (fácil) ---")
cuenta = 3                               # Paso 1: valor inicial
while cuenta > 0:                        # Paso 2: ¿sigo? se pregunta ANTES de cada vuelta (W1)
    print(cuenta)
    cuenta = cuenta - 1                  # Paso 3: me acerco al final (si no, es infinito)
print("¡Despegue!")

print()
print("--- Ejemplo 3: total y caros de una lista de precios (intermedio) ---")
precios = [10, 20, 30]
total = 0                                # Paso 1: acumulador, ANTES del for (R7)
caros = 0                                # Paso 2: contador, ANTES del for (R8)
for precio in precios:                   # Paso 3: recorrer
    total = total + precio               # Paso 4: acumular
    if precio > 15:                      # Paso 5: contar solo los que cumplen
        caros = caros + 1
    print("  vuelta: precio", precio, "| total", total, "| caros", caros)
print("Total:", total, "| caros:", caros)   # -> Total: 60 | caros: 2

print()
print("--- Ejemplo 4: elegir el primer lote que alcance, como next(...) del libro (avanzado) ---")
disponibles = [0, 5, 20]                 # Paso 1: lo que tiene cada lote, YA en orden de preferencia
pedido = 10                              # Paso 2: lo que pide la línea de pedido
elegido = 0                              # Paso 3: aquí guardaré el lote elegido (0 = ninguno)
for disponible in disponibles:           # Paso 4: recorrer en orden
    print("  ¿alcanza un lote con", disponible, "?", disponible >= pedido)
    if disponible >= pedido:             # Paso 5: el PRIMERO que alcance...
        elegido = disponible
        break                            # ...y dejo de buscar (W5)
print("Lote elegido: el que tiene", elegido)   # -> 20
