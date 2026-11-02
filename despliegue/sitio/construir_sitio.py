"""construir_sitio.py — arma el sitio de estudio (MkDocs Material) a partir del repo.

No modifica ningún archivo del repo: copia el material a build/sitio_src/, lo adapta para
la web y genera build/mkdocs.yml. Después se construye con:

    uv run --group docs python despliegue/sitio/construir_sitio.py
    uv run --group docs mkdocs build -f build/mkdocs.yml        # -> site/

Adaptaciones (los README están escritos para GitHub):
  1. README.md  -> index.md (página principal de su carpeta).
  2. Cada .py   -> una página <archivo>.py.md con el código resaltado (se lee en el navegador).
  3. Carpetas sin README (paso5_solucionario/, paso6_ejercicios/...) -> index.md con su contenido.
  4. Links a carpetas -> a su index.md; links a .py -> a su página; links a docs/fuente -> al
     libro oficial gratuito (no publicamos la copia OCR del libro: licencia CC BY-NC-ND).
  5. <details> -> <details markdown="1"> para que las tablas de las claves se vean.
  6. Menú lateral en ORDEN DE ESTUDIO (Fase 0: lecciones 00-17; Fase 1: capítulos 01-13).
"""
import os
import re
import shutil

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BUILD = os.path.join(REPO, "build")
SRC = os.path.join(BUILD, "sitio_src")
LIBRO = "https://www.cosmicpython.com/book/preface.html"

# Qué se publica (relativo al repo). CLAUDE.md (instrucciones del asistente) y docs/ (el libro) no.
ARCHIVOS_RAIZ = ["README.md", "COMO-ESTUDIAR.md", "METODOLOGIA.md"]
CARPETAS = ["lecciones", "fase-1", "progreso"]
IGNORAR = {"__pycache__", ".pytest_cache", "node_modules", ".venv", ".ruff_cache"}
TEXTO = {".py": "python", ".toml": "toml", ".txt": "text", ".mmd": "text", ".ini": "ini", ".cfg": "ini"}
IMAGENES = {".png", ".jpg", ".jpeg", ".svg", ".gif"}


def destino(rel):
    """Ruta dentro de SRC para un archivo del repo (README.md -> index.md)."""
    base, nombre = os.path.split(rel)
    if nombre == "README.md":
        nombre = "index.md"
    return os.path.join(base, nombre)


def recolectar():
    """Lista de archivos del repo a publicar (rutas relativas)."""
    out = [f for f in ARCHIVOS_RAIZ if os.path.exists(os.path.join(REPO, f))]
    for c in CARPETAS:
        for root, dirs, files in os.walk(os.path.join(REPO, c)):
            dirs[:] = sorted(d for d in dirs if d not in IGNORAR)
            for f in sorted(files):
                ext = os.path.splitext(f)[1]
                if f.endswith(".md") or ext in TEXTO or ext in IMAGENES:
                    out.append(os.path.relpath(os.path.join(root, f), REPO))
    return out


PUBLICADOS = set()


def reescribir_link(link, rel_md):
    """Convierte un link relativo de un .md del repo a su equivalente en el sitio."""
    if re.match(r"^[a-z]+:", link) or link.startswith("#") or link.startswith("/"):
        return link
    ruta, _, ancla = link.partition("#")
    ancla = "#" + ancla if ancla else ""
    carpeta_md = os.path.dirname(rel_md)
    objetivo = os.path.normpath(os.path.join(carpeta_md, ruta))   # relativo al repo
    if objetivo.startswith("docs" + os.sep) or objetivo == "docs":
        return LIBRO
    abs_obj = os.path.join(REPO, objetivo)
    if os.path.isdir(abs_obj):
        nuevo = os.path.join(objetivo, "index.md")
    elif objetivo.endswith("README.md"):
        nuevo = destino(objetivo)
    elif os.path.splitext(objetivo)[1] in TEXTO:
        nuevo = objetivo + ".md"
    else:
        nuevo = objetivo
    return os.path.relpath(nuevo, carpeta_md).replace(os.sep, "/") + ancla


