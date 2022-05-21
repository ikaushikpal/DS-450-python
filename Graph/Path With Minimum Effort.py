# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

# Example 1:

# Input: heights = [[1,2,2],
#                   [3,8,2],
#                   [5,3,5]]

# Output: 2

# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.



# Example 2:

# Input: heights = [[1,2,3],
#                 [3,8,4],
#                 [5,3,5]]

# Output: 1

# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].



# Example 3:

# Input: heights =[[1,2,1,1,1],
#                 [1,2,1,2,1],
#                 [1,2,1,2,1],
#                 [1,2,1,2,1],
#                 [1,1,1,2,1]]

# Output: 0

# Explanation: This route does not require any effort.


from heapq import heappop, heappush
from typing import List

# applying Dijkstra Algorithm
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        distMat = [[float('inf')] * COLS for _ in range(ROWS)]
        DX = [0, 0, 1, -1]
        DY = [1, -1, 0, 0]
        
        minHeap = [(0, 0, 0)] # distance, row, col
        distMat[0][0] = 0

        while minHeap:
            dis, row, col = heappop(minHeap)

            # already optimized
            if dis > distMat[row][col]:
                continue

            # Reach to bottom right
            if row == ROWS - 1 and col == COLS - 1:
                return dis  

            for x, y in zip(DX, DY):
                newRow = row + x
                newCol = col + y

                if 0 <= newRow < ROWS and 0 <= newCol < COLS:
                    newDist = max(dis, abs(heights[newRow][newCol] - heights[row][col]))

                    if distMat[newRow][newCol] > newDist:
                        distMat[newRow][newCol] = newDist
                        heappush(minHeap, (distMat[newRow][newCol], newRow, newCol))

# Complexity

# Time: O(ElogV) = O(M*N log M*N), where M is the number of rows and N is the number of columns in the matrix.
# Space: O(M*N)


if __name__ == '__main__':
    heights = [[1,2,2],
               [3,8,2],
               [5,3,5]]
    print(Solution().minimumEffortPath(heights))
    heights = [[1,2,3],
               [3,8,4],
               [5,3,5]]
    print(Solution().minimumEffortPath(heights))
    heights = [[1,2,1,1,1],
               [1,2,1,2,1],
               [1,2,1,2,1],
               [1,2,1,2,1],
               [1,1,1,2,1]]
    print(Solution().minimumEffortPath(heights))