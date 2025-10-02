"""
Пример плагина: добавляет поле 'word_count' в index.json (в meta-стадии).
Реально плагин просто читает все заметки и считает слова.
"""
import os, json, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
NOTES_DIR = os.path.join(os.path.dirname(ROOT), "notes")
META_DIR = os.path.join(os.path.dirname(ROOT), "data", "meta")

def run():
    idx_path = os.path.join(META_DIR, "index.json")
    if not os.path.exists(idx_path):
        return False, "index.json not found"
    idx = json.load(open(idx_path, "r", encoding="utf-8"))
    for fn in idx:
        full = os.path.join(NOTES_DIR, fn)
        if not os.path.exists(full):
            continue
        text = open(full, "r", encoding="utf-8").read()
        words = re.findall(r"\w+", text, flags=re.UNICODE)
        # дописываем динамический атрибут
        meta = idx.get(fn) or {}
        meta["word_count"] = len(words)
        idx[fn] = meta
    json.dump(idx, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return True, "plugin: word_count updated"
