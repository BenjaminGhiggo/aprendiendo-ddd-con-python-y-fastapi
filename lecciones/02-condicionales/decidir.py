# decidir.py

# 1. Guardamos un dato que usaremos para DECIDIR.
edad = 20

# 2. Una COMPARACIÓN da como resultado un valor "booleano": True o False.
print(edad >= 18)   # ¿edad es mayor o igual a 18? -> True

# 3. El if ejecuta un bloque SOLO si la condición es True; si no, va el else.
#    OJO: lo que está "adentro" del if/else va con sangría (4 espacios).
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 4. Cambiamos el dato y la decisión cambia sola.
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
