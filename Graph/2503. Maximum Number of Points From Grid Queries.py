# You are given an m x n integer matrix grid and an array queries of size k.

# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

# If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

# Return the resulting array answer.


# Example 1:
# # Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# Output: [5,8,1]
# Explanation: The diagrams above show which cells we visit to get points for each query.

# Example 2:
# Input: grid = [[5,2,1],[1,1,2]], queries = [3]
# Output: [0]
# Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

# Constraints:
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# k == queries.length
# 1 <= k <= 104
# 1 <= grid[i][j], queries[i] <= 106


import heapq
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M, N = len(grid), len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        # sorting queries in increase order
        # cause if 8 value we get for 4 then for 5 minimum would be 8 if not more
        queries_indexes = [(query, i) for i, query in enumerate(queries)]
        queries_indexes.sort()

        # using min-heap to get minimum values cell
        min_heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        ans = [0] * len(queries)
        points = 0
        for query, index in queries_indexes:
            while min_heap and min_heap[0][0] < query:
                cell_value, x, y = heapq.heappop(min_heap)
                points += 1

                for del_x, del_y in zip(dx, dy):
                    new_x = x + del_x
                    new_y = y + del_y

                    if 0 <= new_x < M and 0<=new_y<N and (new_x, new_y) not in visited:
                        heapq.heappush(min_heap, (grid[new_x][new_y], new_x, new_y))
                        visited.add((new_x, new_y))
            ans[index] = points
        return  ans 
# Time Complexity: O(KlogK + MNlogMN)
# Space Complexity: O(K + MN)



if __name__ == '__main__':
    sol = Solution()
    print(sol.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))
    print(sol.maxPoints(grid = [[5,2,1],[1,1,2]], queries = [3]))