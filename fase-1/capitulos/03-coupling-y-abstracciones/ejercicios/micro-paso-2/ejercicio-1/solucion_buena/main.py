# Ej1 — BUENA: 3 pasos: reunir, decidir (núcleo), aplicar.
def decidir(datos):                        # núcleo puro
    return [("QUITAR", k) for k, v in datos.items() if v < 0]

def procesar(datos):                       # cáscara
    acciones = decidir(datos)              # 2) decidir
    for accion, k in acciones:             # 3) aplicar
        print(accion.lower(), k)

procesar({"a": 1, "b": -2, "c": -3})
