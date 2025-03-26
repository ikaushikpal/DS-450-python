# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true

# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        windowLength = len(s1)
        uniqueChars = Counter(s1)
        remainingChars = len(uniqueChars)
        
        for i, char in enumerate(s2):
            if char in uniqueChars:
                uniqueChars[char] -= 1
                if uniqueChars[char] == 0:
                    remainingChars -= 1
            
            if i >= windowLength:
                removeChar = s2[i - windowLength]
                if removeChar in uniqueChars:
                    uniqueChars[removeChar] += 1
                    if uniqueChars[removeChar] == 1:
                        remainingChars += 1
            
            if remainingChars == 0:
                return True
        return False
# Time Complexity: O(n)
# Space Complexity: O(26) = O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))
    print(sol.checkInclusion("ab", "eidboaoo"))