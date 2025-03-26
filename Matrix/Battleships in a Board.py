from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        battleships = neighbour = 0
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "X":
                    battleships += 1
                    
                    # checking for down neighbour
                    if i+1 < row and board[i+1][j] == 'X':
                        neighbour += 1
                    
                    # checking for right neighbour
                    if j+1 < col and board[i][j+1] == "X":
                        neighbour += 1
            
        return battleships - neighbour
