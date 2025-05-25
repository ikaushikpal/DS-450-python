# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

# Example 1:
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

# Example 2:
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

# Example 3:
# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

# Constraints:
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10^4
# No two stones are at the same coordinate point.


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
    def removeStones(self, stones: List[List[int]]) -> int:
        # Find the maximum row and column index among all stones
        maxRow = maxCol = 0
        for row, col in stones:
            maxRow = max(maxRow, row)
            maxCol = max(maxCol, col)

        # Initialize Disjoint Set with size large enough to accommodate both rows and columns
        # We shift column indices to avoid collision with row indices
        ds = DisjointSet(maxRow + maxCol + 2)

        # Keep track of all unique nodes (row or column indices used in union)
        stonesNodes = set()

        for u, v in stones:
            # Union the row (u) and the shifted column index (maxRow + v + 1)
            # The +1 ensures no overlap if row and column index are the same
            ds.union(u, maxRow + v + 1)

            # Track the nodes involved in union operations
            stonesNodes.add(u)
            stonesNodes.add(maxRow + v + 1)

        # Count how many connected components are present among the nodes
        # Each connected component must leave at least one stone (i.e., can't remove all stones)
        connectedComps = 0
        for stoneNode in stonesNodes:
            if ds.find(stoneNode) == stoneNode:
                # If a node is its own parent, it's a representative of a component
                connectedComps += 1

        # The maximum number of stones that can be removed
        # is total stones minus the number of connected components
        return len(stones) - connectedComps

# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
    print(sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
    print(sol.removeStones([[0,0]]))