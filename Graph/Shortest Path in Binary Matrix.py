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
import heapq
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        N = len(grid)
        if N == 1:
            return 1

        dx = (0, 1, 0, -1, 1, 1, -1, -1)
        dy = (1, 0, -1, 0, 1, -1, 1, -1)

        zeroCoords = [(1, 0, 0)]
        dist = [[float('inf')] * N for _ in range(N)]
        dist[0][0] = 1
        
        while zeroCoords:
            d, x, y = heapq.heappop(zeroCoords)

            for delX, delY in zip(dx, dy):
                newX = x + delX
                newY = y + delY
                
                if 0>newX or newX >= N or newY < 0 or newY >= N:
                    continue
                
                if grid[newX][newY] == 1:
                    continue
                
                if newX == N - 1 and newY == N - 1:
                    return d + 1

                if dist[newX][newY] > d + 1:
                    dist[newX][newY] = d + 1
                    heapq.heappush(zeroCoords, (d + 1, newX, newY))
        return -1
# Time Complexity: O(N^2logN)
# Space Complexity: O(N^2)


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
    print(s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))

