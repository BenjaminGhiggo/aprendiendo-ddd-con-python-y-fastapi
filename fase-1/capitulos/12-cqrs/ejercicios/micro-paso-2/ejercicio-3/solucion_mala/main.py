# MALA: SELECT N+1. Una consulta por los ids y LUEGO una consulta por cada item.
def query(sql):
    print("  SQL:", sql)
    return {"ids": [1, 2, 3]} if "ids" in sql else {"detalle": "x"}
ids = query("SELECT ids FROM lotes")["ids"]
for i in ids:                                   # N consultas extra (1 por id)
    query(f"SELECT * FROM lotes WHERE id={i}")
print("mala -> consultas:", 1 + len(ids))
