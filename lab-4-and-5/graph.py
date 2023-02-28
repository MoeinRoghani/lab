from collections import deque
from matplotlib import pyplot as plt

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

    def get_size(self):
        return len(self.adj)

    def copy(self):
        copy = Graph(self.get_size())
        for node in self.adj:
            for edge in self.adj[node]:
                copy.add_edge(node, edge)
        return copy


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

# Breadth First Search Path
def BFS2(G, node1, node2):

    #FIFO QUEUE
    Q = deque([[node1]])

    #Marking Dictionary
    marked = {node1 : True}
    for node in G.adj: #Marks all of the nodes (populates marked dict)
        if node != node1:
            marked[node] = False

    #Main Code
    while len(Q) != 0:
        temp_path = Q.popleft()
        current_node = temp_path[len(temp_path)-1]
        if current_node == node2:
            return (temp_path)
        for node in G.adj[current_node]:
            if not marked[node]:
                new_path = temp_path + [node]
                Q.append(new_path)
                marked[node] = True
    return []

# Depth First Search Path
def DFS2(G, node1, node2):
    S = [[node1]]

    marked = {}
    for node in G.adj:
        marked[node] = False

    while len(S) != 0:
        temp_path = S.pop()
        current_node = temp_path[len(temp_path)-1]
        if not marked[current_node]:
            marked[current_node] = True

            for node in G.adj[current_node]:
                new_path = temp_path + [node]
                if node == node2:
                    return new_path
                S.append(new_path)
    return []

def DFS3(G,node1):
    S = [node1]
    pred = {}
    marked = {}
    for node in G.adj:
        marked[node] = False

    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True

            for node in G.adj[current_node]:
                if not marked[node]:
                    pred[node] = current_node
                S.append(node)
    return pred

def BFS3(G,node1):
    pred = {}
    Q = deque([node1])

    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                pred[node] = current_node
                Q.append(node)
                marked[node] = True
    return pred

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



#---------------------------------------------------------------Part 1---------------------------------------------------------------
# A functtion to randomly generate a graph with i node and j edges
def create_random_graph(i, j):

    # number of edges should always be smaller or equal to number of nodes
    if j > (i*(i-1)/2):
        raise Exception('The number of edges should always be smaller or equal to the a full graph with that number of nodes')

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

def has_cycle(g):
    out = g.adj
    for node in range(g.number_of_nodes()):
        out[node] = (g.adjacent_nodes(node)) 

    marked, stack = [], []
    for node in out:
        if node not in marked:
            stack.append((node, None))

            while stack:
                current, parent = stack.pop()

                if current in marked:
                    return True
                
                marked.append(current)

                for adjacent in out[current]:
                    if adjacent != parent: 
                        stack.append((adjacent, current))
    return False

def is_connected(G, node1, node2):
    S = [[node1]]

    marked = {}
    for node in G.adj:
        marked[node] = False

    while len(S) != 0:
        temp_path = S.pop()
        current_node = temp_path[len(temp_path)-1]
        if not marked[current_node]:
            marked[current_node] = True

            for node in G.adj[current_node]:
                new_path = temp_path + [node]
                if node == node2:
                    return True
                S.append(new_path)
    
    return False

#---------------------------------------------------------------Experiment 1---------------------------------------------------------------
numberOfNodes = list(range(50, 200, 50))
portionOfEdges = list(range(10, 105, 5))
 
cycles = []

for node in numberOfNodes:
    numberOfSamples = 30
    cycleHistory = []

    #maxEdges = node*(node-1)/2
    maxEdges = node

    numberOfEdges = list(int(maxEdges * p /100) for p in portionOfEdges)
    #portion
    for edges in numberOfEdges:
        temp = 0
        for i in range(numberOfSamples):
            if has_cycle(create_random_graph(node, edges)):
                temp += 1
        cycleHistory.append(temp/numberOfSamples)

    cycles.append(cycleHistory)

x0 = portionOfEdges
y0 = cycles[0]
plt.scatter(x0, y0)
plt.plot(x0, y0, color='r', label='50 Nodes')

x1 = portionOfEdges
y1 = cycles[1]
plt.scatter(x1, y1)
plt.plot(x1, y1, color='b', label='100 Nodes')

x2 = portionOfEdges
y2 = cycles[2]
plt.scatter(x2, y2)
plt.plot(x2, y2, color='g', label='150 Nodes')

plt.ylabel('Likelihood of our graph having a cycle', color='#1C2833')
plt.xlabel('Proportion of edges to number of nodes in percentage', color='#1C2833')
plt.legend()
plt.grid()
plt.show()


