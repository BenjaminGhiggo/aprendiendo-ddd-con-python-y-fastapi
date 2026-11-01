# MALA: para leer, recorremos el modelo de dominio (productos->lotes->asignaciones) a mano.
productos = [
    {"sku": "MESA", "lotes": [{"ref": "l1", "lineas": [{"pedido": "p1"}]}]},
]
def asignaciones_de(pedido):
    out = []
    for p in productos:                        # bucles sobre el dominio: lento y clunky
        for lote in p["lotes"]:
            for linea in lote["lineas"]:
                if linea["pedido"] == pedido:
                    out.append({"sku": p["sku"], "ref": lote["ref"]})
    return out
print("mala:", asignaciones_de("p1"))
