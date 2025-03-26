class Solution:
    def isSafe(self, board, x, y, N):
        # checking for upper rows
        for i in range(0, x):
            if board[i][y] == 1:
                return False
        
        # checking for left diagonal
        row = x
        col = y
        while row>= 0 and col>=0:
            if board[row][col] == 1:
                return False
            
            row -= 1
            col -= 1
        
        # checking for right diagonal
        row = x
        col = y
        while row>= 0 and col < N:
            if board[row][col] == 1:
                return False
            
            row -= 1
            col += 1
        
        return True

    def solveNQueen(self, N):
        board = [[0] * N for i in range(N)]

        if self.solveNQueenUtil(board, 0, N):
            self.printBoard(board)
        else:
            print("Solution doesn't exist")
    
    def solveNQueenUtil(self, board, row, N):
        if row == N:
            return True
        
        for col in range(N):
            if self.isSafe(board, row, col, N):
                board[row][col] = 1
                if self.solveNQueenUtil(board, row + 1, N):
                    return True
                
                board[row][col] = 0
        
        return False

    def printBoard(self, board):
        for row in board:
            print(*row)



if __name__ == '__main__':
    sol = Solution()
    sol.solveNQueen(8)
