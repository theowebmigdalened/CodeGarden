import os, csv, json
from ..graph.build import load_index

ROOT = os.path.dirname(os.path.dirname(__file__))
REPORTS_DIR = os.path.join(os.path.dirname(ROOT), "reports")

def export_tags_csv() -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    idx = load_index()
    path = os.path.join(REPORTS_DIR, "tags.csv")
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file", "tags"])
        for fn, meta in idx.items():
            tags = ",".join(meta.get("tags", []))
            w.writerow([fn, tags])
    return path

# autosave 2025-12-26T14:26:41.652257

# autosave 2026-01-16T18:36:35.374958

# --- snippet: normalize_title ---

# --- snippet: guess_language ---
def guess_language(text: str) -> str:
    """Супер-простая евристика языка по символам."""
    import re
    cyr = len(re.findall(r"[А-Яа-яЁё]", text))
    lat = len(re.findall(r"[A-Za-z]", text))
    if cyr > lat: return "ru"
    if lat > cyr: return "en"
    return "unknown"
# --- endsnippet ---

def normalize_title(title: str) -> str:
    """Базовая нормализация заголовка заметки."""
    return " ".join(title.strip().split())
# --- endsnippet ---




