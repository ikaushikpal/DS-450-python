# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.


# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true


# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false


# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
 
# Brute Force
class Solution:
    def dfs(self, s1, s2, s3, i, j, k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        
        cond1 = cond2 = False
        if i < len(s1) and s1[i] == s3[k]:
            cond1 = self.dfs(s1, s2, s3, i+1, j, k+1)
        
        if j < len(s2) and s2[j] == s3[k]:
            cond2 = self.dfs(s1, s2, s3, i, j+1, k+1)
        
        return cond1 or cond2

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        return self.dfs(s1, s2, s3, 0, 0, 0)
# Time Complexity: O(2**(m+n))
# Space Complexity: O(m+n)


# Memoization
class Solution:
    def dfs(self, s1, s2, s3, i, j, k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        cond1 = cond2 = False
        if i < len(s1) and s1[i] == s3[k]:
            cond1 = self.dfs(s1, s2, s3, i+1, j, k+1)
        
        if j < len(s2) and s2[j] == s3[k]:
            cond2 = self.dfs(s1, s2, s3, i, j+1, k+1)
        
        self.memo[(i, j)] = cond1 or cond2
        return self.memo[(i, j)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        self.memo = {}
        return self.dfs(s1, s2, s3, 0, 0, 0)
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)


# Bottom Up
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        N = len(s1)
        M = len(s2)
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True
        
        for i in range(N):
            if s1[i] == s3[i]:
                dp[i + 1][0] = True
            else:
                break
        
        for j in range(M):
            if s2[j] == s3[j]:
                dp[0][j + 1] = True
            else:
                break
                
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                
                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
        return dp[N][M]
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # cheap optimization
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        N = len(s1)
        M = len(s2)

        currRow = [False] * (M + 1)
        currRow[0] = True
        
        for j in range(M):
            if s2[j] == s3[j]:
                currRow[j + 1] = True
            else:
                break
                
        for i in range(1, N + 1):
            prevRow = currRow
            currRow = [False] * (M + 1)

            if s1[i - 1] == s3[i - 1]:
                currRow[0] = prevRow[0]
            
            for j in range(1, M + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    currRow[j] |= prevRow[j]
                
                if s2[j - 1] == s3[i + j - 1]:
                    currRow[j] |= currRow[j - 1]
        return currRow[M]
# Time Complexity: O(m*n)
# Space Complexity: O(m)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
    print(sol.isInterleave("", "", ""))