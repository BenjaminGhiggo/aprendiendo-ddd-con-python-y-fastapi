# excepciones.py

# 1. A veces una operación NO se puede hacer. En vez de devolver un valor "falso",
#    LANZAMOS (raise) una EXCEPCIÓN: una señal de error con nombre del dominio.
class SinStock(Exception):
    pass   # un tipo de error propio, con nombre que significa algo del negocio

def asignar(cantidad_disponible, pedido_cantidad):
    if pedido_cantidad > cantidad_disponible:
        raise SinStock("No hay stock suficiente")
    return cantidad_disponible - pedido_cantidad

# 2. Para MANEJAR el error usamos try / except.
#    Python intenta el bloque try; si salta la excepción, corre el except.
try:
    resto = asignar(10, 25)       # pide 25 pero hay 10 -> lanza SinStock
    print("Quedan:", resto)
except SinStock as error:
    print("No se pudo asignar:", error)

# 3. Si SÍ se puede, no hay error y el programa sigue normal.
resto = asignar(10, 4)
print("Quedan:", resto)           # 6
