# paso4_tu_turno_solucion.py — PASO 4 de la Lección 03: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index paso3_tu_turno.py paso4_tu_turno_solucion.py
# Si tu versión es distinta pero da la MISMA salida, también está bien.

nombres = ["Ana", "Luis", "Sofía"]
# TODO 1: saluda a cada nombre con "Hola, " + nombre   (R1)
for nombre in nombres:
    print("Hola, " + nombre)

# TODO 2: con range, muestra los números del 1 al 3, uno por línea   (R3)
for i in range(1, 4):
    print(i)

numeros = [5, 10, 15]
# TODO 3: suma los numeros con un acumulador y muestra el total   (R7)
total = 0
for numero in numeros:
    total = total + numero
print(total)

# TODO 4: cuenta cuántos números entre 1 y 10 (ambos incluidos) son pares y muestra la cuenta   (R8 + R9)
pares = 0
for i in range(1, 11):
    if i % 2 == 0:
        pares = pares + 1
print(pares)

n = 1
# TODO 5: mientras n sea 100 o menos, duplícalo (n = n * 2). Al terminar, muestra n   (W1)
while n <= 100:
    n = n * 2
print(n)

# TODO 6: recorre range(1, 20) y muestra el PRIMER múltiplo de 6; luego sal del bucle   (W5)
for i in range(1, 20):
    if i % 6 == 0:
        print(i)
        break

# TODO 7: suma los números del 1 al 10 SALTANDO el 5 (usa continue) y muestra la suma   (W4)
suma = 0
for i in range(1, 11):
    if i == 5:
        continue
    suma = suma + i
print(suma)

# Salida esperada:
# Hola, Ana
# Hola, Luis
# Hola, Sofía
# 1
# 2
# 3
# 30
# 5
# 128
# 6
# 50
