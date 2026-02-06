import re

HEADING_RX = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)




def extract_headings(md_text: str):
    return [(m.group(1), m.group(2).strip()) for m in HEADING_RX.finditer(md_text or "")]
# tweak 2025-10-10T12:51:32.415950

# autosave 2025-12-22T19:58:09.373780
# tweak 2026-02-06T14:43:31.356917
