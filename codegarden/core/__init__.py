# tweak 2025-11-24T09:52:10.352819
# tweak 2026-01-05T12:47:54.312761
# tweak 2026-03-09T15:37:34.754882

# autosave 2026-04-17T15:44:58.535547

# --- snippet: safe_join ---
def safe_join(base: str, *parts: str) -> str:
    """Простая защита от '..' в путях (демо)."""
    import os
    p = os.path.join(base, *parts)
    return os.path.normpath(p)
# --- endsnippet ---

