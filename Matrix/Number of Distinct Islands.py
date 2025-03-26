# Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).


# Example 1:
# Input:
# grid[][] = {{1, 1, 0, 0, 0},
#             {1, 1, 0, 0, 0},
#             {0, 0, 0, 1, 1},
#             {0, 0, 0, 1, 1}}
# Output:
# 1
# Explanation:
# grid[][] = {{1, 1, 0, 0, 0}, 
#             {1, 1, 0, 0, 0}, 
#             {0, 0, 0, 1, 1}, 
#             {0, 0, 0, 1, 1}}
# Same colored islands are equal.
# We have 2 equal islands, so we 
# have only 1 distinct island.


# Example 2:
# Input:
# grid[][] = {{1, 1, 0, 1, 1},
#             {1, 0, 0, 0, 0},
#             {0, 0, 0, 0, 1},
#             {1, 1, 0, 1, 1}}
# Output:
# 3
# Explanation:
# grid[][] = {{1, 1, 0, 1, 1}, 
#             {1, 0, 0, 0, 0}, 
#             {0, 0, 0, 0, 1}, 
#             {1, 1, 0, 1, 1}}
# Same colored islands are equal.
# We have 4 islands, but 2 of them
# are equal, So we have 3 distinct islands.


import sys
from typing import List
sys.setrecursionlimit(10**8)


class Solution:
    def __init__(self):
        self.dir_x = [-1, +1, 0, 0]
        self.dir_y = [0, 0, -1, +1]
        self.dir_m = ['U', 'D', 'L', 'R']

    def check_valid(self, x ,y ):
        if 0<=x<self.row and 0<=y<self.col:
            return True
        return False

    def dfs(self, x, y):
        self.visited[x][y] = True

        for del_x, del_y, move in zip(self.dir_x, self.dir_y, self.dir_m):
            new_x = x + del_x
            new_y = y + del_y
        
            if not self.check_valid(new_x, new_y):
                continue
            
            if not self.grid[new_x][new_y]:
                continue
            
            if self.visited[new_x][new_y]:
                continue
            
            self.path += move
            self.dfs(new_x, new_y)

    def countDistinctIslands(self, grid: List[List[str]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        self.grid = grid
        self.visited = [[False]*self.col for _ in range(self.row)]
        unique_islands = set()
        
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] and not self.visited[i][j]:
                    self.path = 'S'
                    self.dfs(i, j)
                    unique_islands.add(self.path)
        return len(unique_islands)
# T.C. = O(n*m)
# S.C. = O(n*m)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDistinctIslands([[1, 1, 0, 0, 0],
                                    [1, 1, 0, 0, 0],    
                                    [0, 0, 0, 1, 1],
                                    [0, 0, 0, 1, 1]]))

    print(sol.countDistinctIslands([[1, 1, 0, 1, 1],
                                    [1, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 1],
                                    [1, 1, 0, 1, 1]]))
