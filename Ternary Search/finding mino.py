# You have been given an Unimodal function:
# f(x) = 2x^2 - 12x + 17
# with N intervals. For each interval you will be given two integer values l and r , where  and you need to find the minimum value of  where x will be in the range  (both inclusive).

# Sample Input
# 1
# 6 8

# Sample Output
# 7


from math import pow


class Solution:
    def computeFx(self, x):
        return (2*pow(x, 2)) -12*x + 7

    def findingMino(self, left, right):
        error = 10e-6
        
        while right - left > error:
            m1 = left + (right - left) / 3
            m2 = right - (right - left) / 3

            f1 = self.computeFx(m1)
            f2 = self.computeFx(m2)
            
            if f1 < f2:
                right = m2
            else:
                left = m1
        
        return self.computeFx(left)


# reading inputs
sol = Solution()
t = int(input())

for _ in range(t):
    left, right = map(int, input().split())
    print(round(sol.findingMino(left, right)))
