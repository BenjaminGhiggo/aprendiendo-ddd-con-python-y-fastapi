# Ej2 — MALA (funciona): el cálculo de envío crece con un if por cada país.
def costo_envio(pais):
    if pais == "PE":
        return 10
    elif pais == "CL":
        return 15
    # cada país nuevo = otro elif aquí dentro
    return 0

print(costo_envio("PE"))
print(costo_envio("CL"))
