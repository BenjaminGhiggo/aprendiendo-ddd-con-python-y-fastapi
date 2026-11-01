# MALA: el consumidor usa el mensaje crudo externo en todo el sistema.
def procesar(mensaje_crudo):
    # pasa el dict externo tal cual al dominio (acopla al formato externo)
    return mensaje_crudo["ref"] + "/" + str(mensaje_crudo["qty"])
print(procesar({"ref": "l1", "qty": 5}))
