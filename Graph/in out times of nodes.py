# if in query given u,v meaning if u falls under sub-graph of v or viceversa
# then return true , we can do this by just applying dfs to find connection 
# from u to v or v to u. Time complexity of that algorithm will be O(V+E)
# what if we need to do multiple times this then it will not be a efficient 
# solution. For this we are using in out times of each vertices of dfs calls
# Though it will take O(V+E) time to generate it first but then each query will
# be done in constant time 

from collections import defaultdict
from dataclasses import dataclass


@dataclass
class In_Out_Info:
    inTime:int=None
    outTime:int=None

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.__in_out_process = False
        self.timer = 1

    def addEdge(self, u ,v):
        self.graph[u].append(v)

    def dfs(self, vertex, visited):
        visited[vertex] = True
        self.in_out_info[vertex].inTime = self.timer
        self.timer += 1

        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                visited = self.dfs(neighbour, visited)

        self.in_out_info[vertex].outTime = self.timer
        self.timer += 1
        return visited

    def in_out(self):
        visited = defaultdict(bool)
        self.in_out_info = defaultdict(In_Out_Info)
        for vertex in list(self.graph):
            if visited[vertex] == False:
                visited = self.dfs(vertex, visited) 

    def in_out_query(self, u, v):
        if self.__in_out_process == False:
            self.in_out()
            self.__in_out_process = True

        if self.in_out_info[u].inTime < self.in_out_info[v].inTime and self.in_out_info[u].outTime > self.in_out_info[v].outTime:
            return True
        if self.in_out_info[v].inTime < self.in_out_info[u].inTime and self.in_out_info[v].outTime > self.in_out_info[u].outTime:
            return True
        return False


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 6)
    # g.addEdge(5, 6)

    print(g.in_out_query(4, 6))