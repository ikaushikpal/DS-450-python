# Given two strings denoting non-negative numbers X and Y. Calculate the sum of X and Y.


# Example 1:
# Input:
# X = "25", Y = "23"
# Output:
# 48
# Explanation:
# The sum of 25 and 23 is 48.


# Example 2:
# Input:
# X = "2500", Y = "23"
# Output:
# 2523
# Explanation:
# The sum of 2500 and 23 is 2523.


class Solution:
    def findSum(self, X, Y):
        X = X[::-1]
        Y = Y[::-1]
        Z = ''
        carry = i = j = 0

        while i < len(X) and j < len(Y):
            tot = int(X[i]) + int(Y[j]) + carry
            digit = tot % 10
            carry = tot // 10
            Z += str(digit)
            i += 1
            j += 1

        while i < len(X):
            tot = int(X[i]) + carry
            digit = tot % 10
            carry = tot // 10
            Z += str(digit)
            i += 1

        while j < len(Y):
            tot = int(Y[j]) + carry
            digit = tot % 10
            carry = tot // 10
            Z += str(digit)
            j += 1

        if carry == 1:
            Z += str(carry)

        Z = Z[::-1].lstrip('0')
        return '0' if not Z else Z
# TC : O(M + N)
# SC : O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSum('25', '23'))
    print(sol.findSum('2500', '23'))