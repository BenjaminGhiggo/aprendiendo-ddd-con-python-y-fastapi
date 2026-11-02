# nivel_avanzado.py — soluciones de los problemas 🔴 9–12 (README §10, Lección 13 · SRP).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/13-srp/paso5_solucionario/nivel_avanzado.py


# Problema 9: la clase "Dios" Tienda (agregar, total, imprimir_ticket, guardar) se divide
# en una pieza por motivo de cambio (receta S6).
class Carrito:                              # motivo: reglas de compra
    def __init__(self):
        self.items = {}

    def agregar(self, producto, precio):
        self.items[producto] = precio

    def total(self):
        return sum(self.items.values())


def formatear_ticket(carrito):              # motivo: formato del ticket
    return f"{len(carrito.items)} productos | total {carrito.total()}"


class RepositorioCarritos:                  # motivo: cómo se guarda
    def __init__(self):
        self._carritos = []

    def guardar(self, carrito):
        self._carritos.append(carrito)

    def contar(self):
        return len(self._carritos)


c = Carrito()
c.agregar("mesa", 100)
c.agregar("lámpara", 30)
repo = RepositorioCarritos()
repo.guardar(c)
print("P9:", formatear_ticket(c), "| guardados:", repo.contar())

# Problema 10: como total() no imprime ni guarda, probarlo es trivial (asserts).
assert c.total() == 130
assert Carrito().total() == 0
print("P10: OK (total() se prueba sin pantalla ni base de datos)")


# Problema 11: registrar_venta ya no llama a enviar_email adentro; recibe CÓMO avisar.
def registrar_venta(ventas, monto, avisar):
    ventas.append(monto)
    avisar(f"venta registrada: {monto}")


def avisar_email(msg):
    print("P11: EMAIL ->", msg)


def avisar_sms(msg):
    print("P11: SMS ->", msg)


ventas = []
registrar_venta(ventas, 50, avisar_email)
registrar_venta(ventas, 70, avisar_sms)     # cambié el canal SIN editar registrar_venta
print("P11: ventas =", ventas)


# Problema 12 (puente al libro, cap. 8): "allocate, not allocate_and_send_mail_if_out_of_stock".
def asignar(lotes, sku, cantidad):
    """Regla de dominio: elige el primer lote con stock suficiente. NO avisa a nadie."""
    for referencia, lote in lotes.items():
        if lote["sku"] == sku and lote["disponible"] >= cantidad:
            lote["disponible"] = lote["disponible"] - cantidad
            return referencia
    return None


def servicio_asignar(lotes, sku, cantidad, avisar):
    """Orquesta: llama a la regla y, si no hubo stock, decide avisar."""
    referencia = asignar(lotes, sku, cantidad)
    if referencia is None:
        avisar(f"sin stock para {sku}")
    return referencia


def avisar_tienda(msg):
    print("P12: aviso ->", msg)


lotes = {
    "lote-1": {"sku": "MESA", "disponible": 10},
    "lote-2": {"sku": "SILLA", "disponible": 3},
}
print("P12:", servicio_asignar(lotes, "MESA", 4, avisar_tienda))   # lote-1
print("P12:", servicio_asignar(lotes, "SILLA", 5, avisar_tienda))  # avisa y devuelve None
