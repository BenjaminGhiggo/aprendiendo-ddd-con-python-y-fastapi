# Ej1 — BUENA: if/elif/else encadenados; se detiene en cuanto uno acierta.
# Cambia el valor de 'edad' (10, 30, 70) y vuelve a ejecutar.
edad = 30
if edad < 18:
    resultado = "menor"
elif edad < 65:
    resultado = "adulto"
else:
    resultado = "adulto mayor"
print(resultado)
