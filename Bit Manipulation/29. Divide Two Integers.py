# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

# Constraints:
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True

        if dividend <= 0 and divisor > 0:
            sign = False
        
        if dividend > 0 and divisor <= 0:
            sign = False

        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Outer loop runs O(log N) times where N = dividend
        while dividend >= divisor:
            count = 0
            # Inner loop runs O(log N) times to find max shift
            while dividend >= (divisor << (count + 1)):
                count += 1

            quotient += 1 << count
            dividend = dividend - (divisor << count)
        
        # Handle overflow (clamping to 32-bit signed int range)
        if quotient == (1 << 31) and sign:
            return (1 << 31) - 1

        if quotient == (1 << 31) and not sign:
            return -(1 << 31)

        if not sign:
            return -quotient
        return quotient

# Time Complexity: O(log² N), where N = abs(dividend)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.divide(dividend = 10, divisor = 3))
    print(sol.divide(dividend = 7, divisor = -3))
