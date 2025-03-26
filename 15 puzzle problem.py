class Solution:
    def __init__(self, board):
        self.board = board
        self.N = len(board)
        self.INF = 999999
        self.xMoves = [-1, 0, 1, 0]
        self.yMoves = [0, 1, 0, -1]
        self.moves = {0: "U", 1: "R", 2: "D", 3: "L"}
        self.movesCount = 4

    def calculateCost(self):
        counter = 1
        cost = 0
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] != counter:
                    cost += 1
                counter += 1

        return cost - 1

    def findEmptyTile(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 0:
                    return i, j

    def checkLocation(self, x, y):
        if 0 <= x < self.N and 0 <= y < self.N:
            return True
        else:
            return False

    def findMinimum(self, costArr):
        index = -1
        minCost = self.INF

        for i in range(self.movesCount):
            if costArr[i] != self.INF:
                if costArr[i] < minCost:
                    minCost = costArr[i]
                    index = i

        return index

    def swapAndCalculate(self, xOLD, yOLD, xNEW, yNEW):
        self.board[xNEW][yNEW], self.board[xOLD][yOLD] = (
            self.board[xOLD][yOLD],
            self.board[xNEW][yNEW],
        )
        res = self.calculateCost()
        self.board[xNEW][yNEW], self.board[xOLD][yOLD] = (
            self.board[xOLD][yOLD],
            self.board[xNEW][yNEW],
        )

        return res

    def resetCost(self, costArr):
        for i in range(self.movesCount):
            costArr[i] = self.INF

    def findSolution(self):
        x, y = self.findEmptyTile()
        prevMove = ""

        costArr = [self.INF] * self.movesCount
        xMoves = [self.INF] * self.movesCount
        yMoves = [self.INF] * self.movesCount

        totalMoves = 0
        minimumIndex = 0
        resultMoves = []

        # 0 -> UP
        # 1- > RIGHT
        # 2 -> DOWN
        # 3 -> LEFT

        while costArr[minimumIndex] != 0 and self.board[self.N - 1][self.N - 1] != 0:

            for i in range(self.movesCount):
                xNew = x + self.xMoves[i]
                yNew = y + self.yMoves[i]

                if (
                    prevMove == "D"
                    and self.moves[i] == "U"
                    or prevMove == "U"
                    and self.moves[i] == "D"
                    or prevMove == "L"
                    and self.moves[i] == "R"
                    or prevMove == "R"
                    and self.moves[i] == "L"
                ):
                    continue

                if self.checkLocation(xNew, yNew):
                    costArr[i] = self.swapAndCalculate(x, y, xNew, yNew)
                    xMoves[i] = xNew
                    yMoves[i] = yNew

            minimumIndex = self.findMinimum(costArr)

            xNew = xMoves[minimumIndex]
            yNew = yMoves[minimumIndex]
            totalMoves += 1

            self.board[xNew][yNew], self.board[x][y] = (
                self.board[x][y],
                self.board[xNew][yNew],
            )

            x = xNew
            y = yNew

            resultMoves.append(self.moves[minimumIndex])
            prevMove = resultMoves[-1]
            self.resetCost(costArr)

        print(f"To solve need We need {totalMoves} moves")
        print("->".join(resultMoves))


if __name__ == "__main__":
    board = [[6,13,7,10], [8,9,11,0], [15,2,12,5], [14,3,1,4]]

    sol = Solution(board)
    sol.findSolution()
