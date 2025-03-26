# A valid encoding of an array of words is any reference string s and array of indices indices such that:

# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
# Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

 

# Example 1:

# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
# Example 2:

# Input: words = ["t"]
# Output: 2
# Explanation: A valid encoding would be s = "t#" and indices = [0].


from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.child = [None] * 26

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        currentNode = self.root
        isNewNode = False
        
        for char in word:
            index = ord(char) - 97
            if currentNode.child[index] is None:
                currentNode.child[index] = TrieNode()
                isNewNode = True

            currentNode = currentNode.child[index]
        return isNewNode


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trieObj = Trie()
        bucket = defaultdict(list)
        count = maxlength = 0
        
        for word in words:
            length = len(word)
            bucket[length].append(word)
            maxlength = max(maxlength, length) 
            
        for length in range(maxlength, 0, -1):
            for word in bucket[length]:
                if trieObj.insert(word[::-1]):
                    count += len(word) + 1

        return count
# Time Complexity: O(W * K)
# Space Complexity: O(W * K)
# W = number of words
# K = length of longest word


if __name__ == '__main__':
    obj = Solution()
    
    words = ["time", "me", "bell"]
    print(obj.minimumLengthEncoding(words))

    words = ["t"]
    print(obj.minimumLengthEncoding(words))