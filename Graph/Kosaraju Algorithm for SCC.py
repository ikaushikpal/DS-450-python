from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def topologicalSort(self):
        order = deque()
        visited = set()

        def dfs(node):
            visited.add(node)
            for child in self.graph[node]:
                if child not in visited:
                    dfs(child)
            order.append(node)
        
        for node in self.graph:
            if node not in visited:
                dfs(node)

        return order
    
    def transposeGraph(self):
        gTranspose = Graph()

        for node in self.graph:
            for child in self.graph[node]:
                gTranspose.addEdge(child, node)

        return gTranspose
    
    def dfs(self, u, visited, component):
        visited.add(u)
        for child in self.graph[u]:
            if child not in visited:
                self.dfs(child, visited, component)
        component.append(u)

    def kosarajuAlgorithm(self):
        stack = self.topologicalSort()
        gTranspose = self.transposeGraph()
        ans = []
        visited = set()

        while len(stack):
            node = stack.pop()
            if node not in visited:
                component = []
                gTranspose.dfs(node, visited, component)
                ans.append(component)
        
        return ans
# Time Complexity: O(V + E) + O(V + E) + O(V + E) = O(V + E)
# Space Complexity: O(V + E) + O(V) + O(V) = O(V + E)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 2)
    g.addEdge(1, 0)
    g.addEdge(2, 1)

    g.addEdge(2, 3)

    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 3)

    print(g.kosarajuAlgorithm())




    