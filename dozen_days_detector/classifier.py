from pathlib import Path
from typing import Dict

import networkx as nx


def classify_images(image_object_counts: Dict[Path, Dict[str, int]]) -> Dict[Path, int]:
    G = nx.Graph()
    G.add_nodes_from(image_object_counts.keys(), bipartite=0)
    G.add_nodes_from(range(1, 13), bipartite=1)
    edges = _extract_edges(image_object_counts)
    G.add_weighted_edges_from(edges)
    top_nodes = {n for n, d in G.nodes(data=True) if d['bipartite'] == 1}
    matching = nx.bipartite.maximum_matching(G, top_nodes=top_nodes)
    return {k: v for k, v in matching.items() if isinstance(k, str)}


def _extract_edges(image_object_counts):
    edges = list()
    for image_path, object_counts in image_object_counts.items():
        u = image_path
        counts = set(object_counts.values())
        for v in counts:
            if v <= 12:
                w = v
                edges.append((u, v, w))
    return edges
