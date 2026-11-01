# BUENA: A publica un evento; B lo consume cuando pueda (desacoplado en el tiempo).
canal = []
def servicio_a():
    canal.append(("pedido_creado", "pedido"))   # publica y sigue
servicio_a()
print("publicado:", canal)                       # B lo leera despues
