
# --- snippet: top_tags ---
def top_tags(index: dict, n: int = 10):
    """Топ N тегов по частоте."""
    from collections import Counter
    c = Counter()
    for meta in index.values():
        c.update(meta.get("tags", []))
    return c.most_common(n)
# --- endsnippet ---


# --- snippet: strip_yaml_frontmatter ---
def strip_yaml_frontmatter(text: str) -> str:
    """Убирает YAML фронтматтер из начала Markdown."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end+4:]
    return text
# --- endsnippet ---


# autosave 2025-11-21T14:15:19.466363
