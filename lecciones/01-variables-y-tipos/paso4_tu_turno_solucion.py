# paso4_tu_turno_solucion.py — PASO 4 de la Lección 01: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index paso3_tu_turno.py paso4_tu_turno_solucion.py
# Si tu versión es distinta pero da la MISMA salida, también está bien.

# TODO 1: crea la variable ciudad con el valor "Lima" y muestra "Vivo en " + ciudad   (V1 + T10)
ciudad = "Lima"
print("Vivo en " + ciudad)

# TODO 2: crea precio = 50 y cantidad = 4; guarda en total su multiplicación y muéstralo   (V6)
precio = 50
cantidad = 4
total = precio * cantidad
print(total)

# TODO 3: muestra el TIPO de la variable precio   (T4)
print(type(precio))

# TODO 4: cambia ciudad a "Cusco" y muéstrala con una f-string: f"Vivo en {ciudad}"   (V3 + T14)
ciudad = "Cusco"
print(f"Vivo en {ciudad}")

# TODO 5: crea edad = 30 y muestra "Edad: " + edad SIN que dé error   (T12)
edad = 30
print("Edad: " + str(edad))

# TODO 6: crea stock = 20, réstale 3 usando su propio valor, y muéstralo   (V5)
stock = 20
stock = stock - 3
print(stock)

# TODO 7: muestra el resultado de 10 / 4 y, en otra línea, el de 10 // 4   (T6 y T7)
print(10 / 4)
print(10 // 4)

# Salida esperada:
# Vivo en Lima
# 200
# <class 'int'>
# Vivo en Cusco
# Edad: 30
# 17
# 2.5
# 2
