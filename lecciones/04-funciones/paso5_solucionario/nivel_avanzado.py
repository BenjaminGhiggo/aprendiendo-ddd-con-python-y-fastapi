# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/04-funciones/paso5_solucionario/nivel_avanzado.py


# Problema 9: acumular dentro de una función con while (Lección 03) y devolver.
def sumar_hasta(n):
    suma = 0
    i = 1
    while i <= n:
        suma = suma + i     # vuelta a vuelta: 1, 3, 6, 10, 15
        i = i + 1
    return suma


print("P9:", sumar_hasta(5))                     # 15


# Problema 10: varios return temprano (F11) para clasificar.
def clasificar_stock(cantidad):
    if cantidad == 0:
        return "agotado"
    if cantidad < 5:
        return "bajo"
    return "ok"


print("P10:", clasificar_stock(0), clasificar_stock(3), clasificar_stock(10))   # agotado bajo ok


# Problema 11: una función que llama a otra (F12) y usa un valor por defecto (F8).
def calcular_total(precio, cantidad):
    return precio * cantidad


def total_con_envio(precio, cantidad, envio=5):
    return calcular_total(precio, cantidad) + envio


print("P11:", total_con_envio(10, 3), total_con_envio(10, 3, 0))   # 35 30


# Problema 12 (puente al libro): con anotaciones, como
# "def allocate(line: OrderLine, batches: List[Batch]) -> str:" (cap. 1).
def asignar(disponible: int, pedido: int) -> int:
    if pedido > disponible:
        return disponible           # no alcanza: no cambia (en la Lección 07 será un error SinStock)
    return disponible - pedido


print("P12:", asignar(20, 5), asignar(20, 25))   # 15 20
