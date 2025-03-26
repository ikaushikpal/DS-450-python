# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

# Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

# Example 1:
# Input: n = 3
# Output: 3
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.


# Example 2:
# Input: n = 1
# Output: 0


class Solution:
    def helper(self, s, cp, n):
        if len(s) == n:
            return 0
        
        if len(s) > n:
            return float('inf')

        if (s, cp) in self.memo:
            return self.memo[(s, cp)]

        if cp:
            self.memo[(s, cp)] = min(self.helper(s+cp, cp, n) + 1, self.helper(s+s, s, n) + 2) 
        else:
            self.memo[(s, cp)] = self.helper(s+s, s, n) + 2
        
        return self.memo[(s, cp)]

    def minSteps(self, n: int) -> int:
        self.memo = {}
        return self.helper('A', '', n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSteps(3))
    print(sol.minSteps(1))
    print(sol.minSteps(10))