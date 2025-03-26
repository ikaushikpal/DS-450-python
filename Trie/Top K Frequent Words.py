# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Example 1:
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

# Example 2:
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


from typing import List, Optional


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.word_count: int = word_count

class Trie:

    def __init__(self, n):
        self.root = TrieNode()
        self.freq = [[] for _ in range(n + 1)]

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)

            curr = curr.children[index]
        curr.word_count += 1

    def search(self, root, k, word):
        if root is None:
            return
        
        if root.word_count > 0:
            self.freq[root.word_count].append(word)

        for child in root.children:
            if child:
                self.search(child, k, word + child.value)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trieObj = Trie(len(words))
        for word in words:
            trieObj.insert(word)
        
        trieObj.search(trieObj.root, k, '')
        ans = []
        for i in range(len(trieObj.freq)-1, 0,- 1):
            for word in trieObj.freq[i]:
                ans.append(word)
                if len(ans) == k:
                    return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
    print(sol.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))