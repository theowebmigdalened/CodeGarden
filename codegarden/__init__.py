from .core.notes import write_note, read_note, list_notes, index_notes
from .graph.build import build_graph
from .graph.metrics import out_degree, in_degree, top_nodes_by_degree
from .exporters.json_exporter import export_all_to_json
from .exporters.csv_exporter import export_tags_csv

__all__ = [
    "write_note", "read_note", "list_notes", "index_notes",
    "build_graph", "out_degree", "in_degree", "top_nodes_by_degree",
    "export_all_to_json", "export_tags_csv"
]

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

# tweak 2025-11-10T18:37:33.310853
