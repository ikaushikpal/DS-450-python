# Given a positive integer n, you can apply one of the following operations:

# If n is even, replace n with n / 2.
# If n is odd, replace n with either n + 1 or n - 1.
# Return the minimum number of operations needed for n to become 1.

 
# Example 1:
# Input: n = 8
# Output: 3
# Explanation: 8 -> 4 -> 2 -> 1


# Example 2:
# Input: n = 7
# Output: 4
# Explanation: 7 -> 8 -> 4 -> 2 -> 1
# or 7 -> 6 -> 3 -> 2 -> 1


# Example 3:
# Input: n = 4
# Output: 2


class Memo:
    memo = {}

    
class Solution:
    def helper(self, n):
        if n == 1:
            return 0
        
        if n in Memo.memo:
            return Memo.memo[n]
        
        if n & 1:
            Memo.memo[n] = min(self.helper(n + 1), self.helper(n - 1)) + 1
        else:
            Memo.memo[n] = 1 + self.helper(n // 2)
        return Memo.memo[n]
        
    def integerReplacement(self, n: int) -> int:
        return self.helper(n)
# Time Complexity: O(log n)
# Space Complexity: O(log n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.integerReplacement(8))
    print(sol.integerReplacement(7))
    print(sol.integerReplacement(4))