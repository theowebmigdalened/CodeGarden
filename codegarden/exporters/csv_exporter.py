import os, csv, json
from ..graph.build import load_index

ROOT = os.path.dirname(os.path.dirname(__file__))
REPORTS_DIR = os.path.join(os.path.dirname(ROOT), "reports")

def export_tags_csv() -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    idx = load_index()
    path = os.path.join(REPORTS_DIR, "tags.csv")
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["file", "tags"])
        for fn, meta in idx.items():
            tags = ",".join(meta.get("tags", []))
            w.writerow([fn, tags])
    return path
