# bucles.py

# 1. Una LISTA guarda varios valores en orden. (La veremos a fondo en la lección 05.)
nombres = ["Ana", "Benjamin", "Carla"]

# 2. El FOR repite su bloque UNA vez por cada elemento de la lista.
#    En cada vuelta, "nombre" toma el valor del siguiente elemento.
for nombre in nombres:
    print("Hola, " + nombre)

# 3. El WHILE repite MIENTRAS su condición sea True. Aquí contamos de 3 a 1.
cuenta = 3
while cuenta > 0:
    print(cuenta)
    cuenta = cuenta - 1   # nos acercamos al final; si no, sería un bucle infinito

print("¡Despegue!")
