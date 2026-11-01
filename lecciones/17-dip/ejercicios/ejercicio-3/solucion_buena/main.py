# Ej3 — BUENA: los datos entran por parámetro; la lógica no depende de su origen.
def total_ventas(ventas):
    return sum(ventas)

print(total_ventas([100, 200, 300]))
print(total_ventas([5, 5]))   # funciona con cualquier fuente de datos
