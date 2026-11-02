# nivel_intermedio.py — soluciones de los problemas 🟡 5–8 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/07-excepciones/paso5_solucionario/nivel_intermedio.py

# Problema 5: varios except, uno por tipo de error (X6).
for texto in ["5", "abc", "0"]:
    try:
        numero = int(texto)
        print("P5:", texto, "->", 100 / numero)
    except ValueError:
        print("P5:", texto, "-> no es número")
    except ZeroDivisionError:
        print("P5:", texto, "-> división entre cero")

# Problema 6: else (si no hubo error) y finally (siempre) (X7 + X8).
for texto in ["7", "x"]:
    try:
        numero = int(texto)
    except ValueError:
        print("P6: error con", texto)
    else:
        print("P6: ok", numero)
    finally:
        print("P6: fin")


# Problema 7: error propio, y el programa sigue después (X4 + X5 + X15).
class SinStock(Exception):
    pass


def asignar(disponible, pedido):
    if pedido > disponible:
        raise SinStock("pedido de " + str(pedido) + " supera " + str(disponible))
    return disponible - pedido


try:
    asignar(10, 25)
except SinStock as e:
    print("P7:", e)
print("P7: sigo")

# Problema 8: el NOMBRE del tipo de error (X13), atrapando con Exception (cualquier error).
try:
    int("x")
except Exception as e:
    print("P8:", type(e).__name__)
try:
    {}["k"]
except Exception as e:
    print("P8:", type(e).__name__)
try:
    [][0]
except Exception as e:
    print("P8:", type(e).__name__)
