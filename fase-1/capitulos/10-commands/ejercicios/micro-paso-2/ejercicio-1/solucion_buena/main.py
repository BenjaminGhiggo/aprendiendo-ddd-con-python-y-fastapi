# BUENA: cada handler de evento se aísla; un fallo no tumba a los demás.
def registrar(e): print("registrado")
def notificar(e): raise Exception("email caido")
for h in [notificar, registrar]:
    try: h("Asignado")
    except Exception: pass   # aislado