def adaptar_md(texto, rel_md):
    # Protege los bloques de código (no se tocan links dentro de código).
    trozos = re.split(r"(```.*?```)", texto, flags=re.S)
    for i in range(0, len(trozos), 2):
        t = trozos[i]
        partes = re.split(r"(`[^`\n]*`)", t)
        for j in range(0, len(partes), 2):
            partes[j] = re.sub(
                r"(\]\()([^)\s]+)(\))",
                lambda m: m.group(1) + reescribir_link(m.group(2), rel_md) + m.group(3),
                partes[j],
            )
            partes[j] = re.sub(r"<details>", '<details markdown="1">', partes[j])
        trozos[i] = "".join(partes)
    return "".join(trozos)


def pagina_codigo(rel):
    lenguaje = TEXTO[os.path.splitext(rel)[1]]
    codigo = open(os.path.join(REPO, rel), encoding="utf-8").read()
    carpeta = os.path.dirname(rel)
    volver = os.path.relpath(os.path.join(carpeta, "index.md"), carpeta).replace(os.sep, "/")
    return (
        f"# `{os.path.basename(rel)}`\n\n"
        f"> 📂 `{rel}` · [⬆️ volver a la carpeta]({volver})\n>\n"
        f"> Para ejecutarlo, desde la raíz del repo: `uv run python {rel}`\n\n"
        f"```{lenguaje}\n{codigo.rstrip()}\n```\n"
    )


def titulo_de(rel_md):
    try:
        for linea in open(os.path.join(REPO, rel_md), encoding="utf-8"):
            if linea.startswith("# "):
                return linea[2:].strip().replace("`", "")   # sin backticks: el menú no los formatea
    except FileNotFoundError:
        pass
    return os.path.basename(os.path.dirname(rel_md)) or rel_md


def indice_carpeta(rel_dir):
    """index.md para una carpeta sin README: lista su contenido."""
    abs_dir = os.path.join(REPO, rel_dir)
    lineas = [f"# 📂 `{rel_dir}/`\n", "[⬆️ subir un nivel](../index.md)\n"]
    subdirs = sorted(d for d in os.listdir(abs_dir) if os.path.isdir(os.path.join(abs_dir, d)) and d not in IGNORAR)
    archivos = sorted(f for f in os.listdir(abs_dir) if os.path.isfile(os.path.join(abs_dir, f)))
    if subdirs:
        lineas.append("\n**Carpetas**\n")
        for d in subdirs:
            readme = os.path.join(rel_dir, d, "README.md")
            extra = f" — {titulo_de(readme)}" if os.path.exists(os.path.join(REPO, readme)) else ""
            lineas.append(f"- [📁 {d}/]({d}/index.md){extra}")
    if archivos:
        lineas.append("\n**Archivos**\n")
        for f in archivos:
            ext = os.path.splitext(f)[1]
            if ext in TEXTO:
                lineas.append(f"- [📄 {f}]({f}.md)")
            elif f.endswith(".md"):
                lineas.append(f"- [📄 {f}]({destino(f)})")
    return "\n".join(lineas) + "\n"


def nav():
    def entradas(carpeta):
        out = []
        for d in sorted(os.listdir(os.path.join(REPO, carpeta))):
            readme = os.path.join(carpeta, d, "README.md")
            if os.path.isdir(os.path.join(REPO, carpeta, d)) and os.path.exists(os.path.join(REPO, readme)):
                out.append({titulo_de(readme): destino(readme)})
        return out
    progreso = [{"Índice de progreso": "progreso/index.md"}]
    for f in sorted(os.listdir(os.path.join(REPO, "progreso"))):
        if f.endswith(".md") and f != "README.md":
            progreso.append({titulo_de(os.path.join("progreso", f)): f"progreso/{f}"})
    return [
        {"▶ Empieza aquí": "index.md"},
        {"📖 Cómo estudiar": "COMO-ESTUDIAR.md"},
        {"Fase 0 · Python, POO y SOLID": [{"Índice de lecciones": "lecciones/index.md"}] + entradas("lecciones")},
        {"Fase 1 · El libro": [{"Índice de capítulos": "fase-1/capitulos/index.md"}] + entradas("fase-1/capitulos")},
        {"✅ Progreso": progreso},
        {"Metodología": "METODOLOGIA.md"},
    ]


