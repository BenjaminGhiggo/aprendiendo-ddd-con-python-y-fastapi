# paso4_tu_turno_solucion.py — PASO 4 de la Lección 02: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index paso3_tu_turno.py paso4_tu_turno_solucion.py
# Si tu versión es distinta pero da la MISMA salida, también está bien.

edad = 20
# TODO 1: si edad es 18 o más, muestra "Puede votar"; si no, "No puede votar"   (F2)
if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")

n = 7
# TODO 2: muestra "par" si n es par, o "impar" si no lo es   (C12 + F2)
if n % 2 == 0:
    print("par")
else:
    print("impar")

temperatura = 30
# TODO 3: más de 25 -> "Hace calor"; de 15 en adelante -> "Templado"; si no -> "Hace frío"   (F3)
if temperatura > 25:
    print("Hace calor")
elif temperatura >= 15:
    print("Templado")
else:
    print("Hace frío")

usuario = "ana"
clave = "1234"
# TODO 4: si el usuario es "ana" Y la clave es "1234" -> "Bienvenida"; si no -> "Acceso denegado"   (F4)
if usuario == "ana" and clave == "1234":
    print("Bienvenida")
else:
    print("Acceso denegado")

# TODO 5: muestra el resultado de la comparación 3 != 3   (C2)
print(3 != 3)

hay_stock = False
# TODO 6: si NO hay stock, muestra "Agotado"   (C10 + F5)
if not hay_stock:
    print("Agotado")

x = 15
# TODO 7: si x está entre 10 y 20 (ambos incluidos), muestra "En rango"   (C11)
if 10 <= x <= 20:
    print("En rango")

# Salida esperada:
# Puede votar
# impar
# Hace calor
# Bienvenida
# False
# Agotado
# En rango
