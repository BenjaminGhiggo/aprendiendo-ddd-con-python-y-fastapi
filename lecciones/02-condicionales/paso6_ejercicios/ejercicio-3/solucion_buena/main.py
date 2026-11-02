# Ej3 — BUENA: una sola decisión con if/else; la condición vive en un solo lugar.
# Cambia el valor de 'monto' (50, 100) y vuelve a ejecutar.
monto = 100
if monto >= 100:
    print("Aplica descuento")
    total = monto * 0.9
else:
    total = monto
print(total)
