# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:

# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

from typing import List, Optional


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.word_count: int = word_count


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)

            curr = curr.children[index]
        curr.word_count += 1

    def search(self, root: Optional[TrieNode], s: str, word: str) -> str:
        if root is None:
            return 
        
        if len(s) == 0:
            self.ans.append(word[1:])
        else:
            for i, char in enumerate(s):
                index = ord(char) - 97
                child = root.children[index]
                if child:
                    if child.word_count > 0:
                        self.search(self.root, s[i+1:], f'{word} {s[:i+1]}')
                    root = child
                else:
                    return

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trieObj = Trie()
        for word in wordDict:
            trieObj.insert(word)

        trieObj.ans = []
        trieObj.search(trieObj.root, s, '')
        return trieObj.ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
