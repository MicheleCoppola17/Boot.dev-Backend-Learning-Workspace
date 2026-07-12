"""
Assignment
Let's rebuild our Graph class using an adjacency list.

1. Complete the constructor:
    - It should create an empty dictionary called graph as a data member.
2. Complete the add_edge method. It takes two vertices as inputs, and adds an edge to the adjacency list (the dictionary):
    - Be sure to map both vertices to each other, it's a bidirectional edge.
    - Handle the case where a set for a vertex doesn't exist yet.
    - The resulting graph maps vertices to a set of all other vertices they share an edge with. For example:

result = {
    0: {1, 4},
    1: {0, 2, 3, 4},
    2: {1, 3},
    3: {1, 2, 4},
    4: {0, 1, 3}
}
"""

class Graph:
    graph: dict[int, set[int]]

    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u: int, v: int) -> None:
        if u not in self.graph:
            self.graph[u] = set()
        self.graph[u].add(v)

        if v not in self.graph:
            self.graph[v] = set()
        self.graph[v].add(u)

    # don't touch below this line

    def edge_exists(self, u: int, v: int) -> bool:
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
