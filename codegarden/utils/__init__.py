
# autosave 2025-10-17T17:02:10.401611
# tweak 2025-10-24T13:42:31.420416

# autosave 2025-12-19T18:44:13.497906
# tweak 2026-01-19T10:20:53.146164

# --- snippet: top_tags ---
def top_tags(index: dict, n: int = 10):
    """Топ N тегов по частоте."""
    from collections import Counter
    c = Counter()
    for meta in index.values():
        c.update(meta.get("tags", []))
    return c.most_common(n)
# --- endsnippet ---

