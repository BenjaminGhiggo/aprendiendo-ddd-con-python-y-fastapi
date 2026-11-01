from pathlib import Path
from sincronizador import determinar_acciones


def test_cuando_un_archivo_existe_en_origen_pero_no_en_destino():
    origen = {"hash1": "fn1"}
    destino = {}
    acciones = list(determinar_acciones(origen, destino, "/origen", "/destino"))
    assert acciones == [("COPIAR", Path("/origen/fn1"), Path("/destino/fn1"))]


def test_cuando_un_archivo_fue_renombrado_en_origen():
    origen = {"hash1": "fn1"}
    destino = {"hash1": "fn2"}
    acciones = list(determinar_acciones(origen, destino, "/origen", "/destino"))
    assert acciones == [("MOVER", Path("/destino/fn2"), Path("/destino/fn1"))]


def test_cuando_un_archivo_sobra_en_destino():
    origen = {}
    destino = {"hash1": "fn1"}
    acciones = list(determinar_acciones(origen, destino, "/origen", "/destino"))
    assert acciones == [("BORRAR", Path("/destino/fn1"))]


# --- Tests edge-to-edge (con carpetas reales temporales) ---
from sincronizador import sincronizar


def test_sincroniza_un_archivo_nuevo(tmp_path):
    origen = tmp_path / "origen"
    destino = tmp_path / "destino"
    origen.mkdir()
    destino.mkdir()
    (origen / "mi-archivo").write_text("contenido")
    sincronizar(origen, destino)
    assert (destino / "mi-archivo").read_text() == "contenido"


def test_borra_un_archivo_que_sobra_en_destino(tmp_path):
    origen = tmp_path / "origen"
    destino = tmp_path / "destino"
    origen.mkdir()
    destino.mkdir()
    (destino / "sobra").write_text("x")
    sincronizar(origen, destino)
    assert not (destino / "sobra").exists()
