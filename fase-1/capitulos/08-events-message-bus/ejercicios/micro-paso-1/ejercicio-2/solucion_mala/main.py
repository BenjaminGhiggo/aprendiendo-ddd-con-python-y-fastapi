# MALA: evento como diccionario suelto (sin tipo, fácil de romper).
evento = {"tipo": "sin_stock", "sku": "MESA"}
if evento["tipo"] == "sin_stock":
    print("sku:", evento["sku"])
