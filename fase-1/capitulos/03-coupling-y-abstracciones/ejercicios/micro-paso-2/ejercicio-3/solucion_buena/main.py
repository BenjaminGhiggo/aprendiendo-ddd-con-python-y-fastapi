# Ej3 — BUENA: la decisión (filtrar .tmp) está en el núcleo; la cáscara solo aplica.
def decidir(archivos):
    return [("COPIAR", f) for f in archivos if not f.endswith(".tmp")]

def aplicar(acciones):
    for a in acciones:
        print("hacer", a)

aplicar(decidir(["x.tmp", "y.txt"]))
