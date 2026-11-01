# Ej1 — MALA: todo en un bloque: leer, decidir y actuar mezclados.
datos = {"a": 1, "b": -2, "c": -3}
for k, v in datos.items():
    if v < 0:
        print("quitar", k)   # imposible probar la decisión sin ejecutar el efecto
