# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/02-condicionales/paso5_solucionario/nivel_avanzado.py

# Problema 9: bisiesto = divisible entre 4 y (no entre 100, o sí entre 400).
# Los paréntesis agrupan el "o" para que se evalúe junto (como en matemáticas).
anio = 1900
if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print("P9:", anio, "es bisiesto")
else:
    print("P9:", anio, "no es bisiesto")      # 1900 es divisible entre 100 pero no entre 400

# Problema 10: comparar un texto contra varias opciones con elif; else para "lo demás".
color = "amarillo"
if color == "verde":
    print("P10: Avanza")
elif color == "amarillo":
    print("P10: Precaución")
elif color == "rojo":
    print("P10: Detente")
else:
    print("P10: Color inválido")

# Problema 11: envío gratis si cumple CUALQUIERA de las dos (or), con una variable bool (F5).
monto = 80
es_socio = True
if monto >= 100 or es_socio:
    print("P11: Envío gratis")
else:
    print("P11: Envío: 10")

# Problema 12 (puente al libro): can_allocate = mismo sku Y suficiente cantidad.
#   return self.sku == line.sku and self.available_quantity >= line.qty   (cap. 1)
sku_lote = "SMALL-TABLE"
disponible = 20
sku_linea = "SMALL-TABLE"
cantidad = 2
if sku_lote == sku_linea and disponible >= cantidad:
    disponible = disponible - cantidad
    print("P12: Asignado. Disponible:", disponible)
else:
    print("P12: No se puede asignar")
