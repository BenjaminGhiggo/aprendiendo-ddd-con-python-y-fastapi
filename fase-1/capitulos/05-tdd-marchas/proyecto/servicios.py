# servicios.py — la capa de servicios recibe PRIMITIVOS (str/int), no objetos de dominio.
# Así los tests de servicios quedan DESACOPLADOS del modelo (usan strings/ints).
import modelo
from modelo import Lote, LineaPedido


class SkuInvalido(Exception):
    pass


def sku_valido(sku, lotes):
    return sku in {lote.sku for lote in lotes}


def agregar_lote(referencia, sku, cantidad, eta, repo, sesion):
    repo.agregar(Lote(referencia, sku, cantidad, eta))
    sesion.commit()


def asignar(id_pedido, sku, cantidad, repo, sesion) -> str:
    linea = LineaPedido(id_pedido, sku, cantidad)        # el servicio arma la línea
    lotes = repo.listar()
    if not sku_valido(linea.sku, lotes):
        raise SkuInvalido(f"Sku inválido {linea.sku}")
    referencia = modelo.asignar(linea, lotes)
    sesion.commit()
    return referencia
