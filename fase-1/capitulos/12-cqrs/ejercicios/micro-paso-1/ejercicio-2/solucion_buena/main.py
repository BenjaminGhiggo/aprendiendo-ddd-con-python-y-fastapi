# BUENA: Post/Redirect/Get. El POST escribe y responde "ve a verlo" (no datos);
# un GET aparte lee. Recargar el GET no reescribe nada.
pedidos = []
def post_asignar(pedido):
    pedidos.append(pedido)          # escribe y nada mas
    return 202                      # "aceptado, consulta el GET"
def get_pedidos():                  # lee, idempotente
    return list(pedidos)
print("POST status:", post_asignar("p1"))
print("GET:", get_pedidos())
print("RECARGA GET:", get_pedidos())   # no duplica
