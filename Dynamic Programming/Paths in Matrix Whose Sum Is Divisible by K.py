# You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

# Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:
# Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
# Output: 2
# Explanation: There are two paths where the sum of the elements on the path is divisible by k.
# The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
# The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.


# Example 2:
# Input: grid = [[0,0]], k = 5
# Output: 1
# Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.


# Example 3:
# Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
# Output: 10
# Explanation: Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.



from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M, N, MOD = len(grid), len(grid[0]), 10 ** 9 + 7
        
        dp = [[[0] * k for _ in range(N)] for _ in range(M)]
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(M):
            for j in range(N):
                for s in range(k):
                    modded_sum = (s + grid[i][j]) % k
                    
                    if i > 0: dp[i][j][modded_sum] += dp[i - 1][j][s]
                    if j > 0: dp[i][j][modded_sum] += dp[i][j - 1][s]
                        
                    dp[i][j][modded_sum] = dp[i][j][modded_sum] % MOD
                    
        return dp[-1][-1][0]
# Time Complexity: O(M * N * K)
# Space Complexity: O(M * N * K)    


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3))
    print(sol.numberOfPaths(grid = [[0,0]], k = 5))
    print(sol.numberOfPaths(grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1))