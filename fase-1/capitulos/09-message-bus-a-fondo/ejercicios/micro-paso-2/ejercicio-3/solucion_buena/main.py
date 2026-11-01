# BUENA: el bus junta los resultados y los devuelve.
def handler(_): return "l1"
MANEJADORES = {"asignar": [handler]}
def manejar(e):
    return [m(e) for m in MANEJADORES[e]]
print(manejar("asignar")[0])
