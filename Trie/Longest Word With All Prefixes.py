# Given an array of strings words, find the longest string in words such that every prefix of it is also in words.

# For example, let words = ["a", "app", "ap"]. The string "app" has prefixes "ap" and "a", all of which are in words.
# Return the string described above. If there is more than one string with the same length, return the lexicographically smallest one, and if no string exists, return "".

# Example 1:
# Input: words = [“k”,”ki”,”kir”,”kira”, “kiran”]
# Output: “kiran”
# Explanation: “kiran” has prefixes “kira”, “kir”, “ki”, and “k”, and all of them appear in words.

# Example 2:
# Input: words = [“a”, “banana”, “app”, “appl”, “ap”, “apply”, “apple”]
# Output: “apple”
# Explanation: Both “apple” and “apply” have all their prefixes in words. However, “apple” is lexicographically smaller, so we return that.

# Example 3:
# Input: words = [“abc”, “bc”, “ab”, “qwe”]
# Output: ''

from typing import List, Optional


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.word_count: int = word_count
        self.hasChild: bool = False

    def __str__(self) -> str:
        return f"{self.value}-{self.word_count}-{self.prefix_count}"

    def __repr__(self) -> str:
        return self.__str__()


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)

            curr.hasChild = True
            curr = curr.children[index]
        curr.word_count += 1

    def search(self, root: Optional[TrieNode], word) -> str:
        # leaf node
        if not root.hasChild:
            if root.word_count > 0:
                return word
            else:
                return ''
        
        for child in root.children:
            if child and child.word_count > 0:
                ret = self.search(child, word + child.value)
                if len(ret) > 0:
                    return ret
        return ''


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trieObj = Trie()
        for word in words:
            trieObj.insert(word)
        return trieObj.search(trieObj.root, '')


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestWord(['k','ki','kir','kira', 'kiran']))


