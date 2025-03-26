# Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
# The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1.
 

# Example 1:
# Input: grid = {{0,1,1,0},{1,1,0,0},{0,0,1,1}}
# Output: {{1,0,0,1},{0,0,1,1},{1,1,0,0}}
# Explanation: The grid is-
# 0 1 1 0 
# 1 1 0 0 
# 0 0 1 1 
# 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and
# (2,1) are at a distance of 1 from 1's at (0,1),
# (0,2), (0,2), (2,3), (1,0) and (1,1)
# respectively.


# Example 2:
# Input: grid = {{1,0,1},{1,1,0},{1,0,0}}
# Output: {{0,1,0},{0,0,1},{0,1,2}}
# Explanation: The grid is-
# 1 0 1
# 1 1 0
# 1 0 0
# 0's at (0,1), (1,2), (2,1) and (2,2) are at a 
# distance of 1, 1, 1 and 2 from 1's at (0,0),
# (0,2), (2,0) and (1,1) respectively.


from collections import deque


class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid):
        N, M = len(grid), len(grid[0])
        dX = [1, -1, 0, 0]
        dY = [0, 0, 1, -1]
        
        ans = [[-1]*M for _ in range(N)]
        queue = deque()
        seen = set()
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    seen.add((i, j))
        
        while queue:
            i, j, moves = queue.popleft()
            ans[i][j] = moves
            
            for delX, delY in zip(dX, dY):
                newI = i + delX
                newJ = j + delY
                
                if newI < 0 or newI >= N or newJ < 0 or newJ >= M:
                    continue
                
                if (newI, newJ) in seen:
                    continue
                
                seen.add((newI, newJ))
                queue.append((newI, newJ, moves + 1))

        return ans
# Time Complexity: O(N*M)
# Space Complexity: O(N*M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.nearest([[0,1,1,0],[1,1,0,0],[0,0,1,1]]))
    print(sol.nearest([[1,0,1],[1,1,0],[1,0,0]]))