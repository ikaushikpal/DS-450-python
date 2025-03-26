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
    
    def find_euler(self):
        if not self.is_connected():
            return -1
        
        countOddDegree = 0
        for u in self.graph:
            if len(self.graph[u]) & 1:
                countOddDegree += 1
        
        if countOddDegree == 0:
            return 0
        elif countOddDegree == 2:
            return 1
        else:
            return -1
    
    def find_euler_path_cycle(self):
        res = self.find_euler()
        if res == -1:
            print('Graph do not contain any Euler Path or Circuit')
        elif res == 0:
            print('Graph contain Euler Circuit')
        elif res == 1:
            print('Graph contain Euler Path')
    

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    # g.add_edge(0, 1)
    g.add_edge(0, 2)
    # g.add_edge(0, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.find_euler_path_cycle()