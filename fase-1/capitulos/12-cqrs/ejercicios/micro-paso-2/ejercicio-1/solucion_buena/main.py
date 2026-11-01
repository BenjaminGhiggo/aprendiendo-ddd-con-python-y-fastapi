# BUENA: tabla DESNORMALIZADA de lectura; leer es un "SELECT WHERE" directo.
asignaciones_vista = [
    {"pedido": "p1", "sku": "MESA", "ref": "l1"},   # ya aplanado, listo para leer
]
def asignaciones_de(pedido):
    return [{"sku": f["sku"], "ref": f["ref"]}
            for f in asignaciones_vista if f["pedido"] == pedido]
print("buena:", asignaciones_de("p1"))
