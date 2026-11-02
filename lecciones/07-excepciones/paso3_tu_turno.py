# paso3_tu_turno.py — PASO 3 de la Lección 07 (pair programming).
# Completa cada # TODO escribiendo el código DEBAJO del comentario. Luego ejecuta:
#   uv run python lecciones/07-excepciones/paso3_tu_turno.py
# y compara tu salida con la "Salida esperada" del final. Si te trabas, mira la
# fórmula indicada entre paréntesis en el README (§5).
# Cuando termines, compara con paso4_tu_turno_solucion.py.

# TODO 1: define tu propio error PedidoInvalido (X4).

# TODO 2: define validar_pedido(cantidad) que LANCE PedidoInvalido("la cantidad
#         debe ser positiva") si cantidad <= 0; si no, que devuelva cantidad (X5).

# TODO 3: llama validar_pedido(5) dentro de un try; en el else imprime
#         "válido:" y el valor; en el except imprime "inválido:" y el mensaje (X3 + X7).

# TODO 4: repite lo mismo con validar_pedido(-2).

# TODO 5: intenta int("doce") y atrapa el ValueError imprimiendo "no es número" (X12).

# TODO 6: con stock = {"mesa": 3}, intenta stock["sofá"]; atrapa el KeyError e
#         imprime "no hay sofá"; agrega un finally que imprima "fin" (X8 + X9).

# Salida esperada:
# válido: 5
# inválido: la cantidad debe ser positiva
# no es número
# no hay sofá
# fin
