# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/03-bucles/paso5_solucionario/nivel_avanzado.py

# Problema 9: factorial = 1 x 2 x 3 x 4 x 5. El acumulador de una MULTIPLICACIÓN empieza en 1.
factorial = 1
for i in range(1, 6):
    factorial = factorial * i
print("P9:", factorial)

# Problema 10: en cada vuelta, repetir "*" tantas veces como el número de vuelta (Lección 01, T11).
print("P10:")
for i in range(1, 5):
    print("*" * i)

# Problema 11: no sé cuántos meses serán -> while hasta llegar al límite (W2).
ahorro = 0
meses = 0
while ahorro < 100:
    ahorro = ahorro + 30
    meses = meses + 1
print("P11:", f"{meses} meses (ahorro final: {ahorro})")

# Problema 12 (puente al libro): allocated_quantity = sum(line.qty for line in self._allocations)
# es un ACUMULADOR sobre las líneas asignadas. Disponible = comprado - asignado.
comprado = 20
cantidades_asignadas = [2, 3, 5]
asignado = 0
for cantidad in cantidades_asignadas:
    asignado = asignado + cantidad
disponible = comprado - asignado
print("P12:", f"Asignado: {asignado} | Disponible: {disponible}")
