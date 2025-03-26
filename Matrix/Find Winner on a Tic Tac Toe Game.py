from typing import List


class Solution:
    def check_win(self, board, val):
        for i in range(3):
            if board[i][0] == val and board[i][1] == val and board[i][2]==val:
                return True
        
        for i in range(3):
            if board[0][i] == val and board[1][i] == val and board[2][i]==val:
                return True

        if board[0][0] == val and board[1][1] == val and board[2][2]==val:
            return True
        elif board[0][2] == val and board[1][1] == val and board[2][0]==val:
            return True
        else:
            return False
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"
        
        board = [[-1]*3 for _ in range(3)]
        
        for index in range(len(moves)):
            i, j = moves[index]
            board[i][j] = index % 2
        
        # 0 -> A
        # 1 -> B
        
        if self.check_win(board, 0):
            return 'A'
        elif self.check_win(board, 1):
            return 'B'
        elif len(moves) < 9:
            return 'Pending'
        else:
            return "Draw"
        
        
if __name__ == "__main__":
    moves = [[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]
    sol = Solution()
    print(sol.tictactoe(moves))