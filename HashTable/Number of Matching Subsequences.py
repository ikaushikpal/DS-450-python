# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".


# Example 2:
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2


from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        wordDict = defaultdict(list)
        for word in words:
            wordDict[word[0]].append(word)
        
        ans = 0
        for char in s:
            currWorkingSet = wordDict[char]
            wordDict[char] = []
            currWorkingSet = [word[1:] for word in currWorkingSet]

            for word in currWorkingSet:
                if len(word) == 0:
                    ans += 1
                else:
                    wordDict[word[0]].append(word)
        return ans
# Time Complexity: O(M + S + N)
# M is the number of words.
# S is the length of the string.
# N is the max length word in words.

# Space Complexity: O(M + S) 


if __name__ == '__main__':
    sol = Solution()
    print(sol.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))
    print(sol.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))