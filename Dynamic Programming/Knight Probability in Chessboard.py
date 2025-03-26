# On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

# A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.


# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

# The knight continues moving until it has made exactly k moves or has moved off the chessboard.

# Return the probability that the knight remains on the board after it has stopped moving.

 

# Example 1:
# Input: n = 3, k = 2, row = 0, column = 0
# Output: 0.06250
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.


# Example 2:
# Input: n = 1, k = 0, row = 0, column = 0
# Output: 1.00000


class Solution:
    def helper(self, row, col, k, n):
        if row < 0 or row >= n or col < 0 or col >= n:
            return 0
        
        if k == 0:
            return 1

        if (row, col, k) in self.memo:
            return self.memo[(row, col, k)]

        count = 0
        for x, y in self.moves:
            count += self.helper(row+x, col+y, k-1, n)
            
        self.memo[(row, col, k)] = count / 8
        return self.memo[(row, col, k)]

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.memo = {}
        self.moves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
        return self.helper(row, column, k, n)
# Time Complexity: O(N^2 * K)
# Space Complexity: O(N^2 * K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.knightProbability(3, 2, 0, 0))
    print(sol.knightProbability(1, 0, 0, 0))