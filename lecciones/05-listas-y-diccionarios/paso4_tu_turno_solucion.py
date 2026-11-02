# paso4_tu_turno_solucion.py — PASO 4 de la Lección 05: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index paso3_tu_turno.py paso4_tu_turno_solucion.py
# Si tu versión es distinta pero da la MISMA salida, también está bien.

# --- Parte A: listas ---
productos = ["mesa", "silla", "lámpara"]

# TODO 1: imprime el ÚLTIMO producto usando un índice negativo (fórmula L4).
print(productos[-1])

# TODO 2: agrega "cama" al final de la lista (L7).
productos.append("cama")

# TODO 3: imprime cuántos productos hay ahora (L6).
print(len(productos))

# --- Parte B: diccionarios ---
stock = {"mesa": 10, "silla": 25}

# TODO 4: agrega "cama" con stock 4 (D5).
stock["cama"] = 4

# TODO 5: se vendieron 3 sillas: réstalas del stock (mira el Ejemplo 2 del README).
stock["silla"] = stock["silla"] - 3

# TODO 6: muestra el stock de "sofá" SIN que el programa reviente; si no existe, 0 (D4).
print(stock.get("sofá", 0))

# TODO 7: recorre stock con .items() e imprime "mesa -> 10", etc. (D11).
for producto, cantidad in stock.items():
    print(producto, "->", cantidad)

# Salida esperada:
# lámpara
# 4
# 0
# mesa -> 10
# silla -> 22
# cama -> 4
