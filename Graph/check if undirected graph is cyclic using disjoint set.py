from collections import defaultdict
from DisjointSetData import Disjoint


class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n

    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)
        self.graph[end_vertex].append(starting_vertex)

    def isCyclic(self):
        disjoint = Disjoint(self.n)
        visited = [False] * self.n
        for u in list(self.graph):
            visited[u] = True
            for neighbour in self.graph[u]:
                if visited[neighbour] == False:
                    res = disjoint.union(u, neighbour)
                    if res == False:
                        return True
        return False


if __name__ == "__main__":
    g = Graph(6)

    g.addEdge(0, 5)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    # g.addEdge(4, 1)
    g.addEdge(3, 2)
    g.addEdge(3, 4)

    res = g.isCyclic()
    print(f"Graph is cyclic ? {res}")