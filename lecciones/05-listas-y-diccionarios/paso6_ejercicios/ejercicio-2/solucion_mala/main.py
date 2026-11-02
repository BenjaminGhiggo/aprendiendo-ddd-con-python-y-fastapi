# Ej2 — MALA (funciona): busca un precio recorriendo listas paralelas con índices.
productos = ["mesa", "silla", "lampara"]
precios = [100, 50, 30]
buscado = "lampara"
i = 0
while i < 3:
    if productos[i] == buscado:
        print(precios[i])
    i = i + 1
