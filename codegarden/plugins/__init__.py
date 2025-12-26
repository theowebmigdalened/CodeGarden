
# --- snippet: top_tags ---
def top_tags(index: dict, n: int = 10):
    """Топ N тегов по частоте."""
    from collections import Counter
    c = Counter()
    for meta in index.values():
        c.update(meta.get("tags", []))
    return c.most_common(n)
# --- endsnippet ---





# autosave 2025-11-21T14:15:19.466363

# autosave 2025-12-15T10:54:40.678339
# tweak 2025-12-26T15:41:53.295392
