# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.


# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


class ZAlgorithm:
    def buildZArray(self, concatedString):
        N = len(concatedString)
        z = [0] * N
        left = right = 0
        
        for i in range(1, N):
            if right < i:
                left = right = i
                
                while right < N and concatedString[right] == concatedString[right - left]:
                    right += 1
                    
                z[i] = right - left
                right -= 1
            
            else:
                k = i - left
                if z[k] < right - i + 1:
                    z[i] = z[k]
                    
                else:
                    left = i
                    while right < N and concatedString[right] == concatedString[right - left]:
                        right += 1
                        
                    z[i] = right - left
                    right -= 1
            
        return z
    
    def search(self, string, pattern):
        concatedString = pattern + '$' + string
        z = self.buildZArray(concatedString)

        for i in range(len(pattern), len(concatedString)):
            if z[i] == len(pattern):
                return i - len(pattern) - 1
        return -1
        
    
class Solution:
    def __init__(self):
        self.zAlgo = ZAlgorithm()
        
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return self.zAlgo.search(haystack, needle)
# Time Complexity: O(N + M)
# Space Complexity: O(N + M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))
    print(sol.strStr("leetcode", "leeto"))