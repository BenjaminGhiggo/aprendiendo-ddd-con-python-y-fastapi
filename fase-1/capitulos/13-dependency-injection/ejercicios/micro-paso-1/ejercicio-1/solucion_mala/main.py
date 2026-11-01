# MALA: dependencia IMPLICITA. El handler importa y llama directo al email.
# Para testear habria que mock.patch en cada prueba.
def email_send(destino, mensaje): print("ENVIANDO EMAIL REAL a", destino)
def avisar_sin_stock(sku):
    email_send("stock@x.com", f"sin stock {sku}")   # atado a este email concreto
avisar_sin_stock("MESA")
