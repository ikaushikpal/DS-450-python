# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.

# A good string is a string constructed by the above process having a length between low and high (inclusive).

# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

 
# Example 1:
# Input: low = 3, high = 3, zero = 1, one = 1
# Output: 8
# Explanation: 
# One possible valid good string is "011". 
# It can be constructed as follows: "" -> "0" -> "01" -> "011". 
# All binary strings from "000" to "111" are good strings in this example.


# Example 2:
# Input: low = 2, high = 3, zero = 1, one = 2
# Output: 5
# Explanation: The good strings are "00", "11", "000", "110", and "011".


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0
        
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
                
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
            
            if i >= low:
                ans = (ans + dp[i]) % MOD
        return ans
# Time Complexity: O(high)
# Space Complexity: O(high)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countGoodStrings(3, 3, 1, 1))
    print(sol.countGoodStrings(2, 3, 1, 2))