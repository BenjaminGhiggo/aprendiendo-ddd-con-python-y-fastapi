# Ej3 — BUENA: núcleo puro que DEVUELVE; el print queda afuera.
def total_mayor(a, b):
    return a if a > b else b

print(total_mayor(3, 7))
print(total_mayor(3, 7) + total_mayor(1, 2))
