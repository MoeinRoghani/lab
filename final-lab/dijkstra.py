from final_project_part1 import DirectedWeightedGraph
import min_heap

# def dijkstra(graph, start, end):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#     unvisited = {node for node in graph}
#     previous_nodes = {node: None for node in graph}
#
#     current_node = start
#     while current_node != end:
#         current_distance = distances[current_node]
#         for neighbor, weight in graph[current_node].items():
#             new_distance = current_distance + weight
#             if new_distance < distances[neighbor]:
#                 distances[neighbor] = new_distance
#                 previous_nodes[neighbor] = current_node
#
#         unvisited.remove(current_node)
#         candidates = {node: distances[node] for node in unvisited}
#         current_node = min(candidates, key=candidates.get)
#
#     path = []
#     while previous_nodes[current_node] is not None:
#         path.append(current_node)
#         current_node = previous_nodes[current_node]
#     path.append(start)
#     path = path[::-1]
#
#     return previous_nodes, distances[end]

def dijkstra(G, source, dest):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
        if current_node == dest:
            return dist[dest]
    return dist[dest]