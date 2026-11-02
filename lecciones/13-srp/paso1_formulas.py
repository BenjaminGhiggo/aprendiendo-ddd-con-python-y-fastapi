# paso1_formulas.py — PASO 1 de la Lección 13 (SRP).
# Cada bloque es una "receta" de la tabla del README (§5), con su código (S1...S6).
# En cada una verás el ANTES (mezclado) y el DESPUÉS (separado), y la evidencia impresa.
# Ejecuta:  uv run python lecciones/13-srp/paso1_formulas.py


# ---------------------------------------------------------------------------
# S1 · Regla de negocio separada de la PRESENTACIÓN
# Olor: la clase calcula Y además arma el texto para mostrar.
# ---------------------------------------------------------------------------
class PedidoMezclado:                       # ANTES: dos razones para cambiar
    def __init__(self, precios):
        self.precios = precios

    def total(self):
        return sum(self.precios)

    def recibo(self):                       # presentación metida en la regla
        return f"Total a pagar: {self.total()}"


class Pedido:                               # DESPUÉS: solo la regla de negocio
    def __init__(self, precios):
        self.precios = precios

    def total(self):
        return sum(self.precios)


def formatear_recibo(pedido):               # DESPUÉS: solo la presentación
    return f"Total a pagar: {pedido.total()}"


pedido = Pedido([10, 20, 30])
print("S1  antes  :", PedidoMezclado([10, 20, 30]).recibo())
print("S1  después:", pedido.total(), "|", formatear_recibo(pedido))


# ---------------------------------------------------------------------------
# S2 · Regla de negocio separada de la PERSISTENCIA (guardar)
# Olor: la clase calcula Y se guarda a sí misma.
# ---------------------------------------------------------------------------
class RepositorioPedidos:                   # DESPUÉS: guardar es OTRA responsabilidad
    def __init__(self):
        self._guardados = []                # (simulamos la base de datos con una lista)

    def guardar(self, pedido):
        self._guardados.append(pedido)

    def contar(self):
        return len(self._guardados)


repo = RepositorioPedidos()
repo.guardar(pedido)
print("S2  después: pedidos guardados =", repo.contar(), "| Pedido tiene 'guardar'?", hasattr(pedido, "guardar"))


# ---------------------------------------------------------------------------
# S3 · Función con "y" en el nombre -> dos funciones + una que ORQUESTA
# ---------------------------------------------------------------------------
def calcular_y_mostrar_promedio(notas):     # ANTES: calcula Y muestra
    print("S3  antes  : promedio =", sum(notas) / len(notas))


def promedio(notas):                        # DESPUÉS: solo calcula (devuelve)
    return sum(notas) / len(notas)


def mostrar_promedio(valor):                # DESPUÉS: solo muestra
    print("S3  después: promedio =", valor)


calcular_y_mostrar_promedio([12, 15, 18])
mostrar_promedio(promedio([12, 15, 18]))    # la orquestación queda a la vista


# ---------------------------------------------------------------------------
# S4 · Núcleo PURO (recibe datos, devuelve resultado) y BORDE (print/input)
# Olor: la misma función pide datos, calcula e imprime.
# ---------------------------------------------------------------------------
def con_igv(monto):                         # núcleo: no imprime, no pide nada
    return monto * 118 / 100


def mostrar_monto(etiqueta, monto):         # borde: solo habla con la pantalla
    print(f"S4  después: {etiqueta} = {monto}")


mostrar_monto("con IGV", con_igv(100))


# ---------------------------------------------------------------------------
# S5 · La regla de negocio NO envía avisos: devuelve el hecho; otro decide avisar
# (idea del cap. 8: allocate no debe llamarse allocate_and_send_mail_if_out_of_stock)
# ---------------------------------------------------------------------------
def hay_stock(stock, sku, cantidad):        # regla: solo responde sí/no
    return stock.get(sku, 0) >= cantidad


def avisar_email(mensaje):                  # aviso: otra responsabilidad
    print("S5  después: EMAIL ->", mensaje)


stock = {"MESA": 2}
if not hay_stock(stock, "MESA", 5):         # quien orquesta decide si avisar
    avisar_email("sin stock de MESA")


# ---------------------------------------------------------------------------
# S6 · Clase "Dios" (Manager/Utils/Tienda que hace todo) -> una clase por motivo
# ---------------------------------------------------------------------------
class Carrito:                              # motivo: reglas de compra
    def __init__(self):
        self.items = {}

    def agregar(self, producto, precio):
        self.items[producto] = precio

    def total(self):
        return sum(self.items.values())


def ticket(carrito):                        # motivo: formato del ticket
    return f"{len(carrito.items)} productos, total {carrito.total()}"


carrito = Carrito()
carrito.agregar("mesa", 100)
carrito.agregar("silla", 50)
print("S6  después:", ticket(carrito))
