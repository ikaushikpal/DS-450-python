# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

# Example 1:
# Input: grid = [[0,2],
#               [1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.



# Example 2:
# Input: grid = [[0,1,2,3,4],
#               [24,23,22,21,5],
#               [12,13,14,15,16],
#               [11,17,18,19,20],
#               [10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

# NOTE:
# simple dijkstra algorithm

from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DX = [0, 0, 1, -1]
        DY = [1, -1, 0, 0]
        visited = set()
        minHeap = [(grid[0][0], 0, 0)] # (time/ maxheight, x, y)
        visited.add((0, 0))

        while minHeap:
            time, x, y = heapq.heappop(minHeap)

            if x == ROWS - 1 and y == COLS - 1:
                return time

            for i, j in zip(DX, DY):
                newX, newY = x + i, y + j
                if 0 <= newX < ROWS and 0 <= newY < COLS and (newX, newY) not in visited:
                    heapq.heappush(minHeap, (max(time, grid[newX][newY]), newX, newY))
                    visited.add((newX, newY))
        
        return -1
# Time Complexity : O(N^2 logN) where N is the number of rows and columns in the grid.
# Space Complexity : O(N^2)
# we are poping N^2 elements from the minHeap and each moment maximum N^2 elements are present
# So O(N^2 logN*N) = O(2*N^2 logN) = O(N^2 logN)


if __name__ == "__main__":
    s = Solution()
    grid = [[0,2],[1,3]]
    print(s.swimInWater(grid))
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    print(s.swimInWater(grid))

