import os
import re
import json
from typing import List, Dict, Optional

ROOT = os.path.dirname(os.path.dirname(__file__))
NOTES_DIR = os.path.join(os.path.dirname(ROOT), "notes")
META_DIR = os.path.join(os.path.dirname(ROOT), "data", "meta")

LINK_RX = re.compile(r"\[\[([^\[\]]+)\]\]")  # [[Note Title]]
TAG_RX = re.compile(r"(?<!\w)#([a-zA-Z0-9_\-]+)")

def ensure_dirs():
    os.makedirs(NOTES_DIR, exist_ok=True)
    os.makedirs(META_DIR, exist_ok=True)

def list_notes() -> List[str]:
    ensure_dirs()
    return sorted([f for f in os.listdir(NOTES_DIR) if f.endswith(".md")])

def read_note(filename: str) -> Optional[str]:
    path = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(path):
        return None
    return open(path, "r", encoding="utf-8").read()

def write_note(title: str, content: str) -> str:
    """
    Создаёт/перезаписывает заметку. Имя файла — слаг из title.
    """
    ensure_dirs()
    slug = slugify(title) + ".md"
    path = os.path.join(NOTES_DIR, slug)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{content.strip()}\n")
    return path


# --- snippet: normalize_title ---
def normalize_title(title: str) -> str:
    """Базовая нормализация заголовка заметки."""
    return " ".join(title.strip().split())
# --- endsnippet ---

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\-_]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "note"

def extract_links_and_tags(text: str) -> Dict[str, List[str]]:
    links = LINK_RX.findall(text or "")
    tags = TAG_RX.findall(text or "")
    return {"links": list(sorted(set(links))), "tags": list(sorted(set(tags)))}


# --- snippet: top_tags ---
def top_tags(index: dict, n: int = 10):
    """Топ N тегов по частоте."""
    from collections import Counter
    c = Counter()
    for meta in index.values():
        c.update(meta.get("tags", []))
    return c.most_common(n)
# --- endsnippet ---

def index_notes() -> str:
    """
    Пробегает по всем заметкам, извлекает ссылки/теги, пишет индекс в data/meta/index.json
    """
    ensure_dirs()
    idx = {}
    for fname in list_notes():
        body = read_note(fname) or ""
        meta = extract_links_and_tags(body)
        idx[fname] = meta
    out = os.path.join(META_DIR, "index.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)
    return out
# tweak 2025-10-07T11:55:40.392075
