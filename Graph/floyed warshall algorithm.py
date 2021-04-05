import sys


class Graph:
    def __init__(self, graph):
        self.graph = graph

    def copyGraph(self):
        total_no_vertices = len(self.graph[0])
        mat = [0] * total_no_vertices
        for i in range(total_no_vertices):
            temp = [0] * total_no_vertices
            for j in range(total_no_vertices):
                temp[j] = self.graph[i][j]
                if temp[j] == 0:
                    temp[j] = sys.maxsize
            mat[i] = temp
        return mat

    def floyedWarshallAlgorithm(self):
        total_no_vertices = len(self.graph[0])
        mat = self.copyGraph()

        for k in range(total_no_vertices):
            for i in range(total_no_vertices):
                for j in range(total_no_vertices):
                    if mat[i][k] > mat[i][j] + mat[j][k]:
                        mat[i][k] = mat[i][j] + mat[j][k]
        
        for i in range(total_no_vertices):
            for j in range(total_no_vertices):
                if mat[i][j] == sys.maxsize:
                    print("-1",end=' ')
                else:
                    print(mat[i][j],end=' ')
            print()

if __name__ == "__main__":
    mat = [ [0,4,5,0],
            [0,0,6,7],
            [0,0,0,8],
            [0,0,0,0]]
    g = Graph(mat)

    g.floyedWarshallAlgorithm()

