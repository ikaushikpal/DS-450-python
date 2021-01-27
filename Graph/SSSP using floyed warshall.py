import sys


class Graph:
    def __init__(self, graph):
        self.graph = graph

    def copyGraph(self):
        total_no_vertices = len(self.graph[0])
        mat = [0] * total_no_vertices
        nextArr = [[-1]*total_no_vertices for x in range(total_no_vertices)]

        for i in range(total_no_vertices):
            temp = [0] * total_no_vertices

            for j in range(total_no_vertices):
                temp[j] = self.graph[i][j]
                if temp[j] == 0:
                    temp[j] = sys.maxsize
                    nextArr[i][j] = j
            mat[i] = temp
        return mat, nextArr

    def floyedWarshallAlgorithm(self, source, end):
        total_no_vertices = len(self.graph[0])
        mat, nextArr = self.copyGraph()

        for k in range(total_no_vertices):
            for i in range(total_no_vertices):
                for j in range(total_no_vertices):
                    if mat[i][k] > mat[i][j] + mat[j][k]:
                        mat[i][k] = mat[i][j] + mat[j][k]
                        nextArr[i][j] = nextArr[i][k]
        
        path = []
        if mat[source][end] == sys.maxsize:
            print(f"from {source} to {end} there is no path")
            return
        
        currentPos = source
        while currentPos != end:
            if currentPos == -1:
                print(f"Given graph contains negative cycle")
                return
            path.append(currentPos)
            currentPos = nextArr[currentPos][end]

        if nextArr[currentPos][end] == -1:
            print(f"Given graph contains negative cycle")
            return
        path.append(end)

        print("Path = ",path)


if __name__ == "__main__":
    mat = [ [0,4,5,0],
            [0,0,6,7],
            [0,0,0,8],
            [0,0,0,0]]
    g = Graph(mat)

    g.floyedWarshallAlgorithm(0, 2)

