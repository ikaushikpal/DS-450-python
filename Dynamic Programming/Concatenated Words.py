# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.


# Example 1:
# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".


# Example 2:
# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
 

from typing import List


class Solution:
    def dfs(self, word, memo, wordSet):
        if word in memo:
            return memo[word]
        
        memo[word] = False
        # string is comprised entirely of at least two shorter words in the given array.
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            
            if prefix in wordSet and suffix in wordSet:
                memo[word] = True 
                break
                
            if prefix in wordSet and self.dfs(suffix, memo, wordSet):
                memo[word] = True
                memo[suffix] = True 
                break
                
        return memo[word] 
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        memo = {}
        
        return [word for word in words if self.dfs(word, memo, wordSet)] 
# Time Complexity: O(n * k^2) where n is the number of words and k is the length of the longest word
# Space Complexity: O(n * k^2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
    print(sol.findAllConcatenatedWordsInADict(["cat","dog","catdog"]))

