# BUENA: el modelo REGISTRA un evento de reasignación; el bus la ejecuta.
eventos = []
def cambiar_cantidad(lote, nueva):
    lote["disp"] = nueva
    while lote["disp"] < 0:
        linea = lote["asig"].pop()
        lote["disp"] += linea
        eventos.append(("AsignacionRequerida", linea))   # el bus se encarga
l = {"disp": 50, "asig": [50]}
cambiar_cantidad(l, 30)
print(eventos)
