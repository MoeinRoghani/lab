import SPAlgorithm
from HeuristicGraph import HeuristicGraph
from min_heap import MinHeap

class A_Star(SPAlgorithm):
    def __init__(self,):
        self.__G = HeuristicGraph()

    def __graphToHeuristic(self,graph):
        self.__G = HeuristicGraph()
        for node1 in list(graph.adj.keys()):
            self.__G.add_node(node1)
            for node2 in graph.adj[node1]:
                weight = graph.w(node1, node2)
                self.__G.add_edge(node1, node2, weight)
        return

    def calc_sp(self, graph, s, d):
        self.__graphToHeuristic(graph)
        h = self.__G.get_heuristic(d)

        def reconstruct_path(predecessors, current_node):
            path = [current_node]
            while current_node in predecessors:
                current_node = predecessors[current_node]
                path.append(current_node)
            return path[::-1]

        nodes = list(self.__G.adj.keys())

        open_set = MinHeap([self.Element(s, h[s])])
        closed_set = set()
        predecessors = {}
        g_score = {node: float('inf') for node in
                   nodes}  # inf - floating point value representing positive infinity
        g_score[s] = 0

        while not open_set.is_empty():
            current = open_set.extract_min().value
            if current == d:
                return (predecessors[d]) #return (predecessors, reconstruct_path(predecessors, current))

            closed_set.add(current)
            for neighbor in self.__G.adjacent_nodes(current):
                weight = self.__G.w(current, neighbor)
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + h[neighbor]
                    if neighbor in open_set.map:
                        open_set.decrease_key(neighbor, f_score)
                    else:
                        open_set.insert(self.Element(neighbor, f_score))
                    predecessors[neighbor] = current

        return (predecessors[d]) #return (predecessors, None)

    # we use this to represent each element in min heap and read values from it
    class Element:
        def __init__(self, value, key):
            self.value = value
            self.key = key

        def __str__(self):
            return "(" + str(self.value) + "," + str(self.key) + ")"