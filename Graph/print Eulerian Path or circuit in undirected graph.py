from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
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
    
    def build_path(self, u, edgeSet, path):
        path.append(u)

        for v in self.graph[u]:
            if (u, v) in edgeSet:
                edgeSet.remove((u, v))
                edgeSet.remove((v, u))
                self.build_path(v, edgeSet, path)
        
    def print_euler_path(self):
        if not self.is_connected():
            print("Graph is not connected")
            return
        
        oddDegVertices = set()
        tempVertex = None
        edgeSet = set()

        for u in self.graph:
            if len(self.graph[u]) & 1:
                oddDegVertices.add(u)

            if len(self.graph[u]) & 1 == 0 and  len(self.graph[u]) > 0:
                tempVertex = u

            edgeSet = edgeSet.union(set([(u, v) for v in self.graph[u]]))

        if len(oddDegVertices) != 0 and len(oddDegVertices) != 2:
            print('Graph do not contain any Euler Path')
            return 

        path = []
        if len(oddDegVertices) == 0:
            print("Printing Euler Circuit")
            self.build_path(tempVertex, edgeSet, path)
        else:
            print("Printing Euler Path")
            self.build_path(oddDegVertices.pop(), edgeSet, path)
        
        print('->'.join(map(str, path)))
# Time Complexity : O(V+E)
# Space Complexity : O(V+E)


if __name__ == '__main__':
    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 4)
    g1.add_edge(2, 4)
    g1.add_edge(1, 3)
    g1.add_edge(3, 4)
    g1.add_edge(4, 5)
    g1.add_edge(2, 5)
    g1.print_euler_path()

    g2 = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(3, 4)
    g2.add_edge(2, 4)
    g2.print_euler_path()
