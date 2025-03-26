# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

# Example 1:
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

# Example 2:
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

# Example 3:
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
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

    def search(self, root: Optional[TrieNode], searchWord: str, word: str) -> str:
        if root is None:
            return

        if self.remaining == 0:
            return

        if len(searchWord) > 0:
            child = root.children[ord(searchWord[0]) - 97]
            if child:
                self.search(child,
                            searchWord[1:],
                            word + child.value)
            else:
                return
        else:
            if root.word_count > 0:
                self.res.append(word)
                self.remaining -= 1

            for child in root.children:
                if child and self.remaining > 0:
                    self.search(child, '', word + child.value)
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trieObj = Trie()
        for word in products:
            trieObj.insert(word)

        res = []
        for i in range(1, len(searchWord) + 1):
            trieObj.res = []
            trieObj.remaining = 3
            trieObj.search(trieObj.root, searchWord[:i], '')
            res.append(trieObj.res)

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"), end='\n')
    print(sol.suggestedProducts(products = ["havana"], searchWord = "havana"))
