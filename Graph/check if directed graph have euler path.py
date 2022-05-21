from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, u, visited):
        visited.add(u)
        countVisited = 1

        for v in self.graph[u]:
            if v not in visited:
                countVisited += self.dfs(v, visited)

        return countVisited

    def is_connected(self):
        totalComponents = 0
        countIsolatedVertices = 0
        visited = set()

        for u in self.graph:
            if u not in visited:
                if self.dfs(u, visited) == 1:
                    countIsolatedVertices += 1
                totalComponents += 1

        # isolated vetices allowed but more than 1 component where edges exist can be not allowed
        if totalComponents-countIsolatedVertices == 1:
            return True
        else:
            return False
    
    def find_euler_path(self):
        if not self.is_connected():
            print("Graph is not connected")
            return
        
        inDegree = defaultdict(int)
        outDegree = defaultdict(int)
        for u in self.graph:
            for v in self.graph[u]:
                inDegree[v] += 1
                outDegree[u] += 1
        
        # to check if directed graph has euler path
        # at most one vertex has outDegree-inDegree = 1
        # and at most one vertex has inDegree-outDegree = 1
        # and rest of the vertices have inDegree-outDegree = 0
        # if not then it is not euler path

        # if any graph have euler circuit then it has euler path
        # vice versa is not True
         
        inOut = outIn = even = 0
        totalVertices = len(inDegree)

        for u in self.graph:
            if inDegree[u] == outDegree[u]:
                even += 1
            elif inDegree[u] - outDegree[u] == 1:
                inOut += 1
            elif outDegree[u] - inDegree[u] == 1:
                outIn += 1
        
        if inOut <= 1 and outIn <= 1 and totalVertices == inOut + outIn + even:
            print("Graph has Euler Path")
        else:
            print("Graph has no Euler Path")
# Time Complexity: O(V+E)
# Space Complexity: O(V)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 1)
    g.add_edge(2, 0)
    g.add_edge(1, 2)
    g.add_edge(4, 0)
    g.add_edge(1, 4)
    g.find_euler_path()