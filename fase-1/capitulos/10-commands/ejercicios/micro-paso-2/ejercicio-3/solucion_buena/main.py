# BUENA: try/except SOLO para eventos; los comandos propagan.
def procesar_comando(m, handler): return handler(m)   # propaga
def procesar_evento(m, handler):
    try: handler(m)
    except Exception: pass
try: procesar_comando("Asignar", lambda m: (_ for _ in ()).throw(ValueError("x")))
except ValueError: print("comando propago; evento se habria aislado")
