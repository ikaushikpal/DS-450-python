# Given a String S, Find all possible Palindromic partitions of the given String.


# Example 1:
# Input:
# S = "geeks"
# Output:
# g e e k s
# g ee k s
# Explanation:
# All possible palindromic partitions
# are printed.


# Example 2:
# Input:
# S = "madam"
# Output:
# m a d a m
# m ada m
# madam


class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def helper(self, s, res):
        if len(s) == 0:
            self.ans.append(res[:])
            return

        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                res.append(s[:i+1])
                self.helper(s[i+1:], res)
                res.pop()
        
    def allPalindromicPerms(self, s):
        self.ans = []
        self.helper(s, [])
        return self.ans
# Time Complexity: O(N * N * N) = O(N^3)
# Space Complexity: O(N * N) = O(N^2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.allPalindromicPerms("geeks"))
    print(sol.allPalindromicPerms("madam"))
    