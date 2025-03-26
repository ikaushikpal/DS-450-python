# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

from collections import defaultdict


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value = value
        self.child = defaultdict(lambda : None)
        self.word_count = word_count


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.child[char] is None:
                curr.child[char] = TrieNode(char)
            curr = curr.child[char]
        curr.word_count += 1

    def search(self, word: str) -> bool: 
        curr = self.root
        for char in word:
            if curr.child[char] is None:
                return False
            curr = curr.child[char]

        if curr.word_count > 0:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if curr.child[char] is None:
                return False
            curr = curr.child[char]
        return True
