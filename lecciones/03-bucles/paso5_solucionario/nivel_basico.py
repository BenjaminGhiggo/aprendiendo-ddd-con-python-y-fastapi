# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/03-bucles/paso5_solucionario/nivel_basico.py

# Problema 1: del 1 al 10 -> range(1, 11), porque el 11 NO se incluye (R3).
print("P1:")
for i in range(1, 11):
    print(i)

# Problema 2: acumulador que empieza en 0, antes del for (R7).
precios = [10, 20, 30]
total = 0
for precio in precios:
    total = total + precio
print("P2:", total)

# Problema 3: recorrer una lista (R1).
print("P3:")
for nombre in ["Ana", "Benjamin", "Carla"]:
    print("Hola, " + nombre)

# Problema 4: while que baja de 5 a 1 (W1).
print("P4:")
cuenta = 5
while cuenta > 0:
    print(cuenta)
    cuenta = cuenta - 1
print("¡Despegue!")
