# MALA: la vista lee directo de las estructuras del dominio; cambiar de motor obliga a
# reescribir el dominio y la vista juntos (acoplados).
dominio = {"p1": {"MESA": "l1"}}
def ver(pedido):
    return dominio[pedido]          # atado a la forma interna del dominio
print("mala:", ver("p1"))
