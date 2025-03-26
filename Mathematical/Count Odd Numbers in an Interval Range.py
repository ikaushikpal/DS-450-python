# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).


# Example 1:
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].


# Example 2:
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return high - (high >> 1) - (low >> 1)
# Time Complexity: O(1)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countOdds(3, 7))
    print(sol.countOdds(8, 10))