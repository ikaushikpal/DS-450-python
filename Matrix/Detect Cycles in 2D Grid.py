# Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

# A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

# Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

# Return true if any cycle of the same value exists in grid, otherwise, return false.

 

# Example 1:
# Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the image below:


# Example 2:
# Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:


# Example 3:
# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false
 

from typing import List

from sympy import continued_fraction_reduce


class Solution:
    def isValid(self, x, y, char):
        if 0<=x<len(self.grid) and 0<=y<len(self.grid[0]):
            return self.grid[x][y] == char
        return False
    
    def dfs(self, prevX, prevY, x, y, char):
        self.visited[x][y] = True
        
        for delX, delY in zip(self.dx, self.dy):
            newX, newY = x + delX, y + delY
            if (newX == prevX and newY == prevY) or not self.isValid(newX, newY, char):
                continue

            if self.visited[newX][newY]:
                return True
            
            if self.dfs(x, y, newX, newY, char):
                return True
        return False
    
    def containsCycle(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        self.grid = grid
        self.visited = [[False]*N for _ in range(M)]
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        
        for i in range(M):
            for j in range(N):
                if self.visited[i][j]:
                    continue

                char = self.grid[i][j]
                if self.dfs(-1, -1, i, j, char):
                    return True
        return False
# Time Complexity: O(M*N)
# Space Complexity: O(M*N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
    print(sol.containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))
    print(sol.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]))