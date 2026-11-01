# BUENA: comandos (un handler) y eventos (varios), separados.
MANEJADORES_COMANDO = {"Asignar": "handler_asignar"}       # uno
MANEJADORES_EVENTO = {"Asignado": ["registrar", "notificar"]}  # varios
print(MANEJADORES_COMANDO["Asignar"], "|", MANEJADORES_EVENTO["Asignado"])
