# nivel_basico.py — soluciones de los problemas 🟢 1–4 (README §10).
# Intenta resolverlos tú ANTES de abrir este archivo.
# Ejecuta:  uv run python lecciones/05-listas-y-diccionarios/paso5_solucionario/nivel_basico.py

# Problema 1: crea la lista de colores e imprime el SEGUNDO (posición 1, porque empieza en 0).
colores = ["rojo", "verde", "azul"]
print("P1:", colores[1])                 # verde

# Problema 2: el último SIN usar len -> índice negativo (L4).
print("P2:", colores[-1])                # azul

# Problema 3: agrega "negro" (L7) y cuenta (L6).
colores.append("negro")
print("P3:", len(colores))               # 4

# Problema 4: diccionario de precios; leer por clave (D3).
precios = {"pan": 1, "leche": 4}
print("P4:", precios["leche"])           # 4
