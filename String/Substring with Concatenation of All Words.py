# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
# You can return the answer in any order.
 

# Example 1:
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.


# Example 2:
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []


# Example 3:
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]


from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq = Counter(words)
        ans = []
        eachWordLen = len(words[0])
        totalWords = len(words)
        
        for i in range(len(s) - eachWordLen * totalWords + 1):
            tempFreq = {}
            
            for j, word in enumerate(words):
                index = i + j * eachWordLen
                sub = s[index : index + eachWordLen]
                
                if sub not in freq:
                    break
                
                tempFreq[sub] = tempFreq[sub] + 1 if sub in tempFreq else 1
                if tempFreq[sub] > freq[sub]:
                    break
                
                if j + 1 == totalWords:
                    ans.append(i)
        return ans
# Time Complexity: O(N * M * L), where N is the length of s, M is the length of words, and L is the length of each word.
# Space Complexity: O(N * M)


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq = Counter(words)
        ans = []
        eachWordLen = len(words[0])
        totalWords = len(words)
        
        for i in range(len(s) - eachWordLen * totalWords + 1):
            subS = [s[j : j + eachWordLen] for j in range(i, i + eachWordLen * totalWords, eachWordLen)]
            tempFreq = Counter(subS)
            if tempFreq == freq:
                ans.append(i)
        return ans


if __name__ == '__main__': 
    sol = Solution()
    print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))