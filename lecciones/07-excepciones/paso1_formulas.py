# paso1_formulas.py — PASO 1 de la Lección 07.
# Cada bloque es una "fórmula" de la tabla del README (§5), con su código (X1, X2...).
# Ejecuta:  uv run python lecciones/07-excepciones/paso1_formulas.py
# y compara cada línea impresa con la columna "Resultado" de la tabla.

print("========== EXCEPCIONES ==========")

# X1 + X2 · LANZAR un error con raise y ATRAPARLO con try / except.
try:
    raise ValueError("cantidad inválida")
except ValueError:
    print("X2  atrapado un ValueError")

# X3 · Guardar el error en una variable para leer su mensaje: except Tipo as e
try:
    raise ValueError("cantidad inválida")
except ValueError as e:
    print("X3  mensaje:", e)


# X4 · Definir un error PROPIO, con nombre del negocio. (La sintaxis "(Exception)"
#      significa "es un tipo de error"; la explicamos a fondo en la Lección 10.)
class SinStock(Exception):
    pass


# X5 · Lanzar el error propio con un mensaje.
def asignar(disponible, pedido):
    if pedido > disponible:
        raise SinStock("No hay stock suficiente")
    return disponible - pedido


try:
    asignar(10, 25)
except SinStock as e:
    print("X5  SinStock:", e)


# X6 · Varios except: cada tipo de error tiene su propia reacción.
def convertir_y_dividir(texto):
    try:
        numero = int(texto)
        return 100 / numero
    except ValueError:
        return "no es un número"
    except ZeroDivisionError:
        return "no se puede dividir entre 0"


print("X6  '4':  ", convertir_y_dividir("4"))
print("X6  'abc':", convertir_y_dividir("abc"))
print("X6  '0':  ", convertir_y_dividir("0"))

# X7 · else: corre SOLO si NO hubo error.   X8 · finally: corre SIEMPRE.
try:
    resto = asignar(10, 4)
except SinStock:
    print("X7  (no se imprime: no hubo error)")
else:
    print("X7  else, quedan:", resto)
finally:
    print("X8  finally: siempre me ejecuto")

# X9 · Atrapar el KeyError de un diccionario (Lección 05).
stock = {"mesa": 10}
try:
    print(stock["cama"])
except KeyError as e:
    print("X9  KeyError, no existe la clave:", e)

# X10 · Atrapar el IndexError de una lista (Lección 05).
productos = ["mesa", "silla"]
try:
    print(productos[5])
except IndexError as e:
    print("X10 IndexError:", e)

# X11 · Dividir entre cero.
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("X11 ZeroDivisionError:", e)

# X12 · Convertir texto que no es número.
try:
    print(int("abc"))
except ValueError as e:
    print("X12 ValueError:", e)

# X13 · El NOMBRE del tipo de error: type(e).__name__
try:
    asignar(1, 2)
except SinStock as e:
    print("X13 tipo:", type(e).__name__)


# X14 · PROPAGACIÓN: si la función no atrapa el error, "sube" hasta quien la llamó.
def procesar(pedido):
    return asignar(10, pedido)        # aquí NO hay try: el error sigue subiendo


try:
    procesar(50)
except SinStock:
    print("X14 el error subió desde asignar() hasta aquí")

# X15 · Después de atrapar, el programa SIGUE normalmente.
print("X15 sigo ejecutándome")

# ---------------------------------------------------------------------------
# ⚠️ ERRORES (README §8). Están comentados porque DETIENEN el programa.
# Quita el # de UNA línea (o bloque), ejecuta, lee el mensaje y vuelve a ponerlo.
# asignar(10, 25)                    # sin try -> SinStock: No hay stock suficiente
# raise "error"                      # E4 -> TypeError: exceptions must derive from BaseException
# raise SinStockk("x")               # E3 -> NameError: name 'SinStockk' is not defined
# try:                               # E2 -> el except NO es del tipo correcto:
#     stock["cama"]                  #        KeyError: 'cama' (no lo atrapa ValueError)
# except ValueError:
#     print("nunca llego aquí")
# ---------------------------------------------------------------------------
