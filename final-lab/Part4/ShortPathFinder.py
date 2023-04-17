import Graph
import SPAlgorithm


class ShortPathFinder():
    def __init__(self):
        self.__graph = None
        self.__algorithm = None

    def set_graph(self, graph: Graph):
        self.__graph = graph
        return

    def set_algorithm(self, algorithm: SPAlgorithm):
        self.__algorithm = algorithm
        return

    def calc_short_path(self, source: int, dest: int) -> float:
        return self.__algorithm.calc_sp(self.__graph, source, dest)
