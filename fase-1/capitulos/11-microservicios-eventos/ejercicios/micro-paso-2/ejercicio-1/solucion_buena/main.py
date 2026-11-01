# BUENA: el adaptador solo TRADUCE; la lógica vive en el bus/dominio.
def manejar_comando(comando): return "procesado " + comando["ref"]
def consumir(mensaje):
    comando = {"tipo": "CambiarCantidad", "ref": mensaje["ref"], "cantidad": mensaje["cantidad"]}
    return manejar_comando(comando)   # delega
print(consumir({"ref": "l1", "cantidad": 5}))
