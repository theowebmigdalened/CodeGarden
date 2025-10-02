import os, json
from typing import Dict, List
from ..graph.build import build_graph, load_index

ROOT = os.path.dirname(os.path.dirname(__file__))
REPORTS_DIR = os.path.join(os.path.dirname(ROOT), "reports")

def export_all_to_json() -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    idx = load_index()
    g = build_graph()
    out = {
        "index": idx,
        "graph": g
    }
    path = os.path.join(REPORTS_DIR, "export.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return path
