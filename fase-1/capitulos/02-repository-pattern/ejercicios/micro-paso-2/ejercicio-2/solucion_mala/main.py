# Ej2 — MALA: el modelo lleva dentro detalles de la base de datos (acoplado).
class Lote:
    tabla = "lotes"                       # el dominio "sabe" de la BD
    columnas = ["referencia", "sku"]
    def __init__(self, referencia, sku):
        self.referencia = referencia
        self.sku = sku

print(Lote.tabla, Lote.columnas)
