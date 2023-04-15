from min_heap import MinHeap
from element import Element

# We are using MinHeap class in min_heap.py

def a_star(G, s, d, h):
    def reconstruct_path(predecessors, current_node):
        path = [current_node]
        while current_node in predecessors:
            current_node = predecessors[current_node]
            path.append(current_node)
        return path[::-1]

    open_set = MinHeap([Element(s, h[s])])
    closed_set = set()
    predecessors = {}
    g_score = {node: float('inf') for node in G}  # inf - floating point value representing positive infinity 
    g_score[s] = 0

    while not open_set.is_empty():
        current = open_set.extract_min().value
        if current == d:
            return (predecessors, reconstruct_path(predecessors, current))

        closed_set.add(current)
        for neighbor, weight in G[current].items():
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                if neighbor in open_set.map:
                    open_set.decrease_key(neighbor, f_score)
                else:
                    open_set.insert(Element(neighbor, f_score))
                predecessors[neighbor] = current

    return (predecessors, None)
