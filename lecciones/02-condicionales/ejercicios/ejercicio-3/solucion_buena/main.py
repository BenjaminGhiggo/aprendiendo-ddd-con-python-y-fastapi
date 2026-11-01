# Ej3 — BUENA: una sola decisión con if/else; la condición se evalúa una vez.
def total_a_pagar(monto):
    if monto >= 100:
        print("Aplica descuento")
        return monto * 0.9
    else:
        return monto

print(total_a_pagar(50))
print(total_a_pagar(100))
