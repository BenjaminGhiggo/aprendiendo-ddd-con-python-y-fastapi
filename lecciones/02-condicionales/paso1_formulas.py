# paso1_formulas.py — PASO 1 de la Lección 02.
# Cada bloque es una "fórmula" de las tablas del README (§5 y §6), con su código (C1, F1...).
# Ejecuta:  uv run python lecciones/02-condicionales/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.

print("========== COMPARACIONES Y LÓGICA ==========")

# C1 · ¿Son iguales? (doble ==, porque un solo = es "guardar")
print("C1  5 == 5:           ", 5 == 5)

# C2 · ¿Son distintos?
print("C2  5 != 3:           ", 5 != 3)

# C3 · Menor que / mayor que
print("C3  3 < 5 y 3 > 5:    ", 3 < 5, 3 > 5)

# C4 · Menor o igual / mayor o igual
print("C4  18 >= 18, 17 <= 16:", 18 >= 18, 17 <= 16)

# C5 · Comparar textos: deben ser EXACTAMENTE iguales (mayúsculas incluidas)
print("C5  textos:           ", "mesa" == "mesa", "Mesa" == "mesa")

# C6 · True y False son de tipo bool (booleano)
print("C6  type(True):       ", type(True))

# C7 · Guardar el resultado de una comparación en una variable
edad = 20
es_mayor = edad >= 18
print("C7  es_mayor:         ", es_mayor)

# C8 · and: True solo si LAS DOS son True
print("C8  and:              ", True and True, True and False)

# C9 · or: True si AL MENOS UNA es True
print("C9  or:               ", True or False, False or False)

# C10 · not: invierte el valor
print("C10 not True:         ", not True)

# C11 · ¿Está en un rango? (comparación encadenada)
x = 5
print("C11 1 <= x <= 10:     ", 1 <= x <= 10)

# C12 · ¿Es par? El resto de dividir entre 2 es 0
print("C12 8 % 2 == 0:       ", 8 % 2 == 0, "| 7 % 2 == 0:", 7 % 2 == 0)

print()
print("========== FORMAS DE DECIDIR ==========")

# F1 · if solo: hace algo SOLO si se cumple; si no, no hace nada.
stock = 0
if stock == 0:
    print("F1  if:                Agotado")

# F2 · if / else: uno de dos caminos.
edad = 15
if edad >= 18:
    print("F2  if/else:           Mayor de edad")
else:
    print("F2  if/else:           Menor de edad")

# F3 · if / elif / else: varios caminos; entra en el PRIMERO que sea True.
nota = 14
if nota >= 18:
    print("F3  if/elif/else:      excelente")
elif nota >= 11:
    print("F3  if/elif/else:      aprobado")
else:
    print("F3  if/elif/else:      desaprobado")

# F4 · Condición compuesta con and / or.
usuario = "ana"
clave = "1234"
if usuario == "ana" and clave == "1234":
    print("F4  con and:           Bienvenida")

# F5 · Usar una variable booleana directamente como condición.
hay_stock = True
if hay_stock:
    print("F5  con bool:          Se puede vender")

# F6 · if dentro de otro if (anidado): el segundo solo se evalúa si el primero fue True.
sku_correcto = True
disponible = 20
if sku_correcto:
    if disponible >= 2:
        print("F6  anidado:           Se puede asignar")

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # (de la línea o del bloque entero), ejecuta, lee el error y vuelve a ponerlo.
# if edad = 18:              # E1 -> SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
#     print("x")
# if edad >= 18              # E2 -> SyntaxError: expected ':'
#     print("x")
# print("18" > 5)            # E4 -> TypeError: '>' not supported between instances of 'str' and 'int'
# (E3, la sangría que falta, se ve en el README §8.)
# ---------------------------------------------------------------------------
