# Ej2 — BUENA: el modelo es puro; el esquema vive aparte (como orm.py).
class Lote:
    def __init__(self, referencia, sku):
        self.referencia = referencia
        self.sku = sku

# esquema definido por separado (el "orm" conoce al modelo, no al reves)
ESQUEMA = {"tabla": "lotes", "columnas": ["referencia", "sku"]}
print(ESQUEMA["tabla"], ESQUEMA["columnas"])
print("el modelo no sabe de BD:", hasattr(Lote, "tabla"))