#---------------------------------------------------------------Experiment 2---------------------------------------------------------------
numberOfNodes = list(range(50, 200, 50))
portionOfEdges = list(range(10, 105, 2))
 
pathportion = []

for node in numberOfNodes:
    cycleHistory = []
    twocombinations = list(combinations(range(node), 2))
    maxEdges = node

    numberOfEdges = list(int(maxEdges * p /100) for p in portionOfEdges)
    #portion
    for edges in numberOfEdges:
        temp = 0
        graph = create_random_graph(node, edges)
        for combination in twocombinations:
            node1, node2 = combination
            if is_connected(graph, node1, node2):
                temp += 1

        cycleHistory.append(temp/node)

    pathportion.append(cycleHistory)

x0 = portionOfEdges
y0 = pathportion[0]
plt.scatter(x0, y0)
plt.plot(x0, y0, color='r', label='50 Nodes')

x1 = portionOfEdges
y1 = pathportion[1]
plt.scatter(x1, y1)
plt.plot(x1, y1, color='b', label='100 Nodes')

x2 = portionOfEdges
y2 = pathportion[2]
plt.scatter(x2, y2)
plt.plot(x2, y2, color='g', label='150 Nodes')

plt.ylabel('Portion of the connections to number of nodes', color='#1C2833')
plt.xlabel('Proportion of edges to number of nodes in percentage', color='#1C2833')
plt.legend()
plt.grid()
plt.show()

# -------------------------------------------------------------Approximations-------------------------------------------------------------

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


def has_no_edges(G):
    for node in G.adj:
        if G.adj[node]:
            return False
    return True


def approx1(G):
    C = []

    if has_no_edges(G):
        return C

    G2 = G.copy()
    while not is_vertex_cover(G, C):
        node = highest_degree_nodes(G2)
        C.append(node)
        remove_all_incident_edges(G2, node)
    return C


def approx2(G):
    G_copy = G.copy()
    C = set()

    if has_no_edges(G):
        return C

    while not is_vertex_cover(G_copy, C):
        vertex_list = list(G_copy.adj.keys())
        vertex = random.choice([x for x in vertex_list if x not in C])
        C.add(vertex)
    return C
        
        
def approx3(G):
    G_copy = G.copy()
    C = set()

    if has_no_edges(G):
        return C

    while not is_vertex_cover(G_copy, C):
        node1 = random.choice(list(G_copy.adj.keys()))
        if len(G_copy.adjacent_nodes(node1)) == 0:
            continue
        node2 = random.choice(G_copy.adjacent_nodes(node1))
        (u, v) = (node1, node2)

        C.add(u)
        C.add(v)

        remove_all_incident_edges(G_copy, u)
        remove_all_incident_edges(G_copy, v)

    return C


def approx_experiment():
    mvc_sum = {}
    approx1_sum = {}
    approx2_sum = {}
    approx3_sum = {}

    for m in range(1, 28, 5):
        random_graphs = [create_random_graph(8, m) for _ in range(1000)]

        mvc_sum[m] = sum([len(MVC(graph)) for graph in random_graphs])
        approx1_sum[m] = sum([len(approx1(graph)) for graph in random_graphs])
        approx2_sum[m] = sum([len(approx2(graph)) for graph in random_graphs])
        approx3_sum[m] = sum([len(approx3(graph)) for graph in random_graphs])

    approx1_expected_preformance = {m: approx1_sum[m]/mvc_sum[m] for m in mvc_sum}
    approx2_expected_preformance = {m: approx2_sum[m]/mvc_sum[m] for m in mvc_sum}
    approx3_expected_preformance = {m: approx3_sum[m]/mvc_sum[m] for m in mvc_sum}

    plt.plot(list(approx1_expected_preformance.keys()), list(approx1_expected_preformance.values()), label='Approximation 1')
    plt.plot(list(approx2_expected_preformance.keys()), list(approx2_expected_preformance.values()), label='Approximation 2')
    plt.plot(list(approx3_expected_preformance.keys()), list(approx3_expected_preformance.values()), label='Approximation 3')
    plt.legend()
    plt.xlabel('Number of edges')
    plt.ylabel('Expected performance')
    plt.title('Expected Preformance of Approximations vs Number of Edges')
    plt.show()

approx_experiment()

# -------------------------------------------------------------Independent Set Problem-------------------------------------------------------------

def is_independent_set(G,set):
    for node in range(len(set)-1):
        for node2 in range(len(set)):
            if G.are_connected(set[node], set[node2]):
                return False
    return True

def MIS(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    max_is = []
    for subset in subsets:
        if is_independent_set(G, subset):
            if len(subset) > len(max_is):
                max_is = subset
    return max_is
