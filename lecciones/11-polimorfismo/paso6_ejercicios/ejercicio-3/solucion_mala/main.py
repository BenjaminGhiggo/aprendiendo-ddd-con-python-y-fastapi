# Ej3 — MALA (funciona): para agregar un medio de pago nuevo hay que tocar el if.
def pagar(metodo, monto):
    if metodo == "efectivo":
        return "Pagaste " + str(monto) + " en efectivo"
    elif metodo == "tarjeta":
        return "Pagaste " + str(monto) + " con tarjeta"

print(pagar("efectivo", 100))
print(pagar("tarjeta", 100))
