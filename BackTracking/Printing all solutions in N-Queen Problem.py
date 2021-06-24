# space optimized solution with O(N) space
class Solution:

    def __init__(self):
        self.res = []

    def isSafe(self, board, x, y, N):
        # checking for upper rows
        for i in range(x):
            if board[i] == y:
                return False
        
        # checking for left diagonal
        row = x
        col = y
        while row>= 0 and col>=0:
            if board[row] == col:
                return False
            
            row -= 1
            col -= 1
        
        # checking for right diagonal
        row = x
        col = y
        while row>= 0 and col < N:
            if board[row] == col:
                return False
            
            row -= 1
            col += 1
        
        return True
    
    def solveNQueen(self, N):
        self.res = []
        board = [-1] * N

        self.solveNQueenUtil(board, 0, N)

        if len(self.res):
            self.printBoard()
        else:
            print("Solution doesn't exist")
    

    def solveNQueenUtil(self, board, row, N):
        if row == N:
            self.res.append(board.copy())
            return True
        
        for col in range(N):
            if self.isSafe(board, row, col, N):
                board[row] = col

                self.solveNQueenUtil(board, row + 1, N)
                
                board[row] = -1
        

    def printBoard(self):
        print(f"Total No of solutions = {len(self.res)}")
        for row in self.res:
            for val in row:
                print(1+val, end= ' ')
            print()
    


if __name__ == '__main__':
    sol = Solution()
    sol.solveNQueen(8)
