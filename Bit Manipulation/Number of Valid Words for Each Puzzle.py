# With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
# invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].
 

# Example 1:

# Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation: 
# 1 valid word for "aboveyz" : "aaaa" 
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.


# Example 2:
# Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
# Output: [0,1,3,2,0]


from collections import Counter
from typing import List


class Solution:
    def genFullBitRepr(self, string):
        res = 0
        for s in string:
            index = ord(s) - ord('a')
            res |= 1 << index
        return res
    
    def genFirstLetterBitRepr(self, string):
        s = string[0]
        index = ord(s) - ord('a')
        return 1 << index
    
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        binWords = [self.genFullBitRepr(word) for word in words]
        binWordsFreq = Counter(binWords)

        ans = []
        for i in range(len(puzzles)):
            binPuzzle = self.genFullBitRepr(puzzles[i])
            binPuzzleFirstLetter = self.genFirstLetterBitRepr(puzzles[i])
            count = 0
            
            for binWord, freq in binWordsFreq.items():
                containsAllLetters = binPuzzle & binWord == binWord
                containsFirstLetter = binWord & binPuzzleFirstLetter
                if containsAllLetters and containsFirstLetter:
                    count += freq
            ans.append(count)
        return ans
# Time Complexity: O(N^2)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
    print(sol.findNumOfValidWords(["apple","pleas","please"], ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]))
