from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        if grid[0][0] == 0 or grid[-1][-1] == 0:
            return True
        
        if M * N <= 2:
            return False

        bucket = {}
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    bucket[i + j] = bucket.get(i + j, 0) + 1

        for k in range(1, M + N - 2):
            if bucket.get(k, 0) <= 1:
                return True
        return False
sol = Solution()
print(sol.isPossibleToCutPath([[1,1,1],[1,0,0],[1,1,1]]))