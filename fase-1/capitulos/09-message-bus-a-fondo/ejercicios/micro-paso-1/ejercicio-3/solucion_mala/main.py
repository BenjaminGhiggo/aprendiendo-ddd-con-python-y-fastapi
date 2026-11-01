# MALA: no se rastrea qué productos se tocaron; no se sabe de dónde recoger eventos.
productos = {"MESA": ["evento1"]}
def obtener(sku): return productos[sku]
obtener("MESA")
print("vistos: ninguno")        # no hay forma de saber qué se tocó
