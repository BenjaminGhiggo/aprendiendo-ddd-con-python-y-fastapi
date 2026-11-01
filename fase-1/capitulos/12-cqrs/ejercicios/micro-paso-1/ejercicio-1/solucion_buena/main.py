# BUENA: una funcion cambia estado (command) y OTRA responde (query). CQS.
stock = {"MESA": 10}
def asignar(sku, cantidad):         # command: solo cambia estado
    stock[sku] -= cantidad
def disponible(sku):                # query: solo responde
    return stock[sku]
asignar("MESA", 3)
print("buena -> disponible:", disponible("MESA"), "| stock:", stock)
