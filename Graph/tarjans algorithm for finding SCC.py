from collections import defaultdict, deque


class Graph:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, u):
        self.low[u] = self.disc[u] = self.timer
        self.timer += 1
        self.stack.append(u)
        self.presentInStack[u] = True

        for v in self.graph[u]:
            if self.disc[v] == -1:
                self.dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
            
            elif self.presentInStack[v]: # if it a back edge
                self.low[u] = min(self.low[u], self.disc[v])
        
        if self.low[u] == self.disc[u]:
            print(f"SCC with head {u}: ")
            while self.stack[-1] != u:
                poppedVertex = self.stack.pop()
                self.presentInStack[poppedVertex] = False

                print(poppedVertex, end=' ')

            poppedVertex = self.stack.pop()
            self.presentInStack[poppedVertex] = False
            print(poppedVertex, end=' ')
            print()
            print("-" * 30)


    def tarjanSCC(self):
        self.timer = 0
        self.low = [-1] * self.V
        self.disc = [-1] * self.V
        self.presentInStack = [False] * self.V
        self.stack = deque()

        for u in range(self.V):
            if self.disc[u] == -1:
                self.dfs(u)


if __name__ == '__main__':
    g = Graph(11)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 0)
    g.addEdge(2, 6)
    g.addEdge(3, 2)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(5, 8)
    g.addEdge(5, 9)
    g.addEdge(6, 4)
    g.addEdge(7, 9)
    g.addEdge(8, 9)
    g.addEdge(9, 8)

    g.tarjanSCC()