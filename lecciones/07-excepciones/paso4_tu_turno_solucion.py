# paso4_tu_turno_solucion.py — PASO 4 de la Lección 07: solución de referencia de paso3.
# Compárala con la tuya:
#   git diff --no-index paso3_tu_turno.py paso4_tu_turno_solucion.py
# Si tu versión es distinta pero da la MISMA salida, también está bien.

# TODO 1: define tu propio error PedidoInvalido (X4).
class PedidoInvalido(Exception):
    pass


# TODO 2: define validar_pedido(cantidad) que LANCE PedidoInvalido("la cantidad
#         debe ser positiva") si cantidad <= 0; si no, que devuelva cantidad (X5).
def validar_pedido(cantidad):
    if cantidad <= 0:
        raise PedidoInvalido("la cantidad debe ser positiva")
    return cantidad


# TODO 3: llama validar_pedido(5) dentro de un try; en el else imprime
#         "válido:" y el valor; en el except imprime "inválido:" y el mensaje (X3 + X7).
try:
    valor = validar_pedido(5)
except PedidoInvalido as e:
    print("inválido:", e)
else:
    print("válido:", valor)

# TODO 4: repite lo mismo con validar_pedido(-2).
try:
    valor = validar_pedido(-2)
except PedidoInvalido as e:
    print("inválido:", e)
else:
    print("válido:", valor)

# TODO 5: intenta int("doce") y atrapa el ValueError imprimiendo "no es número" (X12).
try:
    int("doce")
except ValueError:
    print("no es número")

# TODO 6: con stock = {"mesa": 3}, intenta stock["sofá"]; atrapa el KeyError e
#         imprime "no hay sofá"; agrega un finally que imprima "fin" (X8 + X9).
stock = {"mesa": 3}
try:
    stock["sofá"]
except KeyError:
    print("no hay sofá")
finally:
    print("fin")

# Salida esperada:
# válido: 5
# inválido: la cantidad debe ser positiva
# no es número
# no hay sofá
# fin
