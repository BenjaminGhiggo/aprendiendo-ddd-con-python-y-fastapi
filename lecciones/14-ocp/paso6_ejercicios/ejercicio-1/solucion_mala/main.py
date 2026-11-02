# Ej1 — MALA (funciona): agregar un descuento obliga a editar la función con otro if.
def precio_final(precio, tipo):
    if tipo == "ninguno":
        return precio
    elif tipo == "normal":
        return precio * 0.9
    # para "black_friday" habría que venir aquí a meter otro elif
    return precio

print(precio_final(100, "ninguno"))
print(precio_final(100, "normal"))
