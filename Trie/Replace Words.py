# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

# Example 1:
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

# Example 2:
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"

from typing import List, Optional


class TrieNode:
    def __init__(self, value=None):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.isEnd: bool = False


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
        curr.isEnd = True

    def search(self, root: Optional[TrieNode], searchWord: str, word: str) -> str:
        for i, char in enumerate(searchWord):
            index = ord(char) - 97
            child = root.children[index]

            if not child:
                return ''

            if child.isEnd:
                return searchWord[:i+1]

            root = child

        if root.isEnd:
            return searchWord
        else:
            return ''


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trieObj = Trie()
        for word in dictionary:
            trieObj.insert(word)
        
        words = list(sentence.split(' '))
        for i, word in enumerate(words):
            string = trieObj.search(trieObj.root, word, '')
            if len(string) > 0:
                words[i] = string
        
        return ' '.join(words)


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
    print(sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))