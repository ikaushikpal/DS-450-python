# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 1



# Example 2:
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2



# Example 3:
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1


from collections import deque
from typing import List


class Solution:
    def exploreConnectComponenet(self, i, j, visited, queue, grid):
        visited.add((i, j))
        queue.append((i, j))

        for x, y in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            newX = i + x
            newY = j + y
            if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == 1 and (newX, newY) not in visited:
                self.exploreConnectComponenet(newX, newY, visited, queue, grid)
    
    def findClosestComponent(self, queue, visited, grid):
        distance = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for x, y in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    newX = i + x
                    newY = j + y
                    if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and (newX, newY) not in visited:
                        if grid[newX][newY] == 1:
                            return distance

                        queue.append((newX, newY))
                        visited.add((newX, newY))

            distance += 1
        
        return distance

    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    self.exploreConnectComponenet(i, j, visited, queue, grid)
                    return self.findClosestComponent(queue, visited, grid)


if __name__ == '__main__':
    print(Solution().shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))
    print(Solution().shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
