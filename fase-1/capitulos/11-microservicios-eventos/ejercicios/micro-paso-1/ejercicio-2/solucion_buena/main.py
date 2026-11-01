# BUENA: separar eventos internos (bus) de externos (canal).
INTERNOS = ["Asignado", "SinStock"]
EXTERNOS = ["LineaAsignada"]     # estos se publican a otros servicios
print("internos:", INTERNOS, "| externos:", EXTERNOS)
