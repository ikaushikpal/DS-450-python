# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.


# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5


# Example 2:
# Input: c = 3
# Output: false


from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, int(sqrt(c))
        while low <= high:
            curr = low*low + high*high
            if curr == c:
                return True
            elif curr > c:
                high -= 1
            else:
                low += 1
        return False
# Time: O(sqrt(c))
# Space: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.judgeSquareSum(5))
    print(sol.judgeSquareSum(3))
    