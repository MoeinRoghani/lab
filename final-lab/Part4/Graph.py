from abc import ABC, abstractmethod

class Graph(ABC):
    @abstractmethod
    def get_adj_nodes(self, node: int) -> [int]:
        pass

    @abstractmethod
    def add_node(self, node: int) -> None:
        pass

    @abstractmethod
    def add_edge(self, start: int, end: int, w: str) -> None:
        pass

    @abstractmethod
    def get_num_of_nodes(self) -> int:
        pass

    @abstractmethod
    def w(self, node: int) -> float:
        pass




