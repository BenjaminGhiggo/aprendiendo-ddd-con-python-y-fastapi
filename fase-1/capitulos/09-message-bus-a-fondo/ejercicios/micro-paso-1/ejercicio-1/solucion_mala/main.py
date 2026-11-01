# MALA: un handler llama a otro handler directamente (acoplado, sin cascada).
def registrar(ref): print("registrar", ref)
def asignar(sku):
    ref = "l1"
    registrar(ref)        # el handler conoce al siguiente handler
asignar("MESA")
