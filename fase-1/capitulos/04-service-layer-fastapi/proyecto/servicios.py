# servicios.py — la CAPA DE SERVICIOS: orquesta el caso de uso "asignar".
# No tiene lógica de negocio (esa vive en el modelo); coordina repo + modelo + commit.
import modelo
from modelo import LineaPedido


class SkuInvalido(Exception):
    pass


def sku_valido(sku, lotes):
    return sku in {lote.sku for lote in lotes}


def asignar(linea: LineaPedido, repo, sesion) -> str:
    lotes = repo.listar()                                   # 1. traer del repositorio
    if not sku_valido(linea.sku, lotes):                    # 2. validar la entrada
        raise SkuInvalido(f"Sku inválido {linea.sku}")
    referencia = modelo.asignar(linea, lotes)               # 3. llamar al dominio
    sesion.commit()                                         # 4. confirmar
    return referencia
