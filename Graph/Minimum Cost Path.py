# Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which the total cost incurred is minimum.
# From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j). 

# Note: It is assumed that negative cost cycles do not exist in the input matrix.
 

# Example 1:
# Input: grid = {{9,4,9,9},{6,7,6,4},
# {8,3,3,7},{7,4,9,10}}
# Output: 43
# Explanation: The grid is-
# 9 4 9 9
# 6 7 6 4
# 8 3 3 7
# 7 4 9 10
# The minimum cost is-
# 9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.


# Example 2:
# Input: grid = {{4,4},{3,7}}
# Output: 14
# Explanation: The grid is-
# 4 4
# 3 7
# The minimum cost is- 4 + 3 + 7 = 14.


import heapq


class Solution:
    def minimumCostPath(self, grid):
        N = len(grid)
        src, dest = (0, 0), (N-1, N-1)
        minHeap = [(grid[0][0], 0, 0)] # (dist, x, y)
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        seen = set(src)
        
        while len(minHeap) > 0:
            dist, x, y = heapq.heappop(minHeap)
            if (x, y) == dest:
                return dist

            for delX, delY in moves:
                newX, newY = x + delX, y + delY
                if (newX, newY) in seen:
                    continue
                
                if 0<=newX<N and 0<=newY<N:
                    newDist = dist + grid[newX][newY]
                    heapq.heappush(minHeap, (newDist, newX, newY))
                    seen.add((newX, newY))
        return -1
# Time Complexity: O(N*N 2logN) = O(N^2logN)
# Space Complexity: O(N*N)


if __name__ == '__main__':
    sol = Solution()
    grid = [[9,4,9,9],[6,7,6,4],[8,3,3,7],[7,4,9,10]]
    print(sol.minimumCostPath(grid))
    grid = [[4,4],[3,7]]
    print(sol.minimumCostPath(grid))