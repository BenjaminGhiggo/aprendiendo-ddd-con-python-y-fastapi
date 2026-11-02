# Ej3 — MALA (funciona): el que llama debe acordarse de chequear el error a mano.
def dividir(a, b):
    if b == 0:
        return None
    return a / b

r = dividir(10, 0)
# Si olvido este if, "r" es None y el programa sigue como si nada.
if r is None:
    print("No se puede dividir entre cero")
else:
    print(r)
