# ocp.py  -> OCP: abierto a EXTENSIÓN, cerrado a MODIFICACIÓN.
# Agregamos comportamientos nuevos SIN editar el código que ya funciona.

# Cada "regla de descuento" es una función independiente.
def sin_descuento(precio):
    return precio

def descuento_10(precio):
    return precio * 0.9

def descuento_black_friday(precio):   # NUEVO: lo agrego sin tocar nada de lo anterior
    return precio * 0.5

# Esta función NO cambia aunque agreguemos reglas nuevas: recibe la regla como dato.
def precio_final(precio, regla_descuento):
    return regla_descuento(precio)

print(precio_final(100, sin_descuento))           # 100
print(precio_final(100, descuento_10))            # 90.0
print(precio_final(100, descuento_black_friday))  # 50.0
