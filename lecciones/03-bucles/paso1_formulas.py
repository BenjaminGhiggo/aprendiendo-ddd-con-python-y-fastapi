# paso1_formulas.py — PASO 1 de la Lección 03.
# Cada bloque es una "fórmula" de las tablas del README (§5 y §6), con su código (R1, W1...).
# Ejecuta:  uv run python lecciones/03-bucles/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.
# (La lista [ ... ] la usamos aquí solo para recorrerla; la verás a fondo en la Lección 05.)

print("========== FOR ==========")

# R1 · Recorrer una lista: en cada vuelta, 'nombre' toma el siguiente elemento.
nombres = ["Ana", "Benjamin", "Carla"]
print("R1  recorrer una lista:")
for nombre in nombres:
    print("      Hola, " + nombre)

# R2 · Repetir n veces con range(n): va de 0 a n-1. end=" " (R11) deja todo en una línea.
print("R2  range(3):          ", end=" ")
for i in range(3):
    print(i, end=" ")
print()

# R3 · range(a, b): desde a hasta b-1 (b NO se incluye).
print("R3  range(1, 4):       ", end=" ")
for i in range(1, 4):
    print(i, end=" ")
print()

# R4 · range(a, b, paso): de 'paso' en 'paso'.
print("R4  range(0, 10, 3):   ", end=" ")
for i in range(0, 10, 3):
    print(i, end=" ")
print()

# R5 · Hacia atrás: paso negativo.
print("R5  range(3, 0, -1):   ", end=" ")
for i in range(3, 0, -1):
    print(i, end=" ")
print()

# R6 · Recorrer un texto: una vuelta por letra.
print("R6  for letra in 'sol':", end=" ")
for letra in "sol":
    print(letra, end=" ")
print()

# R7 · Acumulador: una variable que va SUMANDO en cada vuelta. Se crea ANTES del for.
precios = [10, 20, 30]
total = 0
for precio in precios:
    total = total + precio
print("R7  suma de [10, 20, 30]:", total)

# R8 · Contador: una variable que suma 1 cada vez que algo se cumple.
cuenta = 0
for precio in precios:
    if precio > 15:
        cuenta = cuenta + 1
print("R8  cuántos son > 15:  ", cuenta)

# R9 · Filtrar: un if dentro del for decide qué vueltas hacen algo.
print("R9  pares de 1 a 6:    ", end=" ")
for n in range(1, 7):
    if n % 2 == 0:
        print(n, end=" ")
print()

# R10 · Bucle anidado: un for dentro de otro (el de adentro da TODAS sus vueltas por cada vuelta del de afuera).
print("R10 anidado 2 x 2:")
for a in range(1, 3):
    for b in range(1, 3):
        print("      " + str(a) + " x " + str(b) + " = " + str(a * b))

# R11 · print(x, end=" "): no salta de línea; el siguiente print sigue en la misma línea.
print("R11 end=' ':           ", end=" ")
print("uno", end=" ")
print("dos")

print()
print("========== WHILE Y CONTROL ==========")

# W1 · while: repite MIENTRAS la condición sea True. Algo adentro debe acercarla a False.
print("W1  cuenta regresiva:  ", end=" ")
cuenta = 3
while cuenta > 0:
    print(cuenta, end=" ")
    cuenta = cuenta - 1
print("¡Despegue!")

# W2 · while hasta llegar a un límite (no sé de antemano cuántas vueltas serán).
ahorro = 0
meses = 0
while ahorro < 100:
    ahorro = ahorro + 30
    meses = meses + 1
print("W2  ahorro >= 100:     ", ahorro, "en", meses, "meses")

# W3 · break: sale del bucle en ese mismo momento.
print("W3  break en 4:        ", end=" ")
for n in range(1, 10):
    if n == 4:
        break
    print(n, end=" ")
print()

# W4 · continue: salta el resto de ESTA vuelta y sigue con la siguiente.
print("W4  continue en 3:     ", end=" ")
for n in range(1, 6):
    if n == 3:
        continue
    print(n, end=" ")
print()

# W5 · Buscar el PRIMERO que cumple: for + if + break.
for n in range(50, 100):
    if n % 7 == 0:
        print("W5  primer múltiplo de 7 desde 50:", n)
        break

# W6 · Bandera: una variable bool que recuerda si algo pasó durante el bucle.
encontrado = False
for nombre in nombres:
    if nombre == "Carla":
        encontrado = True
print("W6  ¿está Carla?:      ", encontrado)

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # (de la línea o del bloque entero), ejecuta, lee el error y vuelve a ponerlo.
# for i in range(3)          # E1 -> SyntaxError: expected ':'
#     print(i)
# for i in 5:                # E3 -> TypeError: 'int' object is not iterable
#     print(i)
# for p in [1, 2]:           # E4 -> NameError: name 'acumulado' is not defined
#     acumulado = acumulado + p
# ⚠️ E6 (bucle infinito): NO lo descomentes salvo que sepas detenerlo con Ctrl+C.
# n = 3
# while n > 0:
#     print(n)               # falta n = n - 1 -> nunca termina
# ---------------------------------------------------------------------------
