import os, json
from typing import Dict, List, Tuple

ROOT = os.path.dirname(os.path.dirname(__file__))
META_DIR = os.path.join(os.path.dirname(ROOT), "data", "meta")

def load_index() -> Dict[str, dict]:
    path = os.path.join(META_DIR, "index.json")
    if not os.path.exists(path):
        return {}
    return json.load(open(path, "r", encoding="utf-8"))

def build_graph() -> Dict[str, List[str]]:
    """
    Строит directed-граф: файл -> список файлов, на которые он ссылается (по [[Title]]).
    """
    idx = load_index()
    # сопоставление названия заметки (из заголовка файла) к имени файла
    title2file = {strip_ext(fn): fn for fn in idx.keys()}
    g: Dict[str, List[str]] = {fn: [] for fn in idx.keys()}
    for fn, meta in idx.items():
        for link_title in meta.get("links", []):
            target = title2file.get(slugify(link_title) + ".md")
            if target and target != fn and target in g:
                g[fn].append(target)
    return g

def strip_ext(fn: str) -> str:
    return slugify(fn.rsplit(".", 1)[0])

def slugify(s: str) -> str:
    import re
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\-_]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s

# autosave 2025-10-05T18:29:29.544381

# autosave 2025-10-27T10:03:52.537678

# autosave 2025-12-05T18:04:44.496119
# tweak 2026-01-02T14:23:58.485841
