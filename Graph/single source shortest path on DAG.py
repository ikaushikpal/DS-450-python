from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))


    def dfs(self, vertex, visited, order):
        visited[vertex] = True
        for neighbour, dist in self.graph[vertex]:
            if visited[neighbour] == False:
                self.dfs(neighbour, visited, order)
        order.append(vertex)

    def topologicalSort(self):
        visited = defaultdict(bool)
        order =[]

        for vertex in list(self.graph):
            if visited[vertex] == False:
                self.dfs(vertex, visited, order)
        return order

    def printDistance(self, source, distance):
        count = 0
        for key in distance:
            print(f"distance from {source} to {key} = {distance[key]}")
            count += 1

        if count == 0:
            print(f"From {source} we can not reach to any vertex")

    def SSSP_on_DAG(self, source):
        INF = 9999999
        order = self.topologicalSort()
        distance = defaultdict(lambda:INF) #for default value changing 0 to 9999999
        distance[source] = 0

        while len(order):
            vertex = order.pop()
            currentDistance =  distance[vertex]
            if currentDistance != INF:
                for neighbour,weight in self.graph[vertex]:
                    distance[neighbour] = min(distance[neighbour], currentDistance + weight)
        
        self.printDistance(source, distance)
    

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2, 10)
    g.addEdge(1, 3, 8)
    g.addEdge(2, 4, -3)
    g.addEdge(2, 5, 12)
    g.addEdge(3, 6, -4)
    g.addEdge(4, 7, 6)
    g.addEdge(5, 7, 5)
    g.addEdge(6, 5, 1)
    g.addEdge(6, 7, 2)

    g.SSSP_on_DAG(5)
