# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 2


# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4


# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1


from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        DX = [0, 1, 0, -1, 1, 1, -1, -1]
        DY = [1, 0, -1, 0, 1, -1, 1, -1]
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            i, j, dist = queue.popleft()

            if i == ROWS - 1 and j == COLS - 1:
                return dist

            for del_x, del_y in zip(DX, DY):
                x, y = i + del_x, j + del_y
                if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append((x, y, dist + 1))
        
        return -1
# Time Complexity: O(N^2)
# Space Complexity: O(2 * N) = O(N)


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
    print(s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))

