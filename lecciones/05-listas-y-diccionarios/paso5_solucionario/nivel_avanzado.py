# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/05-listas-y-diccionarios/paso5_solucionario/nivel_avanzado.py

# Problema 9: contar palabras -> el patrón "contador" del Ejemplo 3 (D4 + 1).
palabras = ["mesa", "silla", "mesa", "cama", "mesa"]
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("P9:", conteo)                     # {'mesa': 3, 'silla': 1, 'cama': 1}

# Problema 10: recorrer el diccionario y JUNTAR en una lista los que tienen 0.
stock = {"mesa": 10, "silla": 0, "cama": 4}
agotados = []                            # lista vacía (L2) donde iremos juntando
for producto, cantidad in stock.items():
    if cantidad == 0:
        agotados.append(producto)        # L7
print("P10:", agotados)                  # ['silla']

# Problema 11: leer una clave que NO existe sin que el programa reviente (D4).
print("P11:", stock.get("sofá", 0))      # 0

# Problema 12 (puente al libro): un diccionario cuyo valor es una LISTA de funciones,
# igual que HANDLERS = {events.OutOfStock: [send_out_of_stock_notification]} (cap. 8).
def registrar(pedido):
    print("P12: registrado el pedido", pedido)


def avisar_cliente(pedido):
    print("P12: avisado el cliente del pedido", pedido)


MANEJADORES = {"Asignado": [registrar, avisar_cliente]}
for funcion in MANEJADORES["Asignado"]:
    funcion("o1")
