
# --- snippet: safe_join ---
def safe_join(base: str, *parts: str) -> str:
    """Простая защита от '..' в путях (демо)."""
    import os
    p = os.path.join(base, *parts)
    return os.path.normpath(p)
# --- endsnippet ---

