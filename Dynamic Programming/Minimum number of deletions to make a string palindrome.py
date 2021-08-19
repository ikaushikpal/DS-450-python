# 1312. Minimum Insertion Steps to Make a String Palindrome (same problem different name)
# Hard

# 1057

# 18

# Add to List

# Share
# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward


class Solution:
    def longestCommonSub(self, a, n, b, m):
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n<2:
            return n
        
        s1 = s
        s2 = s[::-1]
        lcs = self.longestCommonSub(s1, len(s1), s2, len(s2))

        return lcs
        
    def minimumNumberOfDeletions(self,S):
        n = len(S)
        lps = self.longestPalindromeSubseq(S)
        
        return n-lps


if __name__ == '__main__':
    s = "geeksforgeeks"
    print(Solution().minimumNumberOfDeletions(s))