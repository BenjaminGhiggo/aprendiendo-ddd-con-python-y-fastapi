# BUENA: un comando tiene UN handler (un responsable).
def manejar_comando(handler, c):
    return handler(c)
print(manejar_comando(lambda c: f"ok {c}", "Asignar"))
