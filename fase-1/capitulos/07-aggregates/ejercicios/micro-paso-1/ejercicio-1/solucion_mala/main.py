# MALA: se asigna tocando los lotes sueltos (sin frontera de consistencia).
lotes = [{"ref": "l1", "disp": 100}, {"ref": "l2", "disp": 50}]
def asignar(cantidad):
    for l in lotes:
        if l["disp"] >= cantidad:
            l["disp"] -= cantidad
            return l["ref"]
print(asignar(10))     # cualquiera puede tocar los lotes directamente
