class Solution:

    def __init__(self, board):
        self.board = board
        self.M = len(board)
        self.N = len(board[0])
    
    def checkXY(self, x, y):
        if 0<=x<self.M and 0<=y<self.N:
            return True
        return False

    def markLandmines(self):
        for i in range(self.M):
            for j in range(self.N):
                if self.board[i][j] == 0:
                    if self.checkXY(i-1, j):
                        self.board[i-1][j] = 0

                    if self.checkXY(i, j+1):
                        self.board[i][j+1] = 0

                    if self.checkXY(i+1, j):
                        self.board[i+1][j] = 0

                    if self.checkXY(i, j-1):
                        self.board[i][j-1] = 0

    def isSafe(self, x, y):
        if self.checkXY(x-1, j) and self.checkXY(x, j+1) and self.checkXY(x+1, j) and self.checkXY(x, j-1):
            return True
        else:
            return False

    def findPath(self):
        self.minimumTime = 999999
        self.markLandmines()

    def findPath(self, x, y, visited, counter):
        if y == self.N - 1:
            self.minimumTime = min(self.minimumTime, counter)
            return
        

        