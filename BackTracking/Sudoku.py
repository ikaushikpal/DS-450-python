class Sudoku:
    def __init__(self):
        self.N = 9
    
    def isSafe(self, board, x, y, value):
        # check same row 
        for col in range(self.N):
            if board[x][col] == value:
                return False

        # check same column 
        for row in range(self.N):
            if board[row][y] == value:
                return False
        
        # check for 3x3
        boxRow = x - x%3
        boxCol = y - y%3
        
        for row in range(boxRow, boxRow+3):
            for col in range(boxCol, boxCol+3):
                if board[row][col] == value:
                    return False
        
        return True
    

    def solveSudoku(self, board):
        if self.solveSudokuUtil(board, 0, 0):
            self.printBoard(board)
        else:
            print("Solution does not exist")
    

    def solveSudokuUtil(self, board, x, y):
        if x == self.N-1 and y == self.N:
            return True

        if y == self.N:
            x += 1
            y = 0


        if board[x][y]:
            return self.solveSudokuUtil(board, x, y+1)


        for value in range(1, self.N+1):
            if self.isSafe(board, x, y, value):
                board[x][y] = value

                if self.solveSudokuUtil(board, x, y+1):
                    return True
            
            board[x][y] = 0

        return False


    def printBoard(self, board):
        for i in range(self.N):

            if i and i % 3 == 0:
                print("-" * 24)

            for j in range(self.N):

                if j and j % 3 == 0:
                    print(' | ', end='')

                print(board[i][j], end=' ')
                
            print()
        
        print()
            


if __name__ == '__main__':
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    sol = Sudoku()
    sol.solveSudoku(board)
