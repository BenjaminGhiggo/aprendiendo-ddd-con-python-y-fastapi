# Ej3 — MALA (funciona): el reporte decide adentro de dónde saca los datos.
def total_ventas():
    ventas = [100, 200, 300]   # datos "cableados" dentro de la lógica
    return sum(ventas)

print(total_ventas())
# No puedo calcular el total con OTRAS ventas sin editar la función.
