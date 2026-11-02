# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/02-condicionales/paso5_solucionario/nivel_basico.py

# Problema 1: un if solo (F1): si no se cumple, no se muestra nada.
precio = 120
if precio > 100:
    print("P1: Caro")

# Problema 2: los textos se comparan exactamente, con mayúsculas (C5).
print("P2:", "Mesa" == "mesa")

# Problema 3: par si el resto entre 2 es 0 (C12).
n = 8
if n % 2 == 0:
    print("P3: par")
else:
    print("P3: impar")

# Problema 4: el mayor de dos números con if/else (F2).
a = 7
b = 12
if a > b:
    print("P4:", a)
else:
    print("P4:", b)
