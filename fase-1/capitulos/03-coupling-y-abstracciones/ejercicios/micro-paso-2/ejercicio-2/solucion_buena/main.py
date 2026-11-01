# Ej2 — BUENA: la lógica se prueba con datos simples (sin disco).
def sobran(origen, destino):
    return [n for n in destino if n not in origen]

print(sobran({"fn1"}, {"fn1", "sobra.txt"}))   # ['sobra.txt']
