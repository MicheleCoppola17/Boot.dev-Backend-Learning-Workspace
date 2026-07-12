"""
Assignment
Complete the unconnected_vertices(self) method. 
It should return a list of vertices (integers) that have no connections. 
A vertex with no edges will have an empty set as its value in the self.graph dictionary.
"""

class Graph:
    def unconnected_vertices(self) -> list[int]:
        unconnected = []
        for vertex in self.graph:
            if len(self.graph[vertex]) == 0:
                unconnected.append(vertex)

        return unconnected
    
    """
    Another way of implementing it:

    def unconnected_vertices(self) -> list[int]:
        return [v for v, edges in self.graph.items() if len(edges) == 0]
    """

    # don't touch below this line

    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u: int, v: int) -> None:
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u: int) -> None:
        if u not in self.graph:
            self.graph[u] = set()
