# Given a grid of dimension nxm containing 0s and 1s. Find the unit area of the largest region of 1s.
# Region of 1's is a group of 1's connected 8-directionally (horizontally, vertically, diagonally).
 

# Example 1:
# Input: grid = {{1,1,1,0},{0,0,1,0},{0,0,0,1}}
# Output: 5
# Explanation: The grid is-
# 1 1 1 0
# 0 0 1 0
# 0 0 0 1
# The largest region of 1's is colored
# in orange.


# Example 2:
# Input: grid = {{0,1}}
# Output: 1
# Explanation: The grid is-
# 0 1
# The largest region of 1's is colored in 
# orange.


class Solution:
    def __init__(self):
        self.xMoves = [0, 0, 1, -1, 1, 1, -1, -1]
        self.yMoves = [1, -1, 0, 0, 1, -1, 1, -1]
    
    def inBound(self, x, y):
        if 0<=x<self.N and 0<=y<self.M:
            return True
        return False
        
    def dfs(self, x, y):
        self.visited.add((x, y))
        area = 1
        
        for delX, delY in zip(self.xMoves, self.yMoves):
            newX = x + delX
            newY = y + delY
            if not self.inBound(newX, newY):
                continue
            
            if (newX, newY) in self.visited:
                continue
            
            if self.grid[newX][newY] == 0:
                continue
            
            area += self.dfs(newX, newY)
        return area
        
    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        self.grid = grid
        self.visited = set()
        self.N, self.M = len(grid), len(grid[0])
        
        maxArea = 0
        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i][j] and (i, j) not in self.visited:
                    maxArea = max(maxArea, self.dfs(i, j))
        return maxArea
# Time Complexity: O(N*M)
# Space Complexity: O(N*M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxArea(grid = [[1,1,1,0],[0,0,1,0],[0,0,0,1]]))
    print(sol.findMaxArea(grid = [[0,1]]))
    