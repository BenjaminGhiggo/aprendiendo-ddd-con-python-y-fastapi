# MALA: la reasignación se hace a mano dentro del handler (enredado).
def cambiar_cantidad(lote, nueva, otros):
    lote["disp"] = nueva
    while lote["disp"] < 0:
        linea = lote["asig"].pop()
        otros[0]["disp"] -= linea; otros[0].setdefault("asig",[]).append(linea)  # reasigna aqui
    return lote
l = {"disp": 50, "asig": [50]}
print(cambiar_cantidad(l, 30, [{"disp": 100}]))
