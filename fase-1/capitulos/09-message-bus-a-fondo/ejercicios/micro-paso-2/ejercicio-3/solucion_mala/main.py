# MALA: devolver el resultado por un canal raro (variable global).
RESULTADO = None
def handler():
    global RESULTADO
    RESULTADO = "l1"
handler(); print(RESULTADO)
