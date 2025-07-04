# Geek's village is represented by a 2-D matrix of characters of size n*m, where

# H - Represents a house
# W - Represents a well
# . - Represents an open ground
# N - Prohibited area(Not allowed to enter this area)

# Every house in the village needs to take water from a well, as the family members are so busy with their work, so every family wants to take the water from a well in minimum time, which is possible only if they have to cover as less distance as possible. Your task is to determine the minimum distance that a person in the house should travel to take out the water and carry it back to the house.

# A person is allowed to move only in four directions left, right, up, and down. That means if he/she is the cell (i,j), then the possible cells he/she can reach in one move are (i,j-1),(i,j+1),(i-1,j),(i+1,j), and the person is not allowed to move out of the grid.

# Note: For all the cells containing 'N', 'W' and '.' our answer should be 0, and for all the houses where there is no possibility of taking water our answer should be -1.


# Example 1:
# Input:
# n = 3
# m = 3
# c[][]: H H H
#        H W H
#        H H H
# Output:
# 4 2 4 
# 2 0 2 
# 4 2 4
# Explanation:
# There is only one well hence all the houses present
# in the corner of matrix will have to travel a minimum
# distance of 4, 2 is for house to well and other two is
# for well to house. And rest of the houses have to travel
# a minimum distance of 2 (House -> Well -> House).

# Example 2:
# Input:
# n = 5
# m = 5
# c[][]: H N H H H
#        N N H H W
#        W H H H H
#        H H H H H
#        H H H H H
# Output:
# -1 0 6 4 2 
# 0 0 4 2 0 
# 0 2 4 4 2 
# 2 4 6 6 4 
# 4 6 8 8 6
# Explanation:
# There is no way any person from the house in
# cell (0,0) can take the water from any well, and
# for rest of the houses there is same type of
# strategy we have to follow as followed in example 1. 
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function geekAndWells() which takes n and m, dimensions of the grid, and a 2-D grid of size n*m and returns a 2-D array containing the minimum distance for all the houses as explained above.

# Expected Time Complexity: O(n*m)
# Expected Space Complexity: O(n*m)

# Constraints:
# 1 <= n <= 10^3
# 1 <= m <= 10^3


from collections import deque
from typing import List


class Solution:

    def chefAndWells(self, ROWS: int, COLS: int, grid: List[List[str]]) -> List[List[int]]:
        HOUSE = 'H'
        WELL = 'W'
        GROUND = '.'
        NOT_ALLOWED = 'N'

        dist = [[float('inf')]*COLS for _ in range(ROWS)]
        visited = [[False] * COLS for _ in range(ROWS)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == WELL:
                    queue.append((row, col, 0))
                    dist[row][col] = 0
                    visited[row][col] = True
        
        while queue:
            row, col, cost = queue.popleft()

            dist[row][col] = cost

            for dx, dy in dirs:
                newRow = row + dx
                newCol = col + dy

                if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS:
                    continue

                if grid[newRow][newCol] == NOT_ALLOWED:
                    continue

                if visited[newRow][newCol]:
                    continue

                queue.append((newRow, newCol, cost + 1))
                visited[newRow][newCol] = True

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == HOUSE:
                    if dist[row][col] == float('inf'):
                        dist[row][col] = -1
                    else:
                        dist[row][col] = dist[row][col] << 1
                elif grid[row][col] in (NOT_ALLOWED, GROUND):
                    dist[row][col] = 0

        return dist
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.chefAndWells(3, 3, [['H', 'H', 'H'], ['H', 'W', 'H'], ['H', 'H', 'H']]))
    print(sol.chefAndWells(5, 5, [['H', 'N', 'H', 'H', 'H'], ['N', 'N', 'H', 'H', 'W'], ['W', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H']]))
    # 4 5
    # . . W . W
    # N W N N W
    # H . . H N
    # N N N . W
    print(sol.chefAndWells(2, 3, [['N', 'W', 'N'],
                                ['H', '.', 'H']]))
