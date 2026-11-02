# paso1_formulas.py — PASO 1 de la Lección 00.
# Cada bloque es una "fórmula" de la tabla del README (§6), con su código (P1, P2...).
# Ejecuta:  uv run python lecciones/00-que-es-ejecutar-un-programa/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.
# Python lee este archivo de ARRIBA hacia ABAJO y realiza cada instrucción en ese orden.

# P1 · Tu primer programa: mostrar un texto. El texto va entre comillas.
print("¡Hola, mundo!")

# P2 · Las comillas pueden ser dobles "..." o simples '...'. Da lo mismo.
print('¡Hola, mundo!')

# P3 · Comillas DENTRO del texto: si por dentro usas dobles, por fuera usa simples.
print('Ella gritó: "Alto!"')

# P4 · Varios valores separados por coma: print los muestra con un espacio entre ellos.
print("Producto:", "Mesa")

# P5 · print() vacío: muestra una línea en blanco.
print()

# P6 · \n dentro del texto significa "salto de línea".
print("Línea 1\nLínea 2")

# P7 · Un número se puede mostrar sin comillas.
print(100)

# P8 · Python CALCULA primero y luego muestra el resultado.
print(2 + 3)

# P9 · OJO: con comillas, es TEXTO y no se calcula.
print("2 + 3")

# P10 · Un comentario empieza con #. Python lo IGNORA: no aparece en pantalla.
# Este texto es un comentario y no se muestra.
print("Después del comentario")

# P11 · Orden: se ejecuta de arriba hacia abajo, una instrucción tras otra.
print("primero")
print("segundo")
print("tercero")

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea, ejecuta, lee el mensaje de error y vuelve a ponerlo.
# print("Hola)        # E1 -> SyntaxError: unterminated string literal (detected at line ...)
# print(Hola)         # E2 -> NameError: name 'Hola' is not defined
# Print("Hola")       # E3 -> NameError: name 'Print' is not defined
# print("Hola"        # E4 -> SyntaxError: '(' was never closed
#   print("Hola")     # E5 -> (quita solo el # y deja los 2 espacios) IndentationError: unexpected indent
# ---------------------------------------------------------------------------
