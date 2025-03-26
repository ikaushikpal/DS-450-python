# Given an array of strings arr[] of size N, find if there exists 2 strings arr[i] and arr[j] such that arr[i]+arr[j] is a palindrome i.e the concatenation of string arr[i] and arr[j] results into a palindrome.


# Example 1:
# Input:
# N = 6
# arr[] = {"geekf", "geeks", "or","keeg", "abc", 
#           "bc"}
# Output: 1 
# Explanation: There is a pair "geekf"
# and "keeg".


# Example 2:
# Input:
# N = 5
# arr[] = {"abc", "xyxcba", "geekst", "or", "bc"}
# Output: 1
# Explanation: There is a pair "abc"
# and "xyxcba".


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.eos = 0
        
        
def insert(root,key):
    curr = root
    for char in key:
        index = ord(char) - 97
        if not curr.children[index]:
            newNode = TrieNode()
            curr.children[index] = newNode
        curr = curr.children[index]
    curr.eos += 1

def search(root, key):
    curr = root
    for char in key:
        index = ord(char) - 97
        if not curr.children[index]:
            return 0
        curr = curr.children[index]
    return curr.eos
    
    
class Solution:
    def palindromepair(self, N, words):
        t = TrieNode()
        for word in words:
            insert(t, word)
        
        for word in words:
            for i in range(len(word)):
                rightHalf = word[:i+1][::-1]
                newW = word + rightHalf
                
                if rightHalf == word:
                    if search(t, rightHalf) >= 2:
                        return 1
                        
                elif newW == newW[::-1]:
                    if search(t, rightHalf) > 0:
                        return 1
                        
            wordRev = word[::-1]
            for i in range(len(word)):
                leftHalf = wordRev[:i+1]
                newW = leftHalf + word
                
                if leftHalf == word:
                    if search(t, word) >= 2:
                        return 1
                        
                elif newW == newW[::-1]:
                    if search(t, leftHalf) > 0:
                        return 1
        return 0
# Time Complexity: O(N*l*l)
# Space Complexity: O(N*l)
# N = number of words
# l = length of each word


sol = Solution()
print(sol.palindromepair(6, ["geekf", "geeks", "or","keeg", "abc", "bc"]))
print(sol.palindromepair(5, ["xyxcba","abc", "geekst", "or", "bc"]))