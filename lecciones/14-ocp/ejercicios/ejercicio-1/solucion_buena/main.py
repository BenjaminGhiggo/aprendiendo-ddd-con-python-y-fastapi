# Ej1 — BUENA: cada descuento es una función; agregar uno no toca precio_final.
def sin_descuento(precio):
    return precio
def descuento_normal(precio):
    return precio * 0.9
def descuento_black_friday(precio):   # NUEVO, sin tocar nada de lo anterior
    return precio * 0.5

def precio_final(precio, regla):
    return regla(precio)

print(precio_final(100, sin_descuento))
print(precio_final(100, descuento_normal))
print(precio_final(100, descuento_black_friday))
