# BUENA: el handler EMITE un evento; el bus llama a los siguientes.
cola = []
def registrar(ref): print("registrar", ref)
MANEJADORES = {"asignado": [lambda ref: registrar(ref)]}
def manejar(evento, dato):
    cola.append((evento, dato))
    while cola:
        e, d = cola.pop(0)
        for m in MANEJADORES.get(e, []): m(d)
def asignar(sku):
    manejar("asignado", "l1")   # emite; no conoce al siguiente
asignar("MESA")
