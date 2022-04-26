# Given an array of words, find all shortest unique prefixes to represent each word in the given array. Assume that no word is prefix of another.

# Example 1:

# Input: 
# N = 4
# arr[] = {"zebra", "dog", "duck", "dove"}
# Output: z dog du dov
# Explanation: 
# z => zebra 
# dog => dog 
# duck => du 
# dove => dov 
# Example 2:

# Input: 
# N = 3
# arr[] =  {"geeksgeeks", "geeksquiz",
#                        "geeksforgeeks"};
# Output: geeksg geeksq geeksf
# Explanation: 
# geeksgeeks => geeksg 
# geeksquiz => geeksq 
# geeksforgeeks => geeksf

from collections import defaultdict


class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = defaultdict(lambda: None)
        self.prefix = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)
            curr.prefix += 1
            curr = curr.children[index]
    
    def search(self, root, remaining_word):
        for i, char in enumerate(remaining_word):
            index = ord(char) - 97
            root = root.children[index]
            if root.prefix == 1:
                return remaining_word[:i+1]
        return remaining_word


class Solution:
    def findPrefixes(self, words, _):
        trieObj = Trie()
        for word in words:
            trieObj.insert(word)

        for i, word in enumerate(words):
            words[i] = trieObj.search(trieObj.root, word)
        return words

