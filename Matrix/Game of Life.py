# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]


# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]


from typing import List


class Solution:
    def countNeighbors(self, board, x, y):
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        ROWS, COLS = len(board), len(board[0])
        count1 = 0
        
        for i, j in zip(dx, dy):
            xNew = x + i
            yNew = y + j
            if 0<=xNew<ROWS and 0<=yNew<COLS:
                if board[xNew][yNew] & 1 == 1:
                    count1 += 1
        
        return count1
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Since the board has ints but only the 1-bit is used, I use the 2-bit to store the new state. At the end, replace the old state with the new state by shifting all values one bit to the right.
        ROWS, COLS = len(board), len(board[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                c1 = self.countNeighbors(board, i, j)
                
                # live cell
                if board[i][j] == 1:
                    # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                    # Any live cell with more than three live neighbors dies, as if by over-population.
                    if c1 < 2 or c1 > 3:
                        board[i][j] = 1 # 01

                    # Any live cell with two or three live neighbors lives on to the next generation.
                    else:
                        board[i][j] = 3 # 11

                # dead cell       
                else:
                    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if c1 == 3:
                        board[i][j] = 2 # 10
                    
                    # do nothing
                    else:
                        board[i][j] = 0 # 00
        
        for i in range(ROWS):
            for j in range(COLS):
                board[i][j] = board[i][j] >> 1
                    

if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    sol = Solution()
    sol.gameOfLife(board)
    print(board)