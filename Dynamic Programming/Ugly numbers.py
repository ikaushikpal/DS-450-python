class Solution:
    def maxDiv(self, x, y):
        while x%y == 0:
            if x in self.dp:
                return 1

            x = x / y
        
        return x

    def checkOne(self, num):
        return True if num == 1 else False

    def isUgly(self, num):
        num = self.maxDiv(num, 2)
        num = self.maxDiv(num, 3)
        num = self.maxDiv(num, 5)

        return self.checkOne(num)
        
    def getNthUglyNo(self, n):
        count = 1
        num = 1
        self.dp = {}

        while count < n:
            num += 1
            if self.isUgly(num):
                self.dp[num] = True
                count += 1
        
        return num


if __name__ == "__main__":
    n = 7
    s = Solution()
    print(s.getNthUglyNo(n))