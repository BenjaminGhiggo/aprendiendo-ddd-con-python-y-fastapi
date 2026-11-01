# MALA: try/except alrededor de TODO (también de comandos): oculta errores de ordenes.
def procesar(mensaje, handler):
    try: return handler(mensaje)
    except Exception: return None    # oculta incluso errores de comandos
print(procesar("Asignar", lambda m: (_ for _ in ()).throw(ValueError())))
