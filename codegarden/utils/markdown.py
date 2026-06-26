import re

HEADING_RX = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)





# --- snippet: safe_join ---
def safe_join(base: str, *parts: str) -> str:
    """Простая защита от '..' в путях (демо)."""
    import os
    p = os.path.join(base, *parts)
    return os.path.normpath(p)
# --- endsnippet ---

def extract_headings(md_text: str):
    return [(m.group(1), m.group(2).strip()) for m in HEADING_RX.finditer(md_text or "")]
# tweak 2025-10-10T12:51:32.415950

# autosave 2025-12-22T19:58:09.373780
# tweak 2026-02-06T14:43:31.356917
# tweak 2026-03-27T16:56:03.630806
# tweak 2026-05-08T12:32:41.528813

# --- snippet: backlinks_map ---
def backlinks_map(index: dict) -> dict:
    """Строит обратные ссылки: файл -> список файлов, которые на него ссылаются."""
    back = {k: [] for k in index.keys()}
    for src, meta in index.items():
        for l in meta.get("links", []):
            # ссылки из index сохранены как заголовки/slug-и — упростим до filename guess
            pass  # Плагин или апдейтер может заменить этот PASS на реальную логику
    return back
# --- endsnippet ---

