
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

