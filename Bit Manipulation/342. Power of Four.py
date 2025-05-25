# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.


# Example 1:
# Input: n = 16
# Output: true

# Example 2:
# Input: n = 5
# Output: false

# Example 3:
# Input: n = 1
# Output: true
 

# Constraints:
# -2^31 <= n <= 2^31 - 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0

    def isPowerOfFour(self, n: int) -> bool:
        if not self.isPowerOfTwo(n):
            return False

        # instead of the loop can use 0x55555555 which is 0101 0101 0101 0101 0101 0101 0101 0101
        while n > 4:
            n = n >> 2
        
        if n == 4 or n == 1:
            return True
        return False
# Time Complexity: O(log4(N))
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfFour(16))
    print(sol.isPowerOfFour(5))
    print(sol.isPowerOfFour(1))