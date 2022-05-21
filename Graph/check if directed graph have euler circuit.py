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
    
    def find_euler_circuit(self):
        if not self.is_connected():
            print("Graph is not connected")
            return
        
        inDegree = defaultdict(int)
        outDegree = defaultdict(int)
        for u in self.graph:
            for v in self.graph[u]:
                inDegree[v] += 1
                outDegree[u] += 1
        
        # to check if directed graph has euler circuit
        # need to check if all vertices have same in and out degree
        # if not then it is not euler circuit
        for u in self.graph:
            if inDegree[u] != outDegree[u]:
                print("Graph has no Euler Circuit")
                return

        print("Graph has Euler Circuit")
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
    g.find_euler_circuit()