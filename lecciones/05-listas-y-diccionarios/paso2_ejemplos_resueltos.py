# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 05.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/05-listas-y-diccionarios/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: inventario con lista (fácil) ---")
productos = ["mesa", "silla", "lámpara"]   # Paso 1: crear (L1)
print(productos[0])                        # Paso 2: el primero (L3)   -> mesa
print(productos[-1])                       # Paso 3: el último (L4)    -> lámpara
productos[1] = "sofá"                      # Paso 4: cambiar (L5)
for prod in productos:                     # Paso 5: recorrer (L14)
    print(prod)                            # -> mesa / sofá / lámpara

print()
print("--- Ejemplo 2: registrar una venta (fácil) ---")
stock = {"mesa": 10, "silla": 25}          # Paso 1: crear (D1)
vendidas = 3                               # Paso 2: el dato de la venta
stock["mesa"] = stock["mesa"] - vendidas   # Paso 3: leer (D3), restar y guardar (D5)
print(stock["mesa"])                       # -> 7

print()
print("--- Ejemplo 3: contar repeticiones (intermedio) ---")
pedidos = ["mesa", "silla", "mesa"]
conteo = {}                                       # Paso 1: diccionario vacío (D2)
for prod in pedidos:                              # Paso 2: recorrer la lista (L14)
    conteo[prod] = conteo.get(prod, 0) + 1        # Paso 3: leer seguro (D4) y sumar 1
    print("  vuelta:", prod, "->", conteo)        # (traza: así cambia en cada vuelta)
print(conteo)                                     # -> {'mesa': 2, 'silla': 1}

print()
print("--- Ejemplo 4: lista dentro de diccionario, como HANDLERS del libro (avanzado) ---")


def avisar_email(sku):
    print("EMAIL: sin stock de", sku)


def avisar_sms(sku):
    print("SMS: sin stock de", sku)


MANEJADORES = {"SinStock": [avisar_email, avisar_sms]}   # Paso 1: clave -> LISTA de funciones

for funcion in MANEJADORES["SinStock"]:                  # Paso 2: leer la lista (D3) y recorrerla (L14)
    funcion("MESA")                                      # Paso 3: llamar a cada una
