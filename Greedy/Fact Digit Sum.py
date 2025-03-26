# A(X) for positive integer X is the sum of factorials of its digits. For example, A(154) = 1! + 5! + 4!= 145.
# Given a number N, find the minimum number X such that A(X) = N. You have to return a list of digits which represent the number X.


# Example 1:
# Input: N = 40321
# Output: 18
# Explanation: A(18)=1!+ 8! =40321 
# Note that A(80) and A(81) are also 
# 40321, But 18 is the smallest 
# number.


# Example 2:
# Input: N = 5040
# Output: 7
# Explanation: A(7) = 7! = 5040.


class Solution:
    def factArray(self, n=9):
        arr = [1]
        for i in range(1, n+1):
            arr.append(arr[-1] * i)
        return arr

    def FactDigit(self, num):
        fact = self.factArray()
        res = []
        for i in range(9, -1, -1):
            div = num // fact[i]
            res.extend([i] * div)
            num = num - div * fact[i]
        return res[::-1]
# Time Complexity: O(X) where X is the number of digits in answer.
# Space Complexity: O(X)

if __name__ == '__main__':
    sol = Solution()
    print(sol.FactDigit(40321))
    print(sol.FactDigit(5040))