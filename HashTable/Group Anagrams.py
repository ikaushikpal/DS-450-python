# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# Example 2:
# Input: strs = [""]
# Output: [[""]]


# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


from collections import defaultdict
from typing import List


class Solution:
    def serialize(self, string):
        freq = [0] * 26
        for char  in string:
            freq[ord(char) - ord('a')] += 1
        
        msg = ''
        for i in range(26):
            char = chr(i + ord('a'))
            value = freq[i]
            msg = f'{msg}-{char}{value}'

        return msg
    
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        uniqueStr = defaultdict(list)

        for string in strings:
            txt = self.serialize(string)
            uniqueStr[txt].append(string)
        
        res = [sorted(value) for value in uniqueStr.values()]
        return res
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))
    