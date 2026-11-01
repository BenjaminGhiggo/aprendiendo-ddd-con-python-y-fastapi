# Ej3 — MALA (funciona): repite la condición del descuento en dos lugares.
def total_a_pagar(monto):
    if monto >= 100:
        print("Aplica descuento")
    if monto >= 100:
        return monto * 0.9
    return monto

print(total_a_pagar(50))
print(total_a_pagar(100))
