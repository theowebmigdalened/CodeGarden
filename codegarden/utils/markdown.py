import re

HEADING_RX = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)


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

def extract_headings(md_text: str):
    return [(m.group(1), m.group(2).strip()) for m in HEADING_RX.finditer(md_text or "")]
# tweak 2025-10-10T12:51:32.415950
