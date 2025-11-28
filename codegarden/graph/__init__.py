
# --- snippet: backlinks_map ---

# --- snippet: normalize_title ---
def normalize_title(title: str) -> str:
    """Базовая нормализация заголовка заметки."""
    return " ".join(title.strip().split())
# --- endsnippet ---

def backlinks_map(index: dict) -> dict:
    """Строит обратные ссылки: файл -> список файлов, которые на него ссылаются."""
    back = {k: [] for k in index.keys()}
    for src, meta in index.items():
        for l in meta.get("links", []):
            # ссылки из index сохранены как заголовки/slug-и — упростим до filename guess
            pass  # Плагин или апдейтер может заменить этот PASS на реальную логику
    return back
# --- endsnippet ---


# --- snippet: top_tags ---
def top_tags(index: dict, n: int = 10):
    """Топ N тегов по частоте."""
    from collections import Counter
    c = Counter()
    for meta in index.values():
        c.update(meta.get("tags", []))
    return c.most_common(n)
# --- endsnippet ---

