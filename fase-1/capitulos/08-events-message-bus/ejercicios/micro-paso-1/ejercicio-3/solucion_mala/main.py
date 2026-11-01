# MALA: lanzar una excepción para "avisar" (mezcla error con notificacion).
class SinStock(Exception): pass
def asignar(hay_stock):
    if not hay_stock: raise SinStock()   # el que llama debe atrapar para "avisar"
try: asignar(False)
except SinStock: print("avisar...")
