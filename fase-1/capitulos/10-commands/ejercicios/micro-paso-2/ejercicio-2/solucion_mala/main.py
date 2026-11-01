# MALA: el error de un COMANDO se traga (quien ordenó no se entera).
def handler_comando(c): raise ValueError("sku invalido")
try:
    handler_comando("Asignar")
except Exception:
    pass                # se silencia: la API devolveria 200 aunque fallo
print("respondio OK (mal)")
