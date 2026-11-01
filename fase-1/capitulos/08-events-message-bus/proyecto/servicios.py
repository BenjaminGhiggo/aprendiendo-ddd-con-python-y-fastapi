import mensajeria
from modelo import Lote, LineaPedido, Producto


class SkuInvalido(Exception):
    pass


def agregar_lote(referencia, sku, cantidad, eta, uow):
    with uow:
        producto = uow.productos.obtener(sku)
        if producto is None:
            producto = Producto(sku, lotes=[])
            uow.productos.agregar(producto)
        producto.lotes.append(Lote(referencia, sku, cantidad, eta))
        uow.comprometer()


def asignar(id_pedido, sku, cantidad, uow) -> str:
    linea = LineaPedido(id_pedido, sku, cantidad)
    with uow:
        producto = uow.productos.obtener(sku)
        if producto is None:
            raise SkuInvalido(f"Sku inválido {sku}")
        referencia = producto.asignar(linea)
        uow.comprometer()
    for evento in getattr(producto, "eventos", []):
        mensajeria.manejar(evento)
    return referencia
