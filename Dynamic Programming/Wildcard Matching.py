# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N, M = len(s), len(p)
        
        dp = [[False] * (N+1) for _ in range(M+1)]
        dp[0][0] = True
        
        for i in range(1, M+1):
            # if pattern char is * then only check the previous char
            if p[i - 1] == '*':
                dp[i][0] = dp[i-1][0]
        
        for i in range(1, M+1):
            for j in range(1, N+1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] =='*':
                    # optimized version of 
                    # for k in range(0, j+1):
                    #   dp[i][j] = dp[i-1][k] or dp[i][j]
                    if j == 1:
                        dp[i][j] = dp[i-1][j-1] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[M][N]

if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch("adceb", "*a*b"))
    print(sol.isMatch("cb", "?a"))