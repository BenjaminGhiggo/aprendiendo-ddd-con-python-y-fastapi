# MALA: el fallo de un handler de evento rompe todo el flujo.
def registrar(e): print("registrado")
def notificar(e): raise Exception("email caido")
for h in [notificar, registrar]:
    h("Asignado")       # notificar revienta y 'registrar' nunca corre
