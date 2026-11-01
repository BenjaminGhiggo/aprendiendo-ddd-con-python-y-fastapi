# MALA: el adaptador tiene lógica de negocio adentro (no es "fino").
def consumir(mensaje):
    # decide reglas de negocio aqui mismo
    if mensaje["cantidad"] < 0:
        return "rechazado"
    return "procesado " + mensaje["ref"]
print(consumir({"ref": "l1", "cantidad": 5}))
