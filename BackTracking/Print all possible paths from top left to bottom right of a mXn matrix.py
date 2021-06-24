class Solution:

    def __init__(self):
        self.xMoves = [1, 0]
        self.yMoves = [0, 1]
        self.moves = len(self.xMoves)
        self.res = []


    def solvePath(self, board):
        self.res = []
        self.M = len(board)
        self.N = len(board[0])
        visited = [[False] * self.N for x in range(self.M)]
        currentPath = [board[0][0]]

        self.solvePathUtil(board, 0 ,0, visited, currentPath)

        if len(self.res) == 0:
            print("Path does not exist")
        else:
            self.printPaths()
    

    def solvePathUtil(self, board, x, y, visited, currentPath):
        if x == self.M-1 and y == self.N-1:
            currentPath_copy = currentPath.copy()
            self.res.append(currentPath_copy)
            return
        
        for i in range(self.moves):
            xNew = x + self.xMoves[i]
            yNew = y + self.yMoves[i]

            if 0<=xNew<self.M and 0<=yNew<self.N and visited[xNew][yNew] == False:
                visited[xNew][yNew] = True
                currentPath.append(board[xNew][yNew])

                self.solvePathUtil(board, xNew, yNew, visited, currentPath)

                currentPath.pop()
                visited[xNew][yNew] = False
        


    def printPaths(self):
        for row in self.res:
            print(*row)



if __name__=='__main__':
    sol = Solution()
    board = [[1, 2, 3],
            [4, 5, 6]]
    
    sol.solvePath(board)
