"""
Assignment
Graphs are useful at LockedIn for more than just representing social connections! 
We'll also use it to build our geographic search feature. We have a graph of cities, where each city is a vertex, and each road connecting two cities is an edge.

Complete the breadth_first_search method on the Graph class.

This method traverses a graph level by level starting from a specified vertex v, and returns all vertices in the order they were visited. 
The breadth-first approach ensures we explore all vertices at the current distance from the start before moving further away.

1. Initialize tracking structures:
    - Create a list to track visited vertices
    - Create a list to use as a queue for vertices waiting to be explored
2. Begin the search:
    - Add the starting vertex v to the queue
3. Process the queue until empty:
    - Remove the first vertex from the queue and add it to the visited list
    - Get a sorted list of this vertex's neighbors
    - For each neighbor, if it is neither visited nor queued, add it to the queue
4. When complete, return the visited list containing vertices in the order they were discovered

(!) We're using unique strings now as our vertices, rather than integers
"""

class Graph:
    def breadth_first_search(self, v: str) -> list[str]:
        visited = []
        to_explore = [v]

        while to_explore:
            vertex = to_explore.pop(0)
            visited.append(vertex)

            for neighbor in sorted(self.graph[vertex]):
                if neighbor not in visited and neighbor not in to_explore:
                    to_explore.append(neighbor)
        
        return visited
            
    # don't touch below this line

    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u: str, v: str) -> None:
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self) -> str:
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
