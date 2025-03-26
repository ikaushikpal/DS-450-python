# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".


# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


from typing import List


class Solution:  
    def findAnagrams(self, s: str, p: str) -> List[int]:
        M, N = len(s), len(p)
        
        ans = []
        window = [0] * 26
        freq_p = [0] * 26
        
        for char in p:
            freq_p[ord(char) - 97] += 1
        
        for i in range(M):
            window[ord(s[i]) - 97] += 1

            if i >= N:
                window[ord(s[i - N]) - 97] -= 1
            
            if freq_p == window:
                ans.append(i - N + 1)
                
        return ans


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))
    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s, p))