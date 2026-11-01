# MALA: el fallo de un handler de evento rompe el resto (sin aislar).
def registrar(e): print("registrado")
def notificar(e): raise Exception("email caido")
corridos = []
try:
    for h in [notificar, registrar]:   # notificar revienta y corta el bucle
        h("Asignado"); corridos.append(h.__name__)
except Exception:
    pass
print("handlers completados:", len(corridos))   # 0 -> 'registrar' nunca corrió
