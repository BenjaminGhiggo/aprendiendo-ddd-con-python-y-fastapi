# MALA: un comando con varios handlers (ambiguo: ¿quién es el responsable?).
def manejar_comando(handlers, c):
    for h in handlers: h(c)         # varios responsables para una orden
manejar_comando([lambda c: print("a"), lambda c: print("b")], "Asignar")
