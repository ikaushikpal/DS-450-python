# Given a floor of dimensions 2 x W and tiles of dimensions 2 x 1, the task is to find the number of ways the floor can be tiled. A tile can either be placed horizontally i.e as a 1 x 2 tile or vertically i.e as 2 x 1 tile. Print the answer modulo 109+7.

 

# Example 1:

# Input:
# W = 3
# Output:
# 3
# Explanation:
# We need 3 tiles to tile the board
# of size  2 x 3. 
# We can tile in following ways:
# 1) Place all 3 tiles vertically. 
# 2) Place first tile vertically.
# and remaining 2 tiles horizontally.
# 3) Place first 2 tiles horizontally
# and remaining tiles vertically.

class Solution:
    # space : O(n)
    def numberOfWays(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        MOD = 10**9 + 7
        
        for i in range(1, n+1):
            if n>=2:
                dp[i] = (dp[i-1] + dp[i-2]) % MOD
            else:
                dp[i] = dp[i-1] % MOD
        
        return dp[n]
    
    # Space : O(1)
    def numberOfWaysConstant(self, n):
        first = 0
        second = 1

        for i in range(n):
            first, second = second, first+second
        
        return second


if __name__ == '__main__':
    n = 3
    print(Solution().numberOfWaysConstant(n))