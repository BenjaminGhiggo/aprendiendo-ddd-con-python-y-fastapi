# paso1_formulas.py — PASO 1 de la Lección 05.
# Cada bloque es una "fórmula" de las tablas del README (§5 y §6), con su código (L1, D1...).
# Ejecuta:  uv run python lecciones/05-listas-y-diccionarios/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.

print("========== LISTAS ==========")

# L1 · Crear una lista: valores entre corchetes [ ], separados por comas.
productos = ["mesa", "silla", "lámpara"]
print("L1  crear:          ", productos)

# L2 · Lista vacía: corchetes sin nada adentro.
vacia = []
print("L2  vacía:          ", vacia)

# L3 · Acceder por posición (índice). El PRIMERO es el 0, no el 1.
print("L3  productos[0]:   ", productos[0])

# L4 · Índice negativo: -1 es el ÚLTIMO, -2 el penúltimo.
print("L4  productos[-1]:  ", productos[-1])

# L5 · Cambiar el elemento de una posición.
productos[1] = "sofá"
print("L5  cambiar [1]:    ", productos)
productos[1] = "silla"            # lo devolvemos a como estaba para las siguientes fórmulas

# L6 · Tamaño: cuántos elementos tiene.
print("L6  len:            ", len(productos))

# L7 · Agregar al final.
productos.append("cama")
print("L7  append('cama'): ", productos)

# L8 · ¿Está? (True = sí, False = no)
print("L8  'mesa' in:      ", "mesa" in productos)
print("L8  'sofá' in:      ", "sofá" in productos)

# L9 · ¿En qué posición está?
print("L9  index('silla'): ", productos.index("silla"))

# L10 · Quitar por valor (quita la PRIMERA aparición).
productos.remove("cama")
print("L10 remove('cama'): ", productos)

# L11 · Sacar el último: pop() lo quita Y lo devuelve.
ultimo = productos.pop()
print("L11 pop() devolvió: ", ultimo, "| queda:", productos)
productos.append("lámpara")       # lo reponemos

# L12 · Rebanar: desde la posición a HASTA b (b NO se incluye).
print("L12 productos[0:2]: ", productos[0:2])

# L13 · Ordenar: sorted() devuelve una lista NUEVA ordenada; la original no cambia.
print("L13 sorted:         ", sorted(productos), "| original:", productos)

# L14 · Recorrer: en cada vuelta, 'prod' toma un elemento.
print("L14 recorrer:")
for prod in productos:
    print("      ->", prod)

print()
print("========== DICCIONARIOS ==========")

# D1 · Crear: pares clave: valor entre llaves { }.
stock = {"mesa": 10, "silla": 25}
print("D1  crear:            ", stock)

# D2 · Diccionario vacío.
d = {}
print("D2  vacío:            ", d)

# D3 · Leer por CLAVE.
print("D3  stock['mesa']:    ", stock["mesa"])

# D4 · Leer seguro: si la clave no existe, devuelve el valor por defecto (no revienta).
print("D4  get('cama', 0):   ", stock.get("cama", 0))

# D5 · Agregar (si la clave no existe) o cambiar (si ya existe).
stock["cama"] = 4
print("D5  stock['cama']=4:  ", stock)

# D6 · ¿Existe la CLAVE?
print("D6  'mesa' in stock:  ", "mesa" in stock)

# D7 · Tamaño: cuántos pares hay.
print("D7  len:              ", len(stock))

# D8 · Borrar un par.
del stock["cama"]
print("D8  del stock['cama']:", stock)

# D9 · Solo las claves (list(...) las muestra como lista).
print("D9  claves:           ", list(stock.keys()))

# D10 · Solo los valores.
print("D10 valores:          ", list(stock.values()))

# D11 · Recorrer pares: en cada vuelta, k es la clave y v su valor.
print("D11 recorrer pares:")
for k, v in stock.items():
    print("      ->", k, v)

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# (En la Lección 07 aprenderás a atrapar estos errores sin que el programa se detenga.)
# print(productos[3])        # E1 -> IndexError: list index out of range
# print(stock["cama"])       # E2 -> KeyError: 'cama'
# productos.remove("sofá")   # E4 -> ValueError: list.remove(x): x not in list
# print(stock("mesa"))       # E6 -> TypeError: 'dict' object is not callable
# ---------------------------------------------------------------------------
