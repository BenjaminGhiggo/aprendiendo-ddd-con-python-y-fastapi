# BUENA: un handler de evento mantiene la vista al dia (como agregar_asignacion_a_vista).
escritura = []
vista = []
def agregar_a_vista(evento):                   # handler del evento Asignado
    vista.append(evento)
def asignar(pedido, sku, ref):
    escritura.append((pedido, sku, ref))       # write
    agregar_a_vista({"pedido": pedido, "sku": sku, "ref": ref})  # evento -> actualiza vista
asignar("p1", "MESA", "l1")
print("buena -> vista:", vista, "(al dia)")
