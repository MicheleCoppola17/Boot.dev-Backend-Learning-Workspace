"""
Assignment
LockedIn, like all social networks, has a social graph: each user is a vertex, and each "friendship" (or in corpo-speak "connection") is an edge. 
We want to represent this graph as a matrix. 
Our users each have a unique ID, which is an integer that we'll use for their vertex number.

1. Complete the __init__ method.
    - Create a new data member called graph, it should be an empty list.
    - Fill the graph with n lists, where n is the number of vertices in the graph.
    - Each of these lists should contain n False values.
2. Complete the add_edge method.
    - It takes two vertices as inputs: u and v.
    - It adds an edge to the graph by setting the corresponding cells to True.
    - There are two cells in the matrix for each pair of vertices. For example, (2, 3) corresponds to these cells:

[
  [False, False, False, False, False],
  [False, False, False, False, False],
  [False, False, False, True, False],
  [False, False, True, False, False],
  [False, False, False, False, False]
]
"""

class Graph:
    graph: list[list[bool]]

    def __init__(self, num_vertices: int) -> None:
        self.graph = [
            [False for _ in range(num_vertices)] 
            for _ in range(num_vertices)
            ]


    def add_edge(self, u: int, v: int) -> None:
        self.graph[u][v] = True
        self.graph[v][u] = True
 
    # don't touch below this line

    def edge_exists(self, u: int, v: int) -> bool:
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
