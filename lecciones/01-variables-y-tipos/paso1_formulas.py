# paso1_formulas.py — PASO 1 de la Lección 01.
# Cada bloque es una "fórmula" de las tablas del README (§5 y §6), con su código (V1, T1...).
# Ejecuta:  uv run python lecciones/01-variables-y-tipos/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.

print("========== VARIABLES ==========")

# V1 · Crear una variable: nombre = valor. El = significa "guarda en".
nombre = "Benjamin"
print("V1  crear:            ", nombre)

# V2 · Usar la variable por su nombre (sin comillas).
print("V2  usar:              Hola,", nombre)

# V3 · Reasignar: guardar un valor NUEVO; el anterior se pierde.
nombre = "Ana"
print("V3  reasignar:        ", nombre)

# V4 · Copiar el valor de una variable a otra.
copia = nombre
print("V4  copiar:           ", copia)

# V5 · Actualizar usando su propio valor: primero se calcula la derecha, luego se guarda.
stock = 20
stock = stock - 2
print("V5  actualizar:       ", stock)

# V6 · Guardar el resultado de una cuenta.
precio = 100
cantidad = 3
total = precio * cantidad
print("V6  resultado:        ", total)

# V7 · Nombres de varias palabras: se unen con guion bajo.
precio_unitario = 100
print("V7  nombre con _:     ", precio_unitario)

print()
print("========== TIPOS Y OPERACIONES ==========")

# T1 · Texto (str): va entre comillas.
print("T1  str:              ", type("Mesa"))

# T2 · Número entero (int): sin comillas, sin punto.
print("T2  int:              ", type(25))

# T3 · Número decimal (float): con punto (no coma).
print("T3  float:            ", type(10.5))

# T4 · type(...) dice el tipo del valor que guarda una variable.
edad = 25
print("T4  type(edad):       ", type(edad))

# T5 · Suma, resta y multiplicación.
print("T5  7 + 3, 7 - 3, 7 * 3:", 7 + 3, 7 - 3, 7 * 3)

# T6 · División con / : SIEMPRE da decimal (float).
print("T6  10 / 4 y 10 / 2:  ", 10 / 4, 10 / 2)

# T7 · División entera // : cuántas veces cabe, sin decimales.
print("T7  10 // 4:          ", 10 // 4)

# T8 · Resto % : lo que sobra de la división entera.
print("T8  10 % 4:           ", 10 % 4)

# T9 · Potencia ** .
print("T9  2 ** 3:           ", 2 ** 3)

# T10 · Unir (concatenar) textos con + .
print("T10 unir:             ", "Hola, " + "Ana")

# T11 · Repetir un texto con * .
print("T11 repetir:          ", "-" * 5)

# T12 · Número -> texto con str(), para poder unirlo con +.
print("T12 str(25):          ", "Edad: " + str(25))

# T13 · Texto -> número con int() o float().
print("T13 int('20') + 1:    ", int("20") + 1, "| float('10.5'):", float("10.5"))

# T14 · Texto con variables adentro (f-string): f"...{variable}...".
print("T14 f-string:         ", f"Hola, {nombre}. Tienes {edad} años")

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# print("Edad: " + 25)      # E1 -> TypeError: can only concatenate str (not "int") to str
# print(nombr)              # E2 -> NameError: name 'nombr' is not defined
# mi nombre = "Ana"         # E3 -> SyntaxError: invalid syntax
# 2nombre = "Ana"           # E4 -> SyntaxError: invalid decimal literal
# print(int("veinte"))      # E5 -> ValueError: invalid literal for int() with base 10: 'veinte'
# print(descuento)          # E6 -> NameError: name 'descuento' is not defined (se usa antes de crearla)
# ---------------------------------------------------------------------------
