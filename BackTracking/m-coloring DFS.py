from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Info:
    visited: bool = False
    color : int = -1
    parent: int = None


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def kGraph(self, k, selfLoop=False):
        for i in range(k):
            for j in range(i):
                self.addEdge(i, j)
        
        if selfLoop:
            for i in range(k):
                self.addEdge(i, i)

class MColoring:
    def __init__(self, graphObj, M):
        self.graphObj = graphObj
        self.graph = self.graphObj.graph
        self.M = M
    
    def printColors(self):
        print(f"{'Vertex':<10} {'Parent-Vertex':<16} Color")
        for u in list(self.graph):
            print(f"{u:<10} {self.info[u].parent} {self.info[u].color:>18}")

        print("*" * 35)

    def colorGraph(self, source):
        self.info = defaultdict(Info)
        
        try:
            if source not in self.graph:
                raise KeyError

            for i in range(1, self.M + 1):
                self.info[source].color = i
                if self.dfsUtil(source):
                    self.printColors()
                    return
            
            print(f"We can not color graph with {self.M} colors")

        except KeyError:
            print("Invalid Source Vertex")
        
        except Exception as e:
            print(e)


    def dfsUtil(self, u):
        self.info[u].visited = True

        for vertex in self.graph[u]:
            if self.info[vertex].visited == False:  # not visited vertices
                for i in range(1, self.M + 1):
                    if self.info[u].color != i:
                        self.info[vertex].color = i
                        self.info[vertex].parent = u

                        if self.dfsUtil(vertex):
                            return True

                        self.info[vertex].color = -1
                        self.info[vertex].visited = True
                        self.info[vertex].visited = False
                return False

            elif self.info[u].color == self.info[vertex].color:
                return False
        return True
                

if __name__ == '__main__':
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(3, 2)

    mColor = MColoring(g, 3)
    mColor.colorGraph(1)

    g1 = Graph()
    g1.kGraph(4)
    mColor1 = MColoring(g1, 4)
    mColor1.colorGraph(0)

