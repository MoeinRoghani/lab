from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


#-------------------------------------------------------------Experiment 1-------------------------------------------------------------
import random
from itertools import combinations

# A functtion to randomly generate a graph with i node and j edges
def create_random_graph(i, j):
    # number of edges should always be smaller or equal to number of nodes
    if j > (i * (i - 1) / 2):
        raise Exception(
            'The number of edges should always be smaller or equal to the a full graph with that number of nodes')

    # making an empty dictionary for our graph
    graph = Graph(i)

    # Create a list of all possible edges between nodes
    edge_samples = list(combinations(range(i), 2))

    # randomly choosing j elements from the combinations
    edges = random.sample(edge_samples, j)

    # make our graph by adding the values
    for edge in edges:
        node1, node2 = edge
        graph.add_edge(node1, node2)

    return graph


def remove_all_incident_edges(G, node):
    for edge in G.adj[node]:
        G.adj[edge].remove(node)
    G.adj[node] = []


def highest_degree_nodes(G):
    keys = list(G.adj.keys())
    if not keys:
        return

    maximum = keys[0]
    for node in keys:
        if len(G.adj[node]) > len(G.adj[maximum]):
            maximum = node
    return maximum


def approx1(G):
    C = []
    G2 = G.copy()
    while not is_vertex_cover(G, C):
        node = highest_degree_nodes(G2)
        C.append(node)
        remove_all_incident_edges(G2, node)
    return C


def approx2(G):
    G_copy = G.copy()
    C = set()
    while not is_vertex_cover(G_copy, C):
        edge_list = list(G_copy.adj.keys())
        edge = random.choice([x for x in edge_list if x not in C])
        C.add(edge)
    return C
        
        
def approx3(G):
    G_copy = G.copy()
    C = set()
    while not is_vertex_cover(G_copy, C):
        node1 = random.choice(list(G_copy.adj.keys()))
        node2 = random.choice(G_copy.adj[node1])
        (u, v) = (node1, node2)
        remove_all_incident_edges(G_copy, u)
        remove_all_incident_edges(G_copy, v)
    return C
