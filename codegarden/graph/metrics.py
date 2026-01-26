from typing import Dict, List, Tuple

def out_degree(graph: Dict[str, List[str]]) -> Dict[str, int]:
    return {k: len(v) for k, v in graph.items()}


# --- snippet: normalize_title ---
def normalize_title(title: str) -> str:
    """Базовая нормализация заголовка заметки."""
    return " ".join(title.strip().split())
# --- endsnippet ---

def in_degree(graph: Dict[str, List[str]]) -> Dict[str, int]:
    incoming = {k: 0 for k in graph.keys()}
    for k, neigh in graph.items():
        for t in neigh:
            if t in incoming:
                incoming[t] += 1
    return incoming


# --- snippet: strip_yaml_frontmatter ---
def strip_yaml_frontmatter(text: str) -> str:
    """Убирает YAML фронтматтер из начала Markdown."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end+4:]
    return text
# --- endsnippet ---

def top_nodes_by_degree(graph: Dict[str, List[str]], n: int = 5) -> List[Tuple[str, int]]:
    deg = {k: len(v) for k, v in graph.items()}
    return sorted(deg.items(), key=lambda x: -x[1])[:n]



# tweak 2025-10-17T14:48:00.375937
# tweak 2026-01-12T10:42:37.751144
# tweak 2026-01-16T10:15:37.512096
# tweak 2026-01-26T09:46:05.905163
