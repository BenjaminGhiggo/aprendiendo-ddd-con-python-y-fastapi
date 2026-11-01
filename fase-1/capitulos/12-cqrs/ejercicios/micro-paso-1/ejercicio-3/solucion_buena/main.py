# BUENA: handlers (escriben) separados de vistas (leen). Como mensajeria.py vs vistas.py.
datos = {}
# --- handlers: cambian estado ---
def guardar(clave, valor):
    datos[clave] = valor
# --- vistas: solo leen ---
def ver(clave):
    return datos.get(clave)
guardar("a", 1)
print("buena -> ver('a'):", ver("a"))
