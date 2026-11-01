# Ej1 — MALA: la función DECIDE y ACTÚA (borra) a la vez; difícil de probar.
def limpiar(numeros):
    for n in numeros:
        if n < 0:
            print("borrando", n)   # efecto (I/O) mezclado con la decisión

limpiar([1, -2, 3, -4])
