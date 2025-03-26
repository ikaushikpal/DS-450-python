# Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

# Implement the WordFilter class:

# WordFilter(string[] words) Initializes the object with the words in the dictionary.
# f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

# Example 1:

# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]

# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".


from typing import List


class TrieNode:
    def __init__(self, char=None):
        self.data = char
        self.child = [None] * 26
        self.indices = set()

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, string, index):
        if len(string) == 0:
            return

        curr = self.root

        for char in string:
            charIdx = ord(char) - 97

            if curr.child[charIdx] is None:
                curr.child[charIdx] = TrieNode(char)
            
            curr.indices.add(index)
            curr = curr.child[charIdx]

    def search(self, string):
        if len(string) == 0:
            return set()

        curr = self.root
        for char in string:
            idx = ord(char) - 97
            if curr is None:
                return set()
            curr = curr.child[idx]
        return curr.indices

class WordFilter:

    def __init__(self, words: List[str]):
        self.forward = Trie()
        self.backward = Trie()
        
        for i, word in enumerate(words):
            self.forward.insert(word, i)
            self.backward.insert(word[::-1], i)
            
    def f(self, prefix: str, suffix: str) -> int:
        idx1 = self.forward.search(prefix)
        idx2 = self.backward.search(suffix[::-1])
        commonIdx = idx1.intersection(idx2)
        
        if len(commonIdx) > 0:
            return max(commonIdx)
        return -1


if __name__ == "__main__":
    words = ["apple", "app", "ap"]
    wordFilter = WordFilter(words)
    print(wordFilter.f("a", "e"))
    print(wordFilter.f("a", "p"))
    print(wordFilter.f("app", "ple"))
    print(wordFilter.f("ap", "app"))