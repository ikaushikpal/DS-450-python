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

    def floyedWarshallAlgorithm_util(self, total_no_vertices, mat):
        count = 0
        for k in range(total_no_vertices):
            for i in range(total_no_vertices):
                for j in range(total_no_vertices):
                    if mat[i][k] > mat[i][j] + mat[j][k]:
                        mat[i][k] = mat[i][j] + mat[j][k]
                        count += 1
        return count

    def floyedWarshallAlgorithm(self):
        total_no_vertices = len(self.graph[0])
        mat = self.copyGraph()

        self.floyedWarshallAlgorithm_util(total_no_vertices, mat)
        count = self.floyedWarshallAlgorithm_util(total_no_vertices, mat)

        if count > 0:
            print(f"Given graph contain negative weight cycle")
        else:
            print(f"Given graph does not contain negative weight cycle")


if __name__ == "__main__":
    mat = [ [0,4,5,0],
            [0,0,6,7],
            [0,0,0,8],
            [0,0,0,0]]
    g = Graph(mat)

    g.floyedWarshallAlgorithm()
