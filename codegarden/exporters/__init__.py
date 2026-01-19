
# --- snippet: safe_join ---

# --- snippet: strip_yaml_frontmatter ---
def strip_yaml_frontmatter(text: str) -> str:
    """Убирает YAML фронтматтер из начала Markdown."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end+4:]
    return text
# --- endsnippet ---


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

def safe_join(base: str, *parts: str) -> str:
    """Простая защита от '..' в путях (демо)."""
    import os
    p = os.path.join(base, *parts)
    return os.path.normpath(p)
# --- endsnippet ---

# tweak 2025-10-31T10:54:03.379918
