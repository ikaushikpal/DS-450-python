# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

 

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]


# Example 2:
# Input: s = "a"
# Output: [["a"]]


from functools import cache


class Solution(object):
    @cache  # the memory trick can save some time
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
# Time Complexity:
# Space Complexity: O(N ^ 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.partition(s = "aab"))
    print(sol.partition(s = "a"))
