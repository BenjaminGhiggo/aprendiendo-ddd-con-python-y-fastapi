# MALA: se carga una PARTE interna (un lote) y se modifica fuera del agregado.
producto = {"sku":"MESA", "lotes":[{"ref":"l1","disp":100}]}
lote = producto["lotes"][0]
lote["disp"] -= 10          # cambio por fuera del agregado
print(producto)
