# Given two strings of lowercase alphabets and a value K, your task is to complete the given function which tells if  two strings are K-anagrams of each other or not.

# Two strings are called K-anagrams if both of the below conditions are true.
# 1. Both have same number of characters.
# 2. Two strings can become anagram by changing at most K characters in a string.

# Example:

# Input:
# str1 = "fodr", str2="gork"
# k = 2
# Output:
# 1
# Explanation: Can change fd to gk

# https://practice.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1/#
class Solution:
    def areKAnagrams(self, str1, str2, k):
        freq1 = [0] * 26
        freq2 = [0] * 26

        for char in str1:
            freq1[ord(char) - ord('a')] += 1
        
        for char in str2:
            freq2[ord(char) - ord('a')] += 1

        count = 0
        for i in range(26):
            if freq1[i] - freq2[i] >= 0:
                count += freq1[i] - freq2[i]
            
            if count > k:
                return False
        return True
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.areKAnagrams("fodr", "gork", 2))