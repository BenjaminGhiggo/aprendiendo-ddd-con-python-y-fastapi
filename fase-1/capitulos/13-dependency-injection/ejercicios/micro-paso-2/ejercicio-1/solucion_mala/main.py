# MALA: el bus es un modulo con handlers FIJOS; no puedo darle otros (p. ej. para tests).
MANEJADORES = {"asignar": lambda m: f"asignado {m} (handler fijo)"}
def manejar(msg, tipo):
    return MANEJADORES[tipo](msg)
print(manejar("o1", "asignar"))   # siempre el mismo handler, no se puede configurar
