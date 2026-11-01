# BUENA: inspeccionamos la firma y pasamos SOLO lo que cada handler pide (como bootstrap.py).
import inspect
def inyectar(handler, deps):
    params = inspect.signature(handler).parameters
    usa = {n: d for n, d in deps.items() if n in params}
    return lambda msg: handler(msg, **usa)
def h_a(msg, uow): return ("a", uow)
def h_b(msg, publicar): return ("b", publicar)
deps = {"uow": "UOW", "publicar": "PUB"}
print(inyectar(h_a, deps)("m"))
print(inyectar(h_b, deps)("m"))
