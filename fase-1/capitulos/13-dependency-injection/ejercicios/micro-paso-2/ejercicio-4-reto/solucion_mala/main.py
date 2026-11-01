# MALA: la eleccion del canal esta REGADA dentro de cada handler.
def handler_1(msg): print("EMAIL:", msg)   # para cambiar a Slack...
def handler_2(msg): print("EMAIL:", msg)   # ...hay que editar CADA handler
handler_1("a"); handler_2("b")
