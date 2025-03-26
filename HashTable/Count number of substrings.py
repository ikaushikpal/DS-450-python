# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 


# Example 1:
# Input:
# S = "aba", K = 2
# Output:
# 3
# Explanation:
# The substrings are:
# "ab", "ba" and "aba".


# Example 2:
# Input: 
# S = "abaaca", K = 1
# Output:
# 7
# Explanation:
# The substrings are:
# "a", "b", "a", "aa", "a", "c", "a". 
from collections import defaultdict


class Solution:
    def helper(self, string, k):
        hashMap = defaultdict(int)
        count = 0
        i, j = 0, 0

        while j < len(string):
            hashMap[string[j]] += 1

            while len(hashMap) > k:
                hashMap[string[i]] -= 1
                if hashMap[string[i]] == 0:
                    del hashMap[string[i]]
                i += 1
            
            count += (j - i + 1)
            j += 1

        return count

    def substrCount(self, string, k):
        return self.helper(string, k) - self.helper(string, k - 1)
# Time Complexity: O(N)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.substrCount("aba", 2))
    print(sol.substrCount("abaaca", 1))