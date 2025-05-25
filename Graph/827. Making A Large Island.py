# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

# Example 2:
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

# Example 3:
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 

# Constraints:
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.


from typing import List

class DisjointSet:
    def __init__(self, N):
        self.size = [1] * N
        self.parent = [i for i in range(N)]

    def find(self, u):
        if u == self.parent[u]:
            return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        uParent = self.find(u)
        vParent = self.find(v)

        if uParent == vParent:
            return False

        if self.size[uParent] >= self.size[vParent]:
            self.size[uParent] += self.size[vParent]
            self.parent[vParent] = uParent
        else:
            self.size[vParent] += self.size[uParent]
            self.parent[uParent] = vParent
        return True


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        ds = DisjointSet(N * M)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    continue
            
                index = i * M + j
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    newIndex = x * M + y

                    if x < 0 or x >= N or y < 0 or y >= M:
                        continue

                    if grid[x][y] == 0:
                        continue

                    ds.union(index, newIndex)
        
        largestIslandSize = max(ds.size)
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    continue
            
                index = i * M + j
                diffParents = set()
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    newIndex = x * M + y

                    if x < 0 or x >= N or y < 0 or y >= M:
                        continue

                    if grid[x][y] == 0:
                        continue
                    
                    newIndexParent = ds.find(newIndex)
                    diffParents.add(newIndexParent)

                islandSize = 0
                for parent in diffParents:
                    islandSize += ds.size[parent]
                
                largestIslandSize = max(largestIslandSize, islandSize + 1)
        return largestIslandSize
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestIsland(grid = [[1,0],[0,1]]))
    print(sol.largestIsland(grid = [[1,1],[1,0]]))
    print(sol.largestIsland(grid = [[1,1],[1,1]]))