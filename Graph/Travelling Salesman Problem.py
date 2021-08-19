class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.VISITED_ALL = (1<<self.V) - 1
    

    def tsp(self, source=0):
        self.source = source
        self.dp = [[-1]*self.V for _ in range(self.VISITED_ALL+1)]

        path = 1 << self.source
        return self.tspUtil(path, self.source)


    def tspUtil(self, path, currentVertex):        
        if path == self.VISITED_ALL: # if we visited all vertices then return curr to src cost
            self.dp[path][currentVertex] = self.graph[currentVertex][self.source]
            return self.graph[currentVertex][self.source]
        
        if self.dp[path][currentVertex] != -1:
            return self.dp[path][currentVertex]
        
        ans = 10**9

        for v in range(self.V):
            if ((1<<v) & path) == 0:
                currentRes = self.graph[currentVertex][v] + self.tspUtil(path|(1<<v), v)
                ans = min(ans, currentRes)

        
        self.dp[path][currentVertex] = ans
        return self.dp[path][currentVertex]


if __name__ == '__main__':
    graph = [[0,20,42,25],[20,0,30,25],[42,30,0,10],[25,25,10,0]]
    g = Graph(graph)

    print("Minimum Cost =", g.tsp())