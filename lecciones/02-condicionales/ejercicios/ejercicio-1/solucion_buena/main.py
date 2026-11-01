# Ej1 — BUENA: if/elif/else encadenados; para en cuanto uno acierta.
def clasificar(edad):
    if edad < 18:
        return "menor"
    elif edad < 65:
        return "adulto"
    else:
        return "adulto mayor"

print(clasificar(10))
print(clasificar(30))
print(clasificar(70))
