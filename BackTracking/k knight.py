class Solution:

    def __init__(self):  
        self.xMoves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.yMoves = [1, 2, 2, 1, -1, -2, -2, -1]


    def solveKKnight(self, N):
        self.N = N
        self.board = [[-1] * N for x in range(N)]
        self.board[0][0] = 0

        resExist = self.solveKKnightUtil(0, 0, 1)
        if resExist:
            self.printBoard()
        else:
            print("Solution does not exist")


    def solveKKnightUtil(self, x ,y, counter):
        if counter == self.N **2 :
            return True


        for i in range(len(self.xMoves)):
            xNew = x + self.xMoves[i]
            yNew = y + self.yMoves[i]

            if 0<=xNew<self.N and 0<=yNew<self.N and self.board[xNew][yNew] == -1:
                self.board[xNew][yNew] = counter
                if self.solveKKnightUtil(xNew, yNew, counter+1):
                    return True

                self.board[xNew][yNew] = -1

        return False


    def printBoard(self):
        for row in range(self.N):
            print(*self.board[row])


if __name__ == '__main__':
    sol = Solution()
    sol.solveKKnight(5)
