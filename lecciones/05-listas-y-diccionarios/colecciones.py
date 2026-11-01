# colecciones.py

# 1. Una LISTA guarda varios valores EN ORDEN. Se accede por POSICIÓN (empieza en 0).
productos = ["mesa", "silla", "lámpara"]
print(productos[0])    # mesa  -> la primera posición es 0, no 1
print(len(productos))  # 3     -> cuántos elementos tiene
productos.append("sofá")   # agrega al final
print(productos)

# 2. Un DICCIONARIO guarda pares CLAVE -> VALOR. Se accede por la CLAVE, no por posición.
stock = {"mesa": 10, "silla": 25}
print(stock["mesa"])   # 10  -> busco por la clave "mesa"
stock["lámpara"] = 7   # agrega (o cambia) un par clave->valor
print(stock)

# 3. Recorrer un diccionario con for: en cada vuelta tomo una clave.
for producto in stock:
    print(producto, "->", stock[producto])
