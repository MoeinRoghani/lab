def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = {node for node in graph}
    previous_nodes = {node: None for node in graph}

    current_node = start
    while current_node != end:
        current_distance = distances[current_node]
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

        unvisited.remove(current_node)
        candidates = {node: distances[node] for node in unvisited}
        current_node = min(candidates, key=candidates.get)

    path = []
    while previous_nodes[current_node] is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.append(start)
    path = path[::-1]

    return previous_nodes, distances[end]
