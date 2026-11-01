# Ej1 — BUENA: el núcleo DECIDE (devuelve datos); la cáscara ACTÚA.
def decidir_borrados(numeros):
    return [("BORRAR", n) for n in numeros if n < 0]   # puro: entra data, sale data

acciones = decidir_borrados([1, -2, 3, -4])
print(acciones)
for accion, n in acciones:
    print("borrando", n)   # el efecto vive aparte
