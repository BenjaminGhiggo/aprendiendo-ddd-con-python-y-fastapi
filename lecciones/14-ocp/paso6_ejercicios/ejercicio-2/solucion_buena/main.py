# Ej2 — BUENA: una tabla (dict) de costos; agregar un país no toca la función.
COSTOS = {"PE": 10, "CL": 15}   # para un país nuevo, solo se agrega una entrada

def costo_envio(pais):
    return COSTOS.get(pais, 0)

print(costo_envio("PE"))
print(costo_envio("CL"))
