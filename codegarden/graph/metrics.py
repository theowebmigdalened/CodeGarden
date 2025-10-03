from typing import Dict, List, Tuple

def out_degree(graph: Dict[str, List[str]]) -> Dict[str, int]:
    return {k: len(v) for k, v in graph.items()}

def in_degree(graph: Dict[str, List[str]]) -> Dict[str, int]:
    incoming = {k: 0 for k in graph.keys()}
    for k, neigh in graph.items():
        for t in neigh:
            if t in incoming:
                incoming[t] += 1
    return incoming

def top_nodes_by_degree(graph: Dict[str, List[str]], n: int = 5) -> List[Tuple[str, int]]:
    deg = {k: len(v) for k, v in graph.items()}
    return sorted(deg.items(), key=lambda x: -x[1])[:n]



