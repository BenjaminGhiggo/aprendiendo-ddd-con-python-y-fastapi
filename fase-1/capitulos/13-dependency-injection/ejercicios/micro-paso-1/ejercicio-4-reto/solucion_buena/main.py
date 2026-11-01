# BUENA: functools.partial bindea el valor AHORA; cada handler queda con su propia dep.
import functools
def asignar(cmd, uow): return f"{cmd}->{uow}"
preparados = [functools.partial(asignar, uow=u) for u in ["UoW-A", "UoW-B"]]
print([p("x") for p in preparados])   # x->UoW-A, x->UoW-B (cada uno el suyo)