def yaml_nav(items, nivel=1):
    """Serializa el nav a YAML a mano (sin depender de PyYAML)."""
    out = []
    pad = "  " * nivel
    for item in items:
        (k, v), = item.items()
        k = '"' + k.replace("\\", "\\\\").replace('"', '\\"') + '"'
        if isinstance(v, list):
            out.append(f"{pad}- {k}:")
            out.extend(yaml_nav(v, nivel + 1))
        else:
            out.append(f"{pad}- {k}: {v}")
    return out


MKDOCS = """site_name: Aprendiendo DDD con Python y FastAPI
site_description: Aprendizaje guiado desde cero en Python hasta los patrones de Cosmic Python
docs_dir: sitio_src
site_dir: ../site
use_directory_urls: true
theme:
  name: material
  language: es
  features:
    - navigation.sections
    - navigation.top
    - navigation.indexes
    - search.highlight
    - search.suggest
    - content.code.copy
    - toc.follow
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      toggle: {icon: material/weather-night, name: Modo oscuro}
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      toggle: {icon: material/weather-sunny, name: Modo claro}
plugins:
  - search:
      lang: es
markdown_extensions:
  - tables
  - attr_list
  - md_in_html
  - admonition
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
validation:
  links:
    not_found: warn
    unrecognized_links: warn
nav:
"""


def main():
    if os.path.exists(BUILD):
        shutil.rmtree(BUILD)
    os.makedirs(SRC)
    archivos = recolectar()
    carpetas_con_index = set()
    for rel in archivos:
        if os.path.basename(rel) == "README.md":
            carpetas_con_index.add(os.path.dirname(rel))
    n_md = n_cod = n_img = n_idx = 0
    for rel in archivos:
        ext = os.path.splitext(rel)[1]
        if rel.endswith(".md"):
            dst = os.path.join(SRC, destino(rel))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            txt = open(os.path.join(REPO, rel), encoding="utf-8").read()
            open(dst, "w", encoding="utf-8").write(adaptar_md(txt, rel))
            n_md += 1
        elif ext in TEXTO:
            dst = os.path.join(SRC, rel + ".md")
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            open(dst, "w", encoding="utf-8").write(pagina_codigo(rel))
            n_cod += 1
        else:
            dst = os.path.join(SRC, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(os.path.join(REPO, rel), dst)
            n_img += 1
    # índices para carpetas publicadas que no tienen README
    for c in CARPETAS:
        for root, dirs, _ in os.walk(os.path.join(REPO, c)):
            dirs[:] = [d for d in dirs if d not in IGNORAR]
            rel_dir = os.path.relpath(root, REPO)
            if rel_dir not in carpetas_con_index:
                open(os.path.join(SRC, rel_dir, "index.md"), "w", encoding="utf-8").write(indice_carpeta(rel_dir))
                n_idx += 1
    # robots.txt: el sitio es público pero no queremos que lo indexen los buscadores
    open(os.path.join(SRC, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    open(os.path.join(BUILD, "mkdocs.yml"), "w", encoding="utf-8").write(MKDOCS + "\n".join(yaml_nav(nav(), 1)) + "\n")
    print(f"sitio_src listo: {n_md} páginas .md, {n_cod} páginas de código, {n_img} imágenes, {n_idx} índices de carpeta")


if __name__ == "__main__":
    main()
