# MALA: un if por tipo de evento para elegir el manejador.
def despachar(evento):
    if evento["tipo"] == "sin_stock":
        print("notificar", evento["sku"])
    elif evento["tipo"] == "asignado":
        print("registrar", evento["sku"])
despachar({"tipo": "sin_stock", "sku": "MESA"})
