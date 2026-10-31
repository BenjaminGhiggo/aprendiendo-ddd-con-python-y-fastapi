# saludo.py

# 1. Una VARIABLE es una "cajita" con nombre que guarda un valor.
#    A la izquierda el nombre, el signo = "guarda en", a la derecha el valor.
nombre = "Benjamin"   # un TEXTO (en Python se llama str, de "string")
edad = 25             # un NÚMERO ENTERO (en Python se llama int)

# 2. Usamos las variables por su nombre.
print("Hola, " + nombre)   # unimos dos textos con +
print("Tu edad es:")
print(edad)

# 3. ¿De qué TIPO es cada valor? Python nos lo dice con type(...)
print(type(nombre))
print(type(edad))

# 4. Una variable puede CAMBIAR. Cambiamos el valor en UN solo lugar...
nombre = "Ana"
print("Hola, " + nombre)   # ...y todo lo que la use, cambia.
