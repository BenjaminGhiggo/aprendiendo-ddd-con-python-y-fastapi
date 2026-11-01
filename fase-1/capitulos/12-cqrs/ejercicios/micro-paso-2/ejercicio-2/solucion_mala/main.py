# MALA: escribimos en el modelo de escritura y NOS OLVIDAMOS de actualizar la vista.
escritura = []
vista = []
def asignar(pedido, sku, ref):
    escritura.append((pedido, sku, ref))       # solo el write; la vista queda vieja
asignar("p1", "MESA", "l1")
print("mala -> escritura:", escritura, "| vista:", vista, "(desactualizada)")
