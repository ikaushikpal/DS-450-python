# Given two integers num and k, consider a set of positive integers with the following properties:

# The units digit of each integer is k.
# The sum of the integers is num.
# Return the minimum possible size of such a set, or -1 if no such set exists.

# Note:

# The set can contain multiple instances of the same integer, and the sum of an empty set is considered 0.
# The units digit of a number is the rightmost digit of the number.
 

# Example 1:
# Input: num = 58, k = 9
# Output: 2
# Explanation:
# One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
# Another valid set is [19,39].
# It can be shown that 2 is the minimum possible size of a valid set.


# Example 2:
# Input: num = 37, k = 2
# Output: -1
# Explanation: It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.


# Example 3:
# Input: num = 0, k = 7
# Output: 0
# Explanation: The sum of an empty set is considered 0.


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        
        for i in range(1, 11):
            if (i * k) % 10 == num % 10 and i * k <= num:
                return i
        return -1
# Time Complexity: O(10) = O(1)
# Space Complexity: O(1)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumNumbers(58, 9))