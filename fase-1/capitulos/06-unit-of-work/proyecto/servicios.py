# servicios.py — ahora reciben una UoW (no repo+sesión sueltos).
import modelo
from modelo import Lote, LineaPedido


class SkuInvalido(Exception):
    pass


def sku_valido(sku, lotes):
    return sku in {lote.sku for lote in lotes}


def agregar_lote(referencia, sku, cantidad, eta, uow):
    with uow:
        uow.lotes.agregar(Lote(referencia, sku, cantidad, eta))
        uow.comprometer()


def asignar(id_pedido, sku, cantidad, uow) -> str:
    linea = LineaPedido(id_pedido, sku, cantidad)
    with uow:
        lotes = uow.lotes.listar()
        if not sku_valido(linea.sku, lotes):
            raise SkuInvalido(f"Sku inválido {linea.sku}")
        referencia = modelo.asignar(linea, lotes)
        uow.comprometer()
    return referencia
