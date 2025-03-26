# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

 

# Example 1:

# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:

# Input: words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".


from typing import List, Optional


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.word_count: int = word_count

    def __repr__(self) -> str:
        return f'{self.value}:{self.word_count}'


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.max_length = 0
        self.res = None

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)

            curr = curr.children[index]
        curr.word_count += 1

    def search(self, root, word):
        if root is None:
            return 
        
        if root != self.root and root.word_count == 0:
            return
        
        if len(word) > self.max_length:
            self.max_length = len(word)
            self.res = word
        
        for child in root.children:
            if child:
                self.search(child, word + child.value)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trieObj = Trie()
        for word in words:
            trieObj.insert(word)
        
        trieObj.search(trieObj.root, '')
        return trieObj.res
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestWord(words = ["w","wo","wor","worl","world"]))