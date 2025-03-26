# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.


# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.


# Example 3:
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


from typing import List


class Solution:
    def isBigger(self, string1, string2, mapper):
        N, M = len(string1), len(string2)
        
        for char1, char2 in zip(string1, string2):
            if char1 != char2:
                return mapper[char1] > mapper[char2]
        return N > M
    
    def buildMapper(self, order):
        return {char:i for i, char in enumerate(order)}
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapper = self.buildMapper(order)
        for i in range(1, len(words)):
            if self.isBigger(words[i - 1], words[i], mapper):
                return False
        return True
# Time Complexity: O(2*M*N) = O(M*N)
# Space Complexity: O(26) = O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
    print(sol.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
    print(sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))