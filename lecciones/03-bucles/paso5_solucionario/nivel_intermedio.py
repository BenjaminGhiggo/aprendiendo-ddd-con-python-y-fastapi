# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/03-bucles/paso5_solucionario/nivel_intermedio.py

# Problema 5: la tabla del 7, con una f-string (Lección 01) dentro del for.
print("P5:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# Problema 6: contador + filtro (R8 + R9).
pares = 0
for n in range(1, 21):
    if n % 2 == 0:
        pares = pares + 1
print("P6:", pares)

# Problema 7: acumular SOLO los que cumplen la condición.
precios = [30, 80, 45, 120, 60]
suma = 0
for precio in precios:
    if precio > 50:
        suma = suma + precio
print("P7:", suma)

# Problema 8: buscar el primero que cumple con while (no sé cuántas vueltas serán).
n = 50
while n % 7 != 0:
    n = n + 1
print("P8:", n)
