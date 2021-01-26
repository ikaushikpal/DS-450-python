from collections import defaultdict
from dataclasses import dataclass


class Info():
    inTime:int=None
    lowTime:int=None

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.timer = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, currentVertex, parentVertex, visited, info, bridges):
        visited[currentVertex] = True
        info[currentVertex].inTime = info[currentVertex].lowTime = self.timer
        self.timer += 1

        for neighbour in self.graph[currentVertex]:
            if parentVertex == neighbour:
                continue # just a edge to its parent

            elif visited[neighbour]:#meaning it found a back edge
                info[currentVertex].lowTime = min(info[currentVertex].lowTime, info[neighbour].inTime)
                #update backedges property

            else: #forwards edge
                self.dfs(neighbour, currentVertex, visited, info, bridges)
                if info[currentVertex].inTime < info[neighbour].lowTime: #find bridge condition
                    bridges.append((currentVertex, neighbour))
                info[currentVertex].lowTime = min(info[currentVertex].lowTime, info[neighbour].lowTime)

    def  printBridges(self, bridges):
        if len(bridges) == 0:
            print("Graph do not contain any bridges")
            return
        print("Total number of bridges in graph are :",len(bridges))
        for u,v in bridges:
            print(f"bridge {u} -> {v}")
            
    def findBridges(self):
        visited = defaultdict(bool)
        info = defaultdict(Info)
        bridges = []

        for vertex in self.graph:
            if visited[vertex] == False:
                self.dfs(vertex, None, visited, info, bridges)
        
        self.printBridges(bridges)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(3, 2)
    g.addEdge(4, 2)
    g.addEdge(3, 4)

    g.findBridges()