# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 
# Example 1:
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.

# Example 2:
# Input: n = 1
# Output: 1
 
# Constraints:
# 1 <= n <= 1000


class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        if n == 3:
            return 5

        dp1 = 1
        dp2 = 2
        dp3 = 5
        MOD = 10**9 + 7

        for _ in range(n - 3):
            dp4 = (2 * dp3 + dp1) % MOD
            dp1 = dp2
            dp2 = dp3
            dp3 = dp4
        return dp3
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTilings(3))
    print(sol.numTilings(1))