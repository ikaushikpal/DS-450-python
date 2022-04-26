# Given a string s, return the number of distinct substrings of s.
# A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

# Example 1:
# Input: s = "aabbaba"
# Output: 21
# Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]

# Example 2:
# Input: s = "abcdefg"
# Output: 28

# Example 3:
# Input: s = "abab"
# Output: 7
# Explanation: ['a', 'ab', 'abc', 'abab', 'b', 'ba', bab']


from typing import List, Optional


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.word_count: int = word_count

    def __str__(self) -> str:
        return f"{self.value}-{self.word_count}-{self.prefix_count}"

    def __repr__(self) -> str:
        return self.__str__()


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.countNodes = 0

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)
                self.countNodes += 1

            curr = curr.children[index]
        curr.word_count += 1


class Solution:
    def countDistinctSubstring(self, s: str) -> int:
        trieObj = Trie()
        for i in range(len(s)):
            for j in range(i, len(s)):
                trieObj.insert(s[j:])

        return trieObj.countNodes
# Time Complexity: O(|s|^2)        
# Time Complexity: O(|s|^2)        


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDistinctSubstring('abab')) # output 7
