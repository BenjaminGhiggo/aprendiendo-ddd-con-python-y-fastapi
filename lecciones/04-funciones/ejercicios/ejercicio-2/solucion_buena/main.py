# Ej2 — BUENA: la función DEVUELVE el número; quien llama decide qué hacer.
def total_con_igv(precio):
    return precio * 1.18

print(total_con_igv(100))
# Ahora sí puedo reutilizar el valor, por ejemplo sumarlo:
print(total_con_igv(100) + total_con_igv(50))
