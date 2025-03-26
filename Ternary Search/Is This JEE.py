# Everyone loves short problem statements.

# Given a function f(x) find its minimum value over the range 0<x<π/2
# f(x)=(x^2 + b∗x + c)/sin(x)

# Input:
# First-line will contain T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, two real numbers b,c.
# Output:
# For each test case, output the minimum value of f(x) over the given range. Absolute error of 10−6 is allowed.


# Constraints
# 1≤T≤100000
# 1≤b,c≤20

# Sample Input:
# 1
# 2 2

# Sample Output:
# 5.8831725615

from math import pow, pi, sin


class Solution:
    def computeFx(self, x, b, c):
        return (pow(x, 2) + b*x + c) / sin(x)

    def minimumJee(self, b, c):
        left, right = 0.0, pi/2
        error = 10e-6

        while right - left > error:
            m1 = left + (right - left) / 3
            m2 = right - (right - left) / 3

            f1 = self.computeFx(m1, b, c)
            f2 = self.computeFx(m2, b, c)
            
            if f1 < f2:
                right = m2
            else:
                left = m1
        
        return self.computeFx(left, b, c)


# reading inputs
sol = Solution()
t = int(input())

for _ in range(t):
    b, c = map(float, input().split())
    print(sol.minimumJee(b, c))