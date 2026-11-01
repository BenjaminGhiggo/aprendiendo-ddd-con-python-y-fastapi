# BUENA: dependencia EXPLICITA. El handler recibe 'enviar' como argumento (DIP).
# En el test le paso un doble; en produccion, el real. Sin mocks.
def avisar_sin_stock(sku, enviar):
    enviar("stock@x.com", f"sin stock {sku}")
enviados = []
avisar_sin_stock("MESA", lambda d, m: enviados.append((d, m)))   # doble de test
print("buena -> enviados:", enviados)
