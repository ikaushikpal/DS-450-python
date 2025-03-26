from collections import defaultdict



class Graph():
    def __init__(self, graph):
        self.INF = (1<<63) - 1
        self.graph = graph
        self.vertices = len(graph[0])
        self.visitedVertices = [False] * self.vertices
        self.path = defaultdict(list)
        self.distance = [self.INF] * self.vertices
    
    def dijkstraUtil(self):
        minDist = self.INF
        index = 0


        for i in range(self.vertices):
            dist = self.distance[i]

            if dist < minDist and not self.visitedVertices[i]:
                minDist = dist
                index = i
        
        return index

    def dijkstra(self, sourceVertex):
        self.path[sourceVertex] = 0
        self.distance[sourceVertex] = 0

        for v in range(self.vertices):
            self.path[v] = [chr(65 + sourceVertex)]

        for vertex in range(self.vertices):
            minimumIndex = self.dijkstraUtil()

            self.visitedVertices[minimumIndex] = True

            # for x in range(self.vertices):
            #     if self.visitedVertices[x] == False and minimumIndex != sourceVertex:
            #         self.path[x].append(chr(65+minimumIndex))

            if minimumIndex != sourceVertex and self.visitedVertices[minimumIndex]:
                self.path[minimumIndex].append(chr(65+minimumIndex))

            for v in range(self.vertices):
                currentCost = self.graph[minimumIndex][v]

                if self.graph[minimumIndex][v] < 0:
                    raise("Invalid Distance")

                elif self.graph[minimumIndex][v] > 0 and self.visitedVertices[v] == False and self.distance[v] > self.distance[minimumIndex] + currentCost:
                    self.distance[v] = self.distance[minimumIndex] + currentCost
                    self.path[v].append(chr(65 + minimumIndex))
        
        self.printRes()

    def printRes(self):
        print(f"{'Source':10} {'Destination':15} {'cost':10} {'path'}")

        for vertex in range(self.vertices):

            source = chr(65)
            destination = chr(65+vertex)
            cost = self.distance[vertex]
            path = self.path[vertex]
            # path = chr(65 + self.path[vertex]) + ' -> ' + chr(65 + vertex)

            print(f"  {source:10} {destination:8} {cost:8}        {path}")


# mat = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
#         [4, 0, 8, 0, 0, 0, 0, 11, 0], 
#         [0, 8, 0, 7, 0, 4, 0, 0, 2], 
#         [0, 0, 7, 0, 9, 14, 0, 0, 0], 
#         [0, 0, 0, 9, 0, 10, 0, 0, 0], 
#         [0, 0, 4, 14, 10, 0, 2, 0, 0], 
#         [0, 0, 0, 0, 0, 2, 0, 1, 6], 
#         [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#         [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        # ]; 
mat = [
        [0,5,1,0,0],
        [0,0,0,4,2],
        [0,3,0,4,0],
        [2,0,0,0,0],
        [0,0,0,1,0],
    ]

g = Graph(mat)
g.dijkstra(0)