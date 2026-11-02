# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 00.
# Los 4 ejemplos resueltos del README (§9), en el mismo orden y con los mismos pasos.
# Ejecuta:  uv run python lecciones/00-que-es-ejecutar-un-programa/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: saludo en dos líneas (fácil) ---")
print("Hola, soy Benjamin")          # Paso 1: primera línea (P1)
print("Estoy aprendiendo Python")    # Paso 2: segunda línea; va DESPUÉS porque está abajo (P11)

print()
print("--- Ejemplo 2: un mensaje con comillas (fácil) ---")
# Paso 1: el texto lleva comillas dobles por dentro -> por fuera uso simples (P3)
print('El cliente dijo: "Quiero una mesa"')

print()
print("--- Ejemplo 3: ficha de producto con comas (intermedio) ---")
print("Producto:", "Mesa")           # Paso 1: dos valores con coma -> un espacio entre ellos (P4)
print("Precio:", 100)                # Paso 2: un texto y un número (P7)
print("Total de 3 mesas:", 3 * 100)  # Paso 3: Python calcula 3 * 100 antes de mostrar (P8)

print()
print("--- Ejemplo 4: mini ticket con saltos de línea y comentarios (avanzado) ---")
# Paso 1: un comentario como nota para mí (no sale en pantalla) (P10)
print("TIENDA LA MESA\n--------------")   # Paso 2: dos líneas con un solo print (P6)
print("Mesa", "x", 2)                       # Paso 3: varios valores (P4)
print()                                     # Paso 4: línea en blanco (P5)
print("Gracias por su compra")              # Paso 5: cierre
