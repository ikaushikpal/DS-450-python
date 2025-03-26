# Given a String S and an integer K. Find the count of all substrings of length K which have exactly K-1 distinct characters.


# Example 1:
# Input:
# S = "abcc"
# K = 2
# Output:
# 1
# Explanation:
# Possible substrings of length K = 2 are
# ab : 2 distinct characters
# bc : 2 distinct characters
# cc : 1 distinct character
# Only one valid substring exists {"cc"}. 


# Example 2:
# Input:
# S = "aabab"
# K = 3
# Output :
# 3
# Explanation:
# Possible substrings of length K = 3 are
# aab : 2 distinct characters
# aba : 2 distinct characters
# bab : 2 distinct characters.
# All of these Substrings are a possible answer,
# so the count is 3.



class Solution:
    def countOfSubstrings(self, S, K):
        charMap = {}
        ans = 0
        for i, char in enumerate(S):
            charMap[char] = charMap.get(char, 0) + 1
            
            if i - K >= 0:
                charMap[S[i - K]] -= 1
                if charMap[S[i - K]] == 0:
                    charMap.pop(S[i - K])
            
            if i >= K-1 and len(charMap) == K - 1:
                ans += 1
        return ans
# T.C. = O(N)
# S.C. = O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countOfSubstrings(S = "abcc", K = 2))
    print(sol.countOfSubstrings(S = "aabab", K = 3))