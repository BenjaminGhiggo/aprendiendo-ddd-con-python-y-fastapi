# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/01-variables-y-tipos/paso5_solucionario/nivel_avanzado.py

# Problema 9: intercambiar dos variables con una variable "temporal" (V4).
a = 5
b = 9
temporal = a      # guardo a para no perderlo
a = b             # a ahora vale 9
b = temporal      # b recibe el 5 que guardé
print("P9:", a, b)

# Problema 10: promedio = suma / cantidad. Los paréntesis hacen la suma primero (P6).
nota1 = 12
nota2 = 15
nota3 = 18
promedio = (nota1 + nota2 + nota3) / 3
print("P10:", promedio)

# Problema 11: 25% de descuento. / siempre da float (P5).
precio = 80
descuento = precio * 25 / 100
precio_final = precio - descuento
print("P11:", precio_final)

# Problema 12 (puente al libro): disponible = comprado - asignado, recalculado tras cada línea.
comprado = 20
asignado = 0
asignado = asignado + 2
asignado = asignado + 3
disponible = comprado - asignado
print("P12:", f"Disponible: {disponible}")
