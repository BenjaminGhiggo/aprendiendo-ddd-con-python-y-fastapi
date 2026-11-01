# MALA: inyectamos TODAS las deps a todos los handlers aunque no las pidan -> TypeError.
def h_a(msg, uow): return ("a", uow)
def h_b(msg, publicar): return ("b", publicar)
deps = {"uow": "UOW", "publicar": "PUB"}
try:
    print(h_a("m", **deps))   # h_a no acepta 'publicar' -> revienta
except TypeError as e:
    print("mala -> TypeError:", e)
