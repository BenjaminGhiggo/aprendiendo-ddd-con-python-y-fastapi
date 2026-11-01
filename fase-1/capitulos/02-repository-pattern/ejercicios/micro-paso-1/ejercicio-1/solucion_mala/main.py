# Ej1 — MALA (funciona): el servicio guarda directo en una lista global (acoplado).
_BD = []
def registrar_lote(referencia):
    _BD.append(referencia)   # no puedo cambiar el almacenamiento ni probar sin tocar esto

registrar_lote("L1")
print(_BD)
