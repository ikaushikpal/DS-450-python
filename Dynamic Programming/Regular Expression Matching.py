# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".


class Solution:
    def isMatchHelper(self, s, p, i, j, dp):
        if i >= len(s) and j >= len(p):
            return True
        
        if j >= len(p):
            return False
        

        if (i, j) in dp:
            return dp[(i, j)]

        match = i<len(s) and (s[i]==p[j] or p[j]=='.')
        
        if j+1<len(p) and p[j+1] == '*':
            dp[(i, j)] = (self.isMatchHelper(s, p, i, j+2, dp) or
                    (match and self.isMatchHelper(s, p, i+1, j, dp)))
        elif match:
            dp[(i, j)] = self.isMatchHelper(s, p, i+1, j+1, dp)
        else:
            dp[(i, j)] = False
        
        return dp[(i, j)]


    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        return self.isMatchHelper(s, p, 0, 0, dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch('aab', 'c*a*b*'))