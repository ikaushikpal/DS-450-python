class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        res = 0
        sign = 1

        for digit in n:
            res += sign * int(digit)
            sign *= -1
        return res