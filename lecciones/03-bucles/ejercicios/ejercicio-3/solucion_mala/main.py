# Ej3 — MALA (funciona): recorre una lista con while + índice manual (frágil).
nombres = ["Ana", "Benjamin", "Carla"]
i = 0
while i < 3:               # el 3 está escrito a mano: si la lista cambia, falla
    print(nombres[i])
    i = i + 1
