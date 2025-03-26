class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.totalVertices = len(self.graph[0])
    
    def minimumDistance(self, distance, visited):
        min = 999999
        for v in range(self.totalVertices): 
            if distance[v] < min and visited[v] == False: 
                min = distance[v] 
                min_index = v 
        return min_index 

    def dijkstraAlgorithm(self, source):
        visited = [False] * self.totalVertices
        distance = [999999] * self.totalVertices
        distance[source] = 0

        for i in range(self.totalVertices):
            minIndex = self.minimumDistance(distance, visited)
            if visited[minIndex] == True:
                continue
            visited[minIndex] = True

            for j in range(self.totalVertices):
                if visited[j] == False and self.graph[minIndex][j] > 0:
                    newDistance = self.graph[minIndex][j] + distance[minIndex]
                    distance[j] = min(distance[j], newDistance)

        self.printShortestDist(source, distance)


    def printShortestDist(self, source, distance):
        for i in range(self.totalVertices):
            print(f"distance from {source} to {i} = {distance[i]}")



if __name__ == "__main__":
    mat = [ [0, 4, 0, 0, 0, 0, 0, 8, 0], 
            [4, 0, 8, 0, 0, 0, 0, 11, 0], 
            [0, 8, 0, 7, 0, 4, 0, 0, 2], 
            [0, 0, 7, 0, 9, 14, 0, 0, 0], 
            [0, 0, 0, 9, 0, 10, 0, 0, 0], 
            [0, 0, 4, 14, 10, 0, 2, 0, 0], 
            [0, 0, 0, 0, 0, 2, 0, 1, 6], 
            [8, 11, 0, 0, 0, 0, 1, 0, 7], 
            [0, 0, 2, 0, 0, 0, 6, 7, 0] ]; 
    
    g = Graph(mat)
    g.dijkstraAlgorithm(0)