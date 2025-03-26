# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.


# Example 2:
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").


# Example 3:
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.


from collections import Counter
from typing import List


class Solution:
    def isValidPair(self, s, t):
        set1 = set(s)
        set2 = set(t)
        if len(set1) != len(s):
            return False
        
        if len(set2) != len(t):
            return False
        
        if len(set1.intersection(set2)) == 0:
            return True
        return False
    
    def dfs(self, arr, i, currentString):
        self.maxxLength = max(self.maxxLength, len(currentString))

        for j in range(i, len(arr)):
            if self.isValidPair(currentString, arr[j]):
                self.dfs(arr, j + 1, currentString + arr[j])

    def maxLength(self, arr: List[str]) -> int:
        self.maxxLength = 0
        self.dfs(arr, 0, '')
        return self.maxxLength


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxLength(["un","iq","ue"]))
    print(sol.maxLength(["cha","r","act","ers"]))