# paso2_ejemplos_resueltos.py — PASO 2 de la Lección 13 (SRP).
# Los 4 ejemplos resueltos del README (§9): siempre VIOLACIÓN -> REFACTOR.
# Ejecuta:  uv run python lecciones/13-srp/paso2_ejemplos_resueltos.py

print("--- Ejemplo 1: pedido que calcula y arma el recibo (fácil) ---")


# Paso 1 (violación): una clase con DOS razones para cambiar.
class PedidoTodo:
    def __init__(self, precios):
        self.precios = precios

    def total(self):
        return sum(self.precios)

    def imprimir_recibo(self):
        print("Total a pagar:", self.total())


PedidoTodo([10, 20, 30]).imprimir_recibo()


# Paso 2 (refactor): la regla en la clase, la presentación en una función aparte.
class Pedido:
    def __init__(self, precios):
        self.precios = precios

    def total(self):
        return sum(self.precios)


def formatear_recibo(pedido):
    return f"Total a pagar: {pedido.total()}"


# Paso 3 (uso): cada pieza hace UNA cosa.
print(formatear_recibo(Pedido([10, 20, 30])))

print()
print("--- Ejemplo 2: función con 'y' en el nombre (fácil) ---")


# Paso 1 (violación): calcula Y muestra. No puedo usar el promedio sin imprimirlo.
def calcular_y_mostrar_promedio(notas):
    print("Promedio:", sum(notas) / len(notas))


calcular_y_mostrar_promedio([12, 15, 18])


# Paso 2 (refactor): una función calcula (devuelve), otra muestra.
def promedio(notas):
    return sum(notas) / len(notas)


def mostrar(etiqueta, valor):
    print(etiqueta, valor)


# Paso 3 (uso): ahora el promedio sirve también para decidir, no solo para mostrar.
p = promedio([12, 15, 18])
mostrar("Promedio:", p)
print("¿Aprobado?", p >= 11)

print()
print("--- Ejemplo 3: pedido que además se guarda (intermedio) ---")


# Paso 1 (violación): la clase sabe calcular Y sabe guardarse.
class PedidoQueSeGuarda:
    base_de_datos = []                      # (simulada)

    def __init__(self, precios):
        self.precios = precios

    def total(self):
        return sum(self.precios)

    def guardar(self):
        PedidoQueSeGuarda.base_de_datos.append(self)


# Paso 2 (refactor): guardar pasa a un REPOSITORIO (el patrón del cap. 2 del libro).
class RepositorioPedidos:
    def __init__(self):
        self._pedidos = []

    def guardar(self, pedido):
        self._pedidos.append(pedido)

    def contar(self):
        return len(self._pedidos)


# Paso 3 (uso): el pedido no sabe nada de guardar; el repositorio sí.
repo = RepositorioPedidos()
repo.guardar(Pedido([5, 5]))
repo.guardar(Pedido([1, 2, 3]))
print("Pedidos guardados:", repo.contar())
print("¿Pedido sabe guardarse?", hasattr(Pedido([1]), "guardar"))

print()
print("--- Ejemplo 4: asignar que también manda email, como en el cap. 8 (avanzado) ---")


# Paso 1 (violación): la regla de asignar decide Y envía el aviso.
def asignar_y_enviar_email(stock, sku, cantidad):
    if stock.get(sku, 0) >= cantidad:
        stock[sku] = stock[sku] - cantidad
        return "asignado"
    print("EMAIL: sin stock de", sku)       # cambiar a SMS obliga a tocar ESTA regla
    return "sin stock"


print(asignar_y_enviar_email({"MESA": 2}, "MESA", 5))


# Paso 2 (refactor): la regla solo asigna y devuelve el resultado.
def asignar(stock, sku, cantidad):
    if stock.get(sku, 0) >= cantidad:
        stock[sku] = stock[sku] - cantidad
        return True
    return False


def avisar_sms(mensaje):
    print("SMS:", mensaje)


# Paso 3 (orquestar): otra función junta las piezas y elige el canal del aviso.
def servicio_asignar(stock, sku, cantidad, avisar):
    if asignar(stock, sku, cantidad):
        return "asignado"
    avisar(f"sin stock de {sku}")
    return "sin stock"


print(servicio_asignar({"MESA": 2}, "MESA", 5, avisar_sms))   # cambié a SMS sin tocar asignar
print(servicio_asignar({"MESA": 9}, "MESA", 5, avisar_sms))
