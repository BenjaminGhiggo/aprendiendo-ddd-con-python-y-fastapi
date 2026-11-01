# MALA: mezclar "bajar cantidad" con "reasignar" en una funcion gigante.
def todo(lote, nueva):
    lote["disp"] = nueva
    # ...y aqui mismo buscar otros lotes, reasignar, notificar... todo junto
    return "complejo"
print(todo({"disp":50}, 30))
