# BUENA: cada paso es un handler; el bus los encadena.
eventos = []
def cambiar(lote, nueva):
    lote["disp"] = nueva
    if lote["disp"] < 0: eventos.append("reasignar")
def reasignar(_): print("reasignando...")
MANEJADORES = {"reasignar": [reasignar]}
l = {"disp": 50}; cambiar(l, -10)
for e in eventos:
    for m in MANEJADORES[e]: m(e)
