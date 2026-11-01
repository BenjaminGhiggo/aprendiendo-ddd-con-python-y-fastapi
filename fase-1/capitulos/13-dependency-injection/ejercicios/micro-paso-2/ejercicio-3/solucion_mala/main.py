# MALA: para testear sin enviar de verdad, monkeypatch de la funcion global. Fragil y acoplado.
def email_send(mensaje): raise RuntimeError("no enviar en test!")
def avisar(sku): email_send(f"sin stock {sku}")
# "parche" manual (como mock.patch): reemplazamos la global
import sys
_orig = email_send
globals()["email_send"] = lambda m: capturado.append(m)
capturado = []
avisar("MESA")
globals()["email_send"] = _orig
print("mala -> capturado por parche:", capturado)
