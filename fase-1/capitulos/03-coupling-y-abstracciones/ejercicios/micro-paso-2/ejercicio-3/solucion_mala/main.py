# Ej3 — MALA: la cáscara también decide (otro if de negocio adentro del bucle de I/O).
def aplicar(acciones):
    for a in acciones:
        if a[0] == "COPIAR" and a[1].endswith(".tmp"):   # ¡regla de negocio en la cáscara!
            continue
        print("hacer", a)

aplicar([("COPIAR", "x.tmp"), ("COPIAR", "y.txt")])
